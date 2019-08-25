import json
from . import app, client, cache, create_token_non_internal, create_token_internal
class TestTransactionCrud():

    id = 0

######### client get id
    def test_client_get_id_valid(self, client):
        token = create_token_non_internal()
        res = client.get('/transaction/1',
                        headers={'Authorization': 'Bearer ' + token}, 
                        content_type='application/json')
        
        res_json=json.loads(res.data)
        assert res.status_code == 200
    
    def test_client_get_id_invalid(self, client):
        token = create_token_internal()
        res = client.get('/transaction/1',
                        headers={'Authorization': 'Bearer ' + token}, 
                        content_type='application/json')
        
        res_json=json.loads(res.data)
        assert res.status_code == 403


######### client get
    def test_client_get_valid(self, client):
        token = create_token_non_internal()
        res = client.get('/transaction',
                        headers={'Authorization': 'Bearer ' + token}, 
                        content_type='application/json')
        
        res_json=json.loads(res.data)
        assert res.status_code == 200
    
    def test_client_get_invalid(self, client):
        token = create_token_internal()
        res = client.get('/transaction',
                        headers={'Authorization': 'Bearer ' + token}, 
                        content_type='application/json')
        
        res_json=json.loads(res.data)
        assert res.status_code == 403


######### admin get 
    def test_admin_get_valid(self, client):
        token = create_token_internal()
        res = client.get('/transaction/admin',
                        headers={'Authorization': 'Bearer ' + token}, 
                        content_type='application/json')
        
        res_json=json.loads(res.data)
        assert res.status_code == 200
    
    def test_admin_get_invalid(self, client):
        token = create_token_non_internal()
        res = client.get('/transaction/admin',
                        headers={'Authorization': 'Bearer ' + token}, 
                        content_type='application/json')
        
        res_json=json.loads(res.data)
        assert res.status_code == 403

