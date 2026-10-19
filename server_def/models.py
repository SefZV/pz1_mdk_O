from django.db import models

class DatabaseServer:
    def __init__(self, name: str, ip_address: str):
        self.name = name
        self.ip_address = ip_address

    def get_info(self) -> str:
        raise NotImplementedError("Метод должен быть переопределен в наследниках")

class PostgreSQLServer(DatabaseServer):
    def get_info(self) -> str:
        return f"PostgreSQL: {self.name} ({self.ip_address}:5432)"

class MySQLServer(DatabaseServer):
    def get_info(self) -> str:
        return f"MySQL: {self.name} ({self.ip_address}:3306)"

class OracleServer(DatabaseServer):
    def get_info(self) -> str:
        return f"Oracle: {self.name} ({self.ip_address}:1521)"

class ServerFactory:
    _registry = {
        "postgresql": PostgreSQLServer,
        "oracle": OracleServer,
        "mysql": MySQLServer,
    }

    @classmethod
    def create_server(cls, server_type: str, name: str, ip_address: str):
        try:
            if server_type not in cls._registry:
                raise ValueError(f"Неизвестный тип сервера: '{server_type}'")
            
            server_class = cls._registry[server_type]
            return server_class(name, ip_address)
            
        except ValueError as error:
            print(f"Ошибка фабрики: {error}")
            raise error

    @classmethod
    def get_available_types(cls):
        return list(cls._registry.keys())