import pandas as pd 
import os
import sys
from dotenv import load_dotenv

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_path)

from contract.contract.contract import Transaction 




load_dotenv("keys/.env")

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

def process_csv(uploaded_file):
    try:
        df = pd.read_csv(uploaded_file)
        
        extra_cols = set(df.columns) - set(Transaction.model_fields.keys())
        if extra_cols:
            return False, f"CSV file contains extra columns: {', '.join(extra_cols)}"

        missing_cols = set(Transaction.model_fields.keys()) - set(df.columns)
        if missing_cols:
            return False, f"CSV file is missing columns: {', '.join(missing_cols)}"

        #df = df.rename(columns=contract.model_fields)
        
        for index, row in df.iterrows():
            try:
                _ = Transaction(**row.to_dict())
            except Exception as e:
                raise ValueError(f"Row {index + 1}: {e}")
        
        return df, True, None
    
    except ValueError as ve:
        return df, False, str(ve)
    except Exception as e:
        return df, False, f"Unexpected Error: {str(e)}"
    
def csv_to_sql(df):
    try:
        df.to_sql(name="transactions", con=DATABASE_URL, if_exists="replace", index=False)
        return True, None
    except Exception as e:
        return False, str(e)