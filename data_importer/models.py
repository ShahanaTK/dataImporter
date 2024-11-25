from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class Phone:
    phoneid: str
    phone_name: str
    phone_data: Dict[str, Any]

    @classmethod
    def from_api_response(cls, response_item: Dict[str, Any]) -> 'Phone':
        return cls(
            phoneid=response_item['id'],
            phone_name=response_item['name'],
            phone_data=response_item.get('data', {})
        )
