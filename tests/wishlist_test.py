import json
from . import app, client, cache, create_token_non_internal, create_token_internal, reset_database


class TestWishlistCrud():
    reset_database()
    id = 0

# ################### post wishlist

    def test_client_post_wishlist_valid(self, client):
        token = create_token_non_internal()
        data = {
            "product_id": "1",
        }
        res=client.post('/wishlist',
                        data=json.dumps(data),
                        headers={'Authorization': 'Bearer ' + token},
                        content_type='application/json')

        res_json=json.loads(res.data)

        TestWishlistCrud.id = res_json['id']

        assert res.status_code == 200

    def test_client_post_wishlist_valid_1(self, client):
        token = create_token_non_internal()
        data = {
            "product_id": "1",
        }
        res=client.post('/wishlist',
                        data=json.dumps(data),
                        headers={'Authorization': 'Bearer ' + token},
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 200

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

################# options 
    def test_wishlist_options_valid(self, client):
        res = client.options('/wishlist/1')
        res_json=json.loads(res.data)     
        assert res.status_code == 200

