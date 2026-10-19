class DatabaseConnectionManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connections = {}
        return cls._instance

    def get_connection(self, db_type: str) -> str:
        try:
            if not isinstance(db_type, str):
                raise TypeError("Тип базы данных должен быть строкой")
                
            if db_type not in self.connections:
                self.connections[db_type] = f"Connection to {db_type}"
                
            return self.connections[db_type]
        except Exception as error:
            return f"Ошибка при подключении: {error}"

    def get_all_connections(self) -> dict:
        return self.connections