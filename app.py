import pandas as pd
import os
from read import get_json_reader
from write import load_db_table


def process_tables(BASE_DIR, conn, table_name):
    json_reader = get_json_reader(BASE_DIR, table_name, chunksize=1000)
    for df in json_reader:
        load_db_table(df, conn, table_name, df.columns[0])


def main():
    BASE_DIR='/Users/nitinchandekar/udemy-spark/Research/data/retail_db_json'
    table_names = 'departments,orders'.split(',')
    conn = 'postgresql://retail_user:itversity@localhost:5452/retail_db'
    for table_name in table_names:
        print("table name is ", table_name)
        process_tables(BASE_DIR, conn, table_name)


if __name__ == '__main__':
    main()