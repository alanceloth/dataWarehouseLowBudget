import pandas as pd 
import os
import sys
from dotenv import load_dotenv
import duckdb as db
import boto3
from loguru import logger

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_path)

from contract.contract.contract import Transaction 

# Inicialização do Loguru
log_directory = "../log"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

log_file_path = os.path.join(log_directory, 'backend_log.log')

logger.add(log_file_path, rotation="500 MB", level="INFO")

logger.info(f"Process started at {pd.Timestamp.now()}")

load_dotenv("keys/.env")

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")

AWS_REGION= os.getenv("AWS_REGION")
AWS_ACCESS_KEY= os.getenv("AWS_ACCESS_KEY")
AWS_SECRET = os.getenv("AWS_SECRET")


DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

def process_csv(uploaded_file):
    """
    Processes a CSV file containing transaction data.

    Args:
        uploaded_file: The path to the uploaded CSV file.

    Returns:
        tuple: A tuple containing three elements:
            - If the CSV file is successfully processed, a DataFrame containing the data, a boolean indicating success (True), and None.
            - If the CSV file contains extra columns or missing columns, a boolean indicating failure (False), and an error message explaining the issue.
            - If an unexpected error occurs during processing, a boolean indicating failure (False), and an error message describing the error.

    Notes:
        This function reads the uploaded CSV file into a DataFrame and validates its structure against the fields expected by the Transaction model.
        If the CSV file contains extra columns or missing columns, the function returns an error message indicating the issue.
        If the CSV file is successfully processed, it constructs Transaction objects from each row and returns a DataFrame containing the data.

    Raises:
        ValueError: If there's an issue with the structure of the CSV file, such as extra or missing columns.
        Any other exceptions raised during processing.
    """
    try:
        df = pd.read_csv(uploaded_file)
        
        extra_cols = set(df.columns) - set(Transaction.model_fields.keys())
        if extra_cols:
            logger.error(f"CSV file contains extra columns: {', '.join(extra_cols)}")
            return False, f"CSV file contains extra columns: {', '.join(extra_cols)}"

        missing_cols = set(Transaction.model_fields.keys()) - set(df.columns)
        if missing_cols:
            logger.error(f"CSV file is missing columns: {', '.join(missing_cols)}")
            return False, f"CSV file is missing columns: {', '.join(missing_cols)}"

        for index, row in df.iterrows():
            try:
                _ = Transaction(**row.to_dict())
            except Exception as e:
                logger.error(f"Row {index + 1}: {e}")
                raise ValueError(f"Row {index + 1}: {e}")
        
        return df, True, None
    
    except ValueError as ve:
        logger.error(str(ve))
        return df, False, str(ve)
    except Exception as e:
        logger.error(f"Unexpected Error: {str(e)}")
        return df, False, f"Unexpected Error: {str(e)}"


def df_to_sql(df):
    """
    Converts a DataFrame to a SQL table.

    Args:
        df (DataFrame): The DataFrame to be converted.

    Returns:
        tuple: A tuple containing two elements:
            - A boolean indicating whether the conversion was successful (True) or not (False).
            - If the conversion failed, a string describing the error encountered. If successful, None.

    Notes:
        This function converts the provided DataFrame to a SQL table named "transactions".
        It replaces any existing table with the same name if it exists.

    Raises:
        Any exceptions raised during the conversion process.
    """
    try:
        df.to_sql(name="transactions", con=DATABASE_URL, if_exists="replace", index=False)
        logger.info("DataFrame converted to SQL table successfully.")
        return True, None
    except Exception as e:
        logger.error(f"Failed to convert DataFrame to SQL table: {str(e)}")
        return False, str(e)
    

def csv_to_parquet(csv_path: str) -> str:
    """
    Transforms a CSV file into a Parquet file using DuckDB.

    Args:
        csv_path (str): The path to the CSV file to be converted.

    Returns:
        str: The path to the generated Parquet file.

    Notes:
        This function uses DuckDB to read the CSV file and convert it into a Parquet file.
        The returned path points to the location of the generated Parquet file.

    Raises:
        Any exceptions raised during the conversion process.
    """
    try:
        parquet_file = db.read_csv(csv_path).to_parquet()
        logger.info(f"CSV file converted to Parquet: {parquet_file}")
        return parquet_file
    except Exception as e:
        logger.error(f"Failed to convert CSV to Parquet: {str(e)}")
        raise e


def save_parquet_to_aws(parquet_file: str, bucket_name: str, bucket_path: str):
    """
    Saves a Parquet file to an Amazon S3 bucket.

    Args:
        parquet_file (str): The local path to the Parquet file to be uploaded.
        bucket_name (str): The name of the S3 bucket where the file will be uploaded.
        bucket_path (str): The key (path) under which the file will be stored in the S3 bucket.

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified Parquet file does not exist.
        Exception: If any other error occurs during the upload process.
    """
    s3 = boto3.client('s3', 
                  aws_access_key_id=AWS_ACCESS_KEY, 
                  aws_secret_access_key=AWS_SECRET)

    try:
        s3.upload_file(parquet_file, bucket_name, bucket_path)
        logger.info(f"File {parquet_file} successfully sent to bucket {bucket_name}.")
    except FileNotFoundError:
        logger.error(f"File {parquet_file} not found.")
    except Exception as e:
        logger.error(f"An error occurred while sending the file to S3: {e}")

