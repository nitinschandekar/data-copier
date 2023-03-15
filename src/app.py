import pandas as pd
import os
from read import get_json_reader
from write import load_db_table


def process_tables(BASE_DIR, conn, table_name):
    json_reader = get_json_reader(BASE_DIR, table_name, chunksize=1000)
    for df in json_reader:
        load_db_table(df, conn, table_name, df.columns[0])


def main():
    BASE_DIR=os.environ.get('BASE_DIR')
    table_names = 'departments,orders'.split(',')
    configs = dict(os.environ.items())
    print("DB_PORT is ", configs["DB_PORT"])
    conn = f'postgresql://{configs["DB_USER"]}:{configs["DB_PASS"]}@{configs["DB_HOST"]}:{configs["DB_PORT"]}/{configs["DB_NAME"]}'
    print ("conn is ", conn)
    for table_name in table_names:
        print("table name is ", table_name)
        process_tables(BASE_DIR, conn, table_name)


if __name__ == '__main__':
    main()