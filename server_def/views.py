from django.http import HttpResponse
from server_def.singleton import DatabaseConnectionManager
from server_def.models import ServerFactory

def index(request):
    connection_manager = DatabaseConnectionManager()
    connection_manager.get_connection("postgresql")
    connection_manager.get_connection("mysql")

    try:
        postgres_server = ServerFactory.create_server("postgresql", "prod-db", "192.168.1.10")
        mysql_server = ServerFactory.create_server("mysql", "dev-db", "192.168.1.20")
        
        html_content = f"""
        <h1>Система учёта серверов СУБД</h1>
        <p><b>ID Singleton:</b> {id(connection_manager)}</p>
        <p><b>Активные подключения:</b> {connection_manager.get_all_connections()}</p>
        <hr>
        <p><b>Сервер 1:</b> {postgres_server.get_info()}</p>
        <p><b>Сервер 2:</b> {mysql_server.get_info()}</p>
        """
        
    except Exception as error:
        html_content = f"<h1>Произошла ошибка:</h1><p>{error}</p>"

    return HttpResponse(html_content)


def server_list(request):
    try:
        available_types = ServerFactory.get_available_types()
        list_items = "".join([f"<li>{db_type}</li>" for db_type in available_types])
        
        html_content = f"""
        <h1>Доступные типы серверов в Factory</h1>
        <ul>{list_items}</ul>
        <a href="/servers/">Назад на главную</a>
        """
    except Exception as error:
        html_content = f"<h1>Ошибка:</h1><p>{error}</p>"

    return HttpResponse(html_content)