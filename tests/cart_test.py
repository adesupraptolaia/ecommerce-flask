import json
from . import app, client, cache, create_token_non_internal, create_token_internal
class TestCardCrud():

    cart_id = 0

######### client get
    def test_client_get_valid(self, client):
        token = create_token_non_internal()
        res = client.get('/cart',
                        headers={'Authorization': 'Bearer ' + token}, 
                        content_type='application/json')
        
        res_json=json.loads(res.data)
        assert res.status_code == 200
    
    def test_client_get_invalid(self, client):
        token = create_token_internal()
        res = client.get('/cart',
                        headers={'Authorization': 'Bearer ' + token}, 
                        content_type='application/json')
        
        res_json=json.loads(res.data)
        assert res.status_code == 403


# ############### client post and delete valid

    def test_client_post_valid(self, client):
        token = create_token_non_internal()
        data = {
            "product_id": "5",
            "qty": "1"
        }
        res=client.post('/cart',
                        data=json.dumps(data),
                        headers={'Authorization': 'Bearer ' + token},
                        content_type='application/json')

        res_json=json.loads(res.data)

        TestCardCrud.cart_id = res_json['cart_id']

        assert res.status_code == 200

    def test_client_delete_valid(self, client):
        token = create_token_non_internal()
        
        res=client.delete(f'/cart/{TestCardCrud.cart_id}', headers={'Authorization': 'Bearer ' + token},
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 200



# ############### client post and delete valid

    def test_client_post_invalid(self, client):
        token = create_token_non_internal()
        data = {
            "qty": "1"
        }
        res=client.post('/cart',
                        data=json.dumps(data),
                        headers={'Authorization': 'Bearer ' + token},
                        content_type='application/json')

        res_json=json.loads(res.data)


        assert res.status_code == 400

    def test_client_delete_invalid(self, client):
        token = create_token_non_internal()
        
        res=client.delete("/cart/-100", headers={'Authorization': 'Bearer ' + token},
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 404

