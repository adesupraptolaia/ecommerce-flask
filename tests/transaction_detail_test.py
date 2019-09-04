import json
from . import app, client, cache, create_token_non_internal, create_token_internal, reset_database

class TestTransactionCrud():

    reset_database()

    id = 0

# post product to cart first
    def test_client_post_cart_valid(self, client):
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

    def test_client_post_transaction_valid(self, client):
        token = create_token_non_internal()
        res = client.post('/transaction',
                        headers={'Authorization': 'Bearer ' + token},
                        content_type='application/json')
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

######### client get id
    def test_client_get_id_valid(self, client):
        token = create_token_non_internal()
        res = client.get('/transactiondetail/1',
                        headers={'Authorization': 'Bearer ' + token}, 
                        content_type='application/json')
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

    def test_client_get_id_valid_1(self, client):
        token = create_token_non_internal()
        res = client.get('/transactiondetail?product_id=1&transaction_id=1',
                        headers={'Authorization': 'Bearer ' + token}, 
                        content_type='application/json')
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

    
    def test_client_get_id_invalid(self, client):
        token = create_token_non_internal()
        res = client.get('/transactiondetail/-100',
                        headers={'Authorization': 'Bearer ' + token}, 
                        content_type='application/json')
        
        res_json=json.loads(res.data)
        assert res.status_code == 404

######### admin get id
    def test_admin_get_id_valid(self, client):
        token = create_token_internal()
        res = client.get('/transactiondetail/admin/1',
                        headers={'Authorization': 'Bearer ' + token}, 
                        content_type='application/json')
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

    def test_admin_get_id_valid_1(self, client):
        token = create_token_internal()
        res = client.get('/transactiondetail/admin?product_id=1&transaction_id=1',
                        headers={'Authorization': 'Bearer ' + token}, 
                        content_type='application/json')
        
        res_json=json.loads(res.data)
        assert res.status_code == 200
    
    def test_admin_get_id_invalid(self, client):
        token = create_token_internal()
        res = client.get('/transactiondetail/admin/-100',
                        headers={'Authorization': 'Bearer ' + token}, 
                        content_type='application/json')
        
        res_json=json.loads(res.data)
        assert res.status_code == 404

######### admin get 
    def test_admin_get_valid(self, client):
        token = create_token_internal()
        res = client.get('/transactiondetail/admin',
                        headers={'Authorization': 'Bearer ' + token}, 
                        content_type='application/json')
        
        res_json=json.loads(res.data)
        assert res.status_code == 200
    
    def test_admin_get_invalid(self, client):
        token = create_token_non_internal()
        res = client.get('/transactiondetail/admin',
                        headers={'Authorization': 'Bearer ' + token}, 
                        content_type='application/json')
        
        res_json=json.loads(res.data)
        assert res.status_code == 403

################# options 
    def test_transaction_detail_options_valid(self, client):
        res = client.options('/transactiondetail')
        res_json=json.loads(res.data)     
        assert res.status_code == 200
    
    def test_transaction_detail_options_valid_1(self, client):
        res = client.options('/transactiondetail/1')
        res_json=json.loads(res.data)     
        assert res.status_code == 200

    def test_transaction_detail_options_valid_2(self, client):
        res = client.options('/transactiondetail/admin')
        res_json=json.loads(res.data)     
        assert res.status_code == 200

    def test_transaction_detail_options_valid_3(self, client):
        res = client.options('/transactiondetail/admin/1')
        res_json=json.loads(res.data)     
        assert res.status_code == 200

