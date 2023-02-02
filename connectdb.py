import os
import psycopg2

class cdb:
    def connect(self,query):
        conn = psycopg2.connect(
                host="localhost",
                database="local_1",
                user=os.environ['PostgreSQL 14'],
                password=os.environ['root'])

        # Open a cursor to perform database operations
        cur = conn.cursor()

        # Execute a command: this creates a new table
        cur.execute()

        # Insert data into the table



        conn.commit()

        cur.close()
        conn.close()