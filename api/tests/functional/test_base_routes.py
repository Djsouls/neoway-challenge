BASE_API = '/api/v1/'

def test_invalid_url_return_404(client):
    """Testa se uma URL inválida retorna erro 404"""
    assert client.get('/url/que/nao/existe').status_code == 404

def test_base_url_return_200(client):
    """Testa se a URL base retorna código 200"""
    assert client.get(BASE_API).status_code == 200

## TODO: Implement database agnostic testing
def test_status_route(client):
    """Testa se a rota de status retorna código 200"""
    """
    route = BASE_API + 'status'

    response = client.get(route)

    assert response.status_code == 200
    """