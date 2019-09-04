import json
from . import app, client, cache, create_token_non_internal, create_token_internal, reset_database

class TestProductCrud():
    reset_database()
    product_id = 0

######### client get id
    def test_client_get_id_valid(self, client):
        res = client.get('/product/1', content_type='application/json')
        
        res_json=json.loads(res.data)
        assert res.status_code == 200
    
    def test_client_get_id_invalid(self, client):
        res = client.get('/product/100000', content_type='application/json')
        
        res_json=json.loads(res.data)
        assert res.status_code == 404

# # ######################## get all

    def test_client_get_all_valid(self, client):
        res=client.get('/product',
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 200

    def test_client_get_all_valid_1(self, client):
        res=client.get('/product?category=category',
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 200

# # ############### client post, put and delete valid

    def test_client_post_valid(self, client):
        token = create_token_internal()
        data = {
            "name": "tes",
            "description": "tes",
            "category": "tes",
            "image": "tes",
            "price": 1,
            "discount": 1,
            "stock": 1,
        }
        res=client.post('/product', 
                        data=json.dumps(data), headers={'Authorization': 'Bearer ' + token},
                        content_type='application/json')

        res_json=json.loads(res.data)

        TestProductCrud.product_id = res_json['id']

        assert res.status_code == 200

    def test_client_post_valid_1(self, client):
        token = create_token_internal()
        data = {
            "name": "tes",
            "description": "tes",
            "category": "tes",
            "image": "tes",
            "price": 1,
            "discount": 0,
            "stock": 1,
        }
        res=client.post('/product', 
                        data=json.dumps(data), headers={'Authorization': 'Bearer ' + token},
                        content_type='application/json')

        res_json=json.loads(res.data)
        assert res.status_code == 200

    def test_client_put_valid(self, client):
        token = create_token_internal()
        data = {
            "name": "tes1",
            "description": "tes1",
            "category": "tes1",
            "image": "tes1",
            "price": 1,
            "discount": 1,
            "stock": 1,
        }
        res=client.put(f'/product/{TestProductCrud.product_id}', 
                        data=json.dumps(data), headers={'Authorization': 'Bearer ' + token},
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 200

    def test_client_put_valid_2(self, client):
        token = create_token_internal()
        data = {
            "name": "tes1",
            "description": "tes1",
            "category": "tes1",
            "image": "tes1",
            "price": 1,
            "discount": 0,
            "stock": 1,
        }
        res=client.put(f'/product/{TestProductCrud.product_id}', 
                        data=json.dumps(data), headers={'Authorization': 'Bearer ' + token},
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 200

    def test_client_put_invalid_1(self, client):
        token = create_token_internal()
        data = {
            "name": "tes1",
            "description": "tes1",
            "category": "tes1",
            "image": "tes1",
            "price": 1,
            "discount": 0,
            "stock": 1,
        }
        res=client.put(f'/product/-100', 
                        data=json.dumps(data), headers={'Authorization': 'Bearer ' + token},
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 404
    

    def test_client_delete_valid(self, client):
        token = create_token_internal()
        
        res=client.delete(f'/product/{TestProductCrud.product_id}', headers={'Authorization': 'Bearer ' + token},
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 200

# # ############### client post and delete invalid

    def test_client_post_invalid(self, client):
        token = create_token_internal()
        data = {
            "name": "tes",
            "description": "tes",
            "category": "tes",
            "image": "tes",
            "price": "tes",
            "discount": "tes",
            "stock": "tes",
        }
        res=client.post('/product', 
                        data=json.dumps(data), headers={'Authorization': 'Bearer ' + token},
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 400

    def test_client_delete_invalid(self, client):
        token = create_token_internal()
        
        res=client.delete("/product/-1000000", headers={'Authorization': 'Bearer ' + token},
                        content_type='application/json')

        res_json=json.loads(res.data)


        assert res.status_code == 404

################# options 
    def test_product_options_valid(self, client):
        res = client.options('/product')
        res_json=json.loads(res.data)     
        assert res.status_code == 200

    def test_product_options_valid_1(self, client):
        res = client.options('/product/1')
        res_json=json.loads(res.data)     
        assert res.status_code == 200
