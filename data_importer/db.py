import psycopg2
import yaml
import os
from typing import List
from .models import Phone
from .logger import setup_logger
import json

logger = setup_logger()

class DatabaseClient:
    def __init__(self):
        with open('config/config.yaml', 'r') as f:
            config = yaml.safe_load(f)
        
        db_config = config['database']
        # Get password from environment variable
        db_password = os.getenv('DB_PASSWORD', db_config['password'])
        
        self.conn_params = {
            'host': db_config['host'],
            'port': db_config['port'],
            'database': db_config['database'],
            'user': db_config['user'],
            'password': db_password
        }
    
    def create_table(self):
        """Create the phone table if it doesn't exist"""
        create_table_query = """
        CREATE TABLE IF NOT EXISTS public.phone (
            phoneid text NOT NULL,
            phone_name text NULL,
            phone_data jsonb NULL,
            CONSTRAINT phone_pkey PRIMARY KEY (phoneid)
        );
        """
        
        with psycopg2.connect(**self.conn_params) as conn:
            with conn.cursor() as cur:
                cur.execute(create_table_query)
                logger.info("Table created or already exists")
    
    def drop_table(self):
        """Drop the phone table if it exists"""
        drop_table_query = """
        DROP TABLE IF EXISTS public.phone;
        """
        
        with psycopg2.connect(**self.conn_params) as conn:
            with conn.cursor() as cur:
                cur.execute(drop_table_query)
                logger.info("Table dropped if existed")
    
    def insert_phones(self, phones: List[Phone]):
        """Insert phone data into the database"""
        insert_query = """
        INSERT INTO public.phone (phoneid, phone_name, phone_data)
        VALUES (%s, %s, %s)
        ON CONFLICT (phoneid) DO UPDATE
        SET phone_name = EXCLUDED.phone_name,
            phone_data = EXCLUDED.phone_data;
        """
        
        with psycopg2.connect(**self.conn_params) as conn:
            with conn.cursor() as cur:
                for phone in phones:
                    try:
                        cur.execute(
                            insert_query,
                            (
                                phone.phoneid,
                                phone.phone_name,
                                json.dumps(phone.phone_data)
                            )
                        )
                        logger.info(f"Inserted/Updated phone with ID: {phone.phoneid}")
                    except Exception as e:
                        logger.error(f"Error inserting phone {phone.phoneid}: {str(e)}")
                        conn.rollback()
                        raise
                
                conn.commit()
                logger.info(f"Successfully inserted {len(phones)} phones")
