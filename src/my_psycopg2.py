# Preparation for this part
#   - pip install psycopg2-binary
#   - have Docker installed
#   - execute 'docker-compose up' in command line (folder of this project)
#   - https://www.psycopg.org/docs/

import psycopg2  
import pandas as pd
import pandas.io.sql as sqlio

# Connect to your postgres DB
conn = psycopg2.connect(dbname="python_course", user="postgres", password="example", host = "localhost")

# Open a cursor to perform database operations
cur = conn.cursor()

sql_create_table = """CREATE TABLE transactions (
            inv_id SERIAL PRIMARY KEY,
            InvoiceNo VARCHAR(255),
            StockCode VARCHAR(255),
            Description VARCHAR(255),
            Quantity real,
            InvoiceDate VARCHAR(255),
            UnitPrice real,
            CustomerID integer,
            Country VARCHAR(255)
        )"""

# Execute a query to create the table
#cur.execute("""DROP table transactions""")
cur.execute(sql_create_table)

conn.commit()

# Execute the copy command to bulk load in data
copy_command = """COPY transactions(InvoiceNo,StockCode,Description,Quantity,InvoiceDate,UnitPrice,CustomerID,Country) FROM '/mnt/data/data.csv' CSV HEADER;"""
cur.execute(copy_command)
conn.commit()
# query specific invoice
query_invoice = """Select * from transactions where InvoiceNo = '536370'"""

# get the results
cur.execute(query_invoice)
records = cur.fetchall()
#print the results
print(records)
#print(records[0])

# get results into pandas dataframe
data = sqlio.read_sql_query(query_invoice, conn)
print(data)

# close communication with the PostgreSQL database server
cur.close()
# commit the changes
conn.commit()