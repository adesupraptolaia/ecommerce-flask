import json
from . import app, client, cache, create_token_non_internal, create_token_internal
class TestWishlistCrud():

    id = 0

######### client get
    def test_client_get_valid(self, client):
        token = create_token_non_internal()
        res = client.get('/wishlist',
                        headers={'Authorization': 'Bearer ' + token}, 
                        content_type='application/json')
        
        res_json=json.loads(res.data)
        assert res.status_code == 200
    
    def test_client_get_invalid(self, client):
        token = create_token_internal()
        res = client.get('/wishlist',
                        headers={'Authorization': 'Bearer ' + token}, 
                        content_type='application/json')
        
        res_json=json.loads(res.data)
        assert res.status_code == 403


# ############### client post and delete valid

    def test_client_post_valid(self, client):
        token = create_token_non_internal()
        data = {
            "product_id": "5",
        }
        res=client.post('/wishlist',
                        data=json.dumps(data),
                        headers={'Authorization': 'Bearer ' + token},
                        content_type='application/json')

        res_json=json.loads(res.data)

        TestWishlistCrud.id = res_json['id']

        assert res.status_code == 200

    def test_client_delete_valid(self, client):
        token = create_token_non_internal()
        
        res=client.delete(f'/wishlist/{TestWishlistCrud.id}', headers={'Authorization': 'Bearer ' + token},
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 200



# ############### client post and delete valid

    def test_client_post_invalid(self, client):
        token = create_token_non_internal()
        data = {
            "qty": "1"
        }
        res=client.post('/wishlist',
                        data=json.dumps(data),
                        headers={'Authorization': 'Bearer ' + token},
                        content_type='application/json')

        res_json=json.loads(res.data)


        assert res.status_code == 400

    def test_client_delete_invalid(self, client):
        token = create_token_non_internal()
        
        res=client.delete("/wishlist/-100", headers={'Authorization': 'Bearer ' + token},
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 404

