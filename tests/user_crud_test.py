import json
from . import app, client, cache, create_token, create_token_internal

class TestUserCrud():

    id = 0

######### get list
    def test_user_list(self, client):
        token = create_token_internal()
        res = client.get('/user',
                        headers={'Authorization': 'Bearer ' + token})
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

    def test_user_invalid_list(self, client):
        token = create_token()
        res = client.get('/user', 
                        headers={'Authorization': 'Bearer ' + token})
        res_json=json.loads(res.data)
        assert res.status_code == 403

######### get
    def test_user_get(self, client):
        token = create_token_internal()
        res = client.get('/user/2',
                        headers={'Authorization': 'Bearer ' + token})
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

    def test_user_invalid_get(self, client):
        token = create_token_internal()
        res = client.get('/user/1', 
                        headers={'Authorization': 'Bearer ' + token})
        res_json=json.loads(res.data)
        assert res.status_code == 404

######### post

    def test_user_input(self, client):
        token = create_token_internal()
        data = {
        "name": "Siti",
        "age": 51,
        "sex": "female",
        "client_id": 4
        }
        res=client.post('/user', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)

        TestUserCrud.id = res_json['id']
        assert res.status_code == 200


    def test_user_invalid_input(self, client):
        token = create_token_internal()
        data = {
        "age": 51,
        "sex": "male",
        "client_id": 4
        }
        res=client.post('/user', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        assert res.status_code == 400

######### put

    def test_user_update(self, client):
        token = create_token_internal()
        data = {
        "name": "Andy",
        "age": 51,
        "sex": "male",
        "client_id": 4
        }
        res=client.put('/user/3', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        assert res.status_code == 200
    
    def test_user_invalid_update(self, client):
        token = create_token_internal()
        data = {
        "age": 51,
        "sex": "male",
        "client_id": 4
        }
        res=client.put('/user/2', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        assert res.status_code == 400

######### delete
    def test_user_delete(self, client):
        token = create_token_internal()
        res=client.delete(f'/user/{TestUserCrud.id}', 
                        headers={'Authorization': 'Bearer ' + token})

        assert res.status_code == 200

    def test_user_invalid_delete(self, client):
        token = create_token_internal()
        res=client.delete(f'/user/1', 
                        headers={'Authorization': 'Bearer ' + token})

        assert res.status_code == 404

        