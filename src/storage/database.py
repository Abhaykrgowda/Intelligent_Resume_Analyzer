"""
Database access layer (future extension)

Possible implementations:
- PostgreSQL
- MongoDB
- SQLite
- Cloud databases (IBM Cloud, AWS RDS)
"""

class DatabaseClient:
    def connect(self):
        raise NotImplementedError

    def save_candidate(self, candidate):
        raise NotImplementedError

    def save_report(self, report):
        raise NotImplementedError
