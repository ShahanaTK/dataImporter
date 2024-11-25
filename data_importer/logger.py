import logging
import os
import yaml

def setup_logger():
    # Create logs directory if it doesn't exist
    os.makedirs('logs', exist_ok=True)
    
    # Load config
    with open('config/config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    
    logging_config = config['logging']
    
    # Configure logging
    logging.basicConfig(
        level=logging_config['level'],
        format=logging_config['format'],
        handlers=[
            logging.FileHandler(logging_config['file']),
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger(__name__)
