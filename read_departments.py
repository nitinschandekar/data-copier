import pandas as pd
import os

def read_order():
    conn = 'postgresql://retail_user:itversity@localhost:5452/retail_db'
    query = 'Select * from orders'
    df = pd.read_sql(query, conn)
    print(df)


def main():
    path = os.environ['PATH']
    print("PATH env var is ", path)

if (__name__ == '__main__'):
    main()

