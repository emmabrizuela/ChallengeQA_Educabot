import requests

def test_departments_api():
    url = "https://www.mercadolibre.com.ar/menu/departments"
    response = requests.get(url)
    assert response.status_code == 200
    assert "departments" in response.text
