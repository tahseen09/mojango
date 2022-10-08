from pymongo import MongoClient

class MongoConnection:
    def __init__(self, host: str = "localhost", port: int=27017) -> None:
        self.host = host
        self.port = port
        self.connection = self.get_connection()

    def get_connection(self):
        return MongoClient(self.host, self.port)

    def get_database(self, database_name: str):
        return self.connection[database_name]
