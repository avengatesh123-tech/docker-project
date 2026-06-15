import time
import argparse
import pandas as pd
from sqlalchemy import create_engine

def main(params):
    user = params.pg_user       
    password = params.pg_pass   
    host = params.pg_host       
    port = params.pg_port       
    db = params.pg_db           
    table_name = params.target_table

    engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}")
    csv_name = 'airlines_flights_data.csv'
    df = pd.read_csv(csv_name)

    batch_size = 5   
    delay = 5        

    print(f"Starting ingestion into table {table_name}...")

    for start in range(0, len(df), batch_size):
        end = start + batch_size
        df_chunk = df.iloc[start:end]

        df_chunk.to_sql(
            name=table_name,
            con=engine,
            if_exists="append",
            index=False
        )

        print(f"Inserted rows {start} to {end}")
        time.sleep(delay)   # wait 5 seconds

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--pg-user', required=True, help='user name for postgres')
    parser.add_argument('--pg-pass', required=True, help='password for postgres')
    parser.add_argument('--pg-host', required=True, help='host for postgres')
    parser.add_argument('--pg-port', required=True, help='port for postgres')
    parser.add_argument('--pg-db', required=True, help='database name for postgres')
    parser.add_argument('--target-table', required=True, help='name of the table where we will write the results to')

    args = parser.parse_args()
    main(args)