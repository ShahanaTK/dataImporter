import requests
import yaml
from typing import List, Dict, Any
from .logger import setup_logger
from .models import Phone

logger = setup_logger()

class APIClient:
    def __init__(self):
        with open('config/config.yaml', 'r') as f:
            config = yaml.safe_load(f)
        
        self.base_url = config['api']['base_url']
        self.endpoint = config['api']['endpoint']
    
    def get_phones(self) -> List[Phone]:
        """
        Fetch phone data from the API
        """
        url = f"{self.base_url}{self.endpoint}"
        logger.info(f"Fetching data from {url}")
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            phones = [Phone.from_api_response(item) for item in data]
            logger.info(f"Successfully fetched {len(phones)} phones")
            return phones
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching data from API: {str(e)}")
            raise
