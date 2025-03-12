"""
Advanced Flyweight Pattern Example: Database Connection Pooling
The Flyweight Pattern can be used to optimize database connections by implementing a connection pool. Instead of
creating a new database connection every time a request is made, we reuse existing connections whenever possible.

Scenario:
    * A database-intensive application needs multiple database connections.
    * Creating and closing connections repeatedly is slow and inefficient.
    * We use a connection pool to reuse existing connections, improving performance.

Key Benefits:
    ✅ Optimized Performance: Reduces overhead from frequent database connection creation.
    ✅ Efficient Resource Management: Limits the number of active connections.
    ✅ Improves Scalability: Supports multiple users without overloading the database.
    ✅ Prevents Connection Exhaustion: Ensures the system doesn’t run out of database connections.

Explanation:
    1. Flyweight (DatabaseConnection)
        Represents a shared database connection.
        Simulates executing a query.
    2. Flyweight Factory (DatabaseConnectionPool)
        Maintains a pool of reusable database connections.
        Limits the number of active connections.
        Reuses existing connections whenever possible.
    3. Client (client_simulation())
        Requests a database connection.
        Executes a query.
        Releases the connection back into the pool.
"""

import time
import random

# Flyweight (Shared Database Connection)
class DatabaseConnection:
    def __init__(self, connection_id):
        self.connection_id = connection_id
        print(f"Creating Database Connection {self.connection_id}")

    def execute_query(self, query):
        print(f"Executing query on Connection {self.connection_id}: {query}")
        time.sleep(1)  # Simulating query execution time

# Flyweight Factory (Connection Pool Manager)
class DatabaseConnectionPool:
    _pool = []
    _max_connections = 3  # Limit the number of connections

    @staticmethod
    def get_connection():
        if DatabaseConnectionPool._pool:
            print("Reusing existing connection...")
            return DatabaseConnectionPool._pool.pop()
        elif len(DatabaseConnectionPool._pool) < DatabaseConnectionPool._max_connections:
            connection = DatabaseConnection(len(DatabaseConnectionPool._pool) + 1)
            return connection
        else:
            print("No available connections! Please wait...")
            time.sleep(2)  # Simulating wait time for an available connection
            return DatabaseConnectionPool.get_connection()  # Retry

    @staticmethod
    def release_connection(connection):
        print(f"Releasing Connection {connection.connection_id} back to pool.")
        DatabaseConnectionPool._pool.append(connection)

# Client: Application making database queries
def client_simulation(client_id):
    print(f"\nClient {client_id} requesting database connection...")
    connection = DatabaseConnectionPool.get_connection()
    connection.execute_query(f"SELECT * FROM users WHERE id = {random.randint(1, 100)}")
    DatabaseConnectionPool.release_connection(connection)

# Simulate Multiple Clients Accessing Database
if __name__ == "__main__":
    for i in range(5):  # Simulate 5 clients making queries
        client_simulation(i)
