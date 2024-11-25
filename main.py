from data_importer.api_client import APIClient
from data_importer.db import DatabaseClient
from data_importer.logger import setup_logger

def main():
    logger = setup_logger()
    logger.info("Starting data import process")
    
    try:
        # Initialize clients
        api_client = APIClient()
        db_client = DatabaseClient()
        
        # Drop and recreate table
        db_client.drop_table()
        db_client.create_table()
        
        # Fetch phones from API
        phones = api_client.get_phones()
        
        # Insert phones into database
        db_client.insert_phones(phones)
        
        logger.info("Data import process completed successfully")
        
    except Exception as e:
        logger.error(f"Error during data import: {str(e)}")
        raise

if __name__ == "__main__":
    main()
