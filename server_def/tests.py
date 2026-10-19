from django.test import TestCase
from server_def.singleton import DatabaseConnectionManager
from server_def.models import (
    ServerFactory, PostgreSQLServer, MySQLServer, OracleServer,
)


class SingletonTest(TestCase):
    def test_single_instance(self):
        m1 = DatabaseConnectionManager()
        m2 = DatabaseConnectionManager()
        self.assertIs(m1, m2)

    def test_shared_connections(self):
        m1 = DatabaseConnectionManager()
        m2 = DatabaseConnectionManager()
        m1.get_connection("postgresql")
        self.assertIn("postgresql", m2.get_all_connections())


class FactoryTest(TestCase):
    def test_create_postgresql(self):
        s = ServerFactory.create_server("postgresql", "db1", "10.0.0.1")
        self.assertIsInstance(s, PostgreSQLServer)
        self.assertIn("PostgreSQL", s.get_info())

    def test_create_mysql(self):
        s = ServerFactory.create_server("mysql", "db2", "10.0.0.2")
        self.assertIsInstance(s, MySQLServer)

    def test_create_oracle(self):
        s = ServerFactory.create_server("oracle", "db3", "10.0.0.3")
        self.assertIsInstance(s, OracleServer)

    def test_unknown_type(self):
        with self.assertRaises(ValueError):
            ServerFactory.create_server("mongodb", "x", "10.0.0.4")