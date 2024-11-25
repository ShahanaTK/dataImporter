# Data Importer Module

This module retrieves mobile phone data from a REST API and stores it in a PostgreSQL database.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure the database:
- Create a PostgreSQL database named `phone_db`
- Set the environment variable `DB_PASSWORD` with your PostgreSQL password:
```bash
# On Windows
set DB_PASSWORD=your_password
# On Unix/Linux
export DB_PASSWORD=your_password
```

4. Run the application:
```bash
python main.py
```

## Project Structure

- `config/`: Configuration files
  - `config.yaml`: Contains database and API configurations
- `data_importer/`: Main module
  - `api_client.py`: Handles API requests
  - `db.py`: Database operations
  - `logger.py`: Logging configuration
  - `models.py`: Data models
- `tests/`: Test files
  - `test_api_client.py`: API client tests

## Features

- Fetches mobile phone data from REST API
- Stores data in PostgreSQL with JSONB support
- Handles dynamic data structure
- Includes logging and error handling
- Includes basic unit tests

## Database Schema

```sql
CREATE TABLE public.phone (
    phoneid text NOT NULL,
    phone_name text NULL,
    phone_data jsonb NULL,
    CONSTRAINT api_objects_pkey PRIMARY KEY (phoneid)
);
```
