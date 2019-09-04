import json
from . import app, client, cache, create_token_non_internal, create_token_internal, reset_database

class TestTransactionCrud():
    reset_database()
    id = 0

######### Post
    # post product to cart first
    def test_client_post_valid(self, client):
        token = create_token_non_internal()
        data = {
            "product_id": "1",
            "qty": "1"
        }
        res=client.post('/cart',
                        data=json.dumps(data),
                        headers={'Authorization': 'Bearer ' + token},
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 200

    def test_client_post_valid(self, client):
        token = create_token_non_internal()
        res = client.post('/transaction',
                        headers={'Authorization': 'Bearer ' + token},
                        content_type='application/json')
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

######### client get id
    def test_client_get_id_valid(self, client):
        token = create_token_non_internal()
        res = client.get('/transaction/1',
                        headers={'Authorization': 'Bearer ' + token}, 
                        content_type='application/json')
        
        res_json=json.loads(res.data)
        assert res.status_code == 200
    
    def test_client_get_id_invalid(self, client):
        token = create_token_non_internal()
        res = client.get('/transaction/1000',
                        headers={'Authorization': 'Bearer ' + token}, 
                        content_type='application/json')
        
        res_json=json.loads(res.data)
        assert res.status_code == 404


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
        res = client.get('/transaction/admin?client_id=1',
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

################# options 
    def test_transaction_detail_options_valid(self, client):
        res = client.options('/transaction')
        res_json=json.loads(res.data)     
        assert res.status_code == 200

    def test_transaction_detail_options_valid_1(self, client):
        res = client.options('/transaction/admin')
        res_json=json.loads(res.data)     
        assert res.status_code == 200

    def test_transaction_detail_options_valid_2(self, client):
        res = client.options('/transaction/1')
        res_json=json.loads(res.data)     
        assert res.status_code == 200