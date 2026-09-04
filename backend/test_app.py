import pytest
from app import app

from app import app

def test_add_product():
    client = app.test_client()
    
    producto = {
        'id': 1,
        'name': 'Teclado',
        'price': 20.0,
        'quantity': 2
    }
    
    response = client.post('/api/products', json=producto)
    
    assert response.status_code == 201
    assert response.get_json() == producto