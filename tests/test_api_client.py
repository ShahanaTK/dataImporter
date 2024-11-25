import pytest
from data_importer.api_client import APIClient
from data_importer.models import Phone

def test_api_client_initialization():
    client = APIClient()
    assert client.base_url == "https://api.restful-api.dev"
    assert client.endpoint == "/objects"

def test_phone_model():
    test_data = {
        "id": "test123",
        "name": "Test Phone",
        "data": {
            "color": "Black",
            "capacity": "256GB"
        }
    }
    
    phone = Phone.from_api_response(test_data)
    assert phone.phoneid == "test123"
    assert phone.phone_name == "Test Phone"
    assert phone.phone_data["color"] == "Black"
    assert phone.phone_data["capacity"] == "256GB"
