import json
from . import app, client, cache, create_token_non_internal, create_token_internal
class TestClientCrud():

    client_id = 0

######### client get
    def test_client_get_valid(self, client):
        token = create_token_non_internal()
        res = client.get('/client',
                        headers={'Authorization': 'Bearer ' + token}, 
                        content_type='application/json')
        
        res_json=json.loads(res.data)
        assert res.status_code == 200
    
    def test_client_get_invalid(self, client):
        token = create_token_internal()
        res = client.get('/client',
                        headers={'Authorization': 'Bearer ' + token}, 
                        content_type='application/json')
        
        res_json=json.loads(res.data)
        assert res.status_code == 403


# ############### client post

    def test_client_post_invalid(self, client):
        data = {
            "username": "tes1",
            "password": "tes1"
        }
        res=client.post('/client',
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 400

# ######################## client put / edit

    def test_client_put_valid(self, client):
        token = create_token_non_internal()
        data = {
            "username": "tes1",
            "password": "tes1",
            "email" : "tes1@tes1.com"
        }
        res=client.put('/client', headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 200

    def test_client_put_valid_2(self, client):
        token = create_token_non_internal()
        data = {
            "username": "tes",
            "password": "tes",
            "email" : "tes@tes.com"
        }
        res=client.put('/client', headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 200

    def test_client_put_invalid(self, client):
        token = create_token_non_internal()
        data = {
            "username": "tes1",
            "password": "tes1",
        }
        res=client.put('/client', headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 400
