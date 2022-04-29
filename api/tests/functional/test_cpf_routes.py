BASE_API = '/api/v1/'

def test_all_cpfs_route_return_seeded_cpfs(client):
    """"Testa se a rota /cpfs retorna os valores cadastrados previamente"""
    route = BASE_API + 'cpfs'

    response = client.get(route)

    assert len(response.data) != 0
    assert response.status_code == 200