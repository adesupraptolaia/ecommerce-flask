import json
from . import app, client, cache, create_token_non_internal, create_token_internal

class TestAdminCrud():

    id = 0

######### admin get
    def test_admin_get_valid(self, client):
        token = create_token_internal()
        res = client.get('/admin',
                        headers={'Authorization': 'Bearer ' + token}, content_type='application/json')
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

    def test_admin_get_invalid(self, client):
        token = create_token_non_internal()
        res = client.get('/admin',
                        headers={'Authorization': 'Bearer ' + token}, content_type='application/json')
        
        res_json=json.loads(res.data)
        assert res.status_code == 403


# ################### admin put /edit

    def test_admin_edit_valid(self, client):
        token = create_token_internal()
        data = {
            'username': 'tes1',
            'password': 'tes1',
            'email' : 'tes@tes.com'
        }
        res=client.put('/admin', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data), 
                        content_type='application/json')

        res_json=json.loads(res.data)

        # TestBookCrud.id = res_json['id']
        assert res.status_code == 200

    def test_admin_edit_valid_2(self, client):
        token = create_token_internal()
        data = {
            'username': 'tes',
            'password': 'tes',
            'email' : 'tes@tes.com'
        }
        res=client.put('/admin', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data), 
                        content_type='application/json')

        res_json=json.loads(res.data)

        # TestBookCrud.id = res_json['id']
        assert res.status_code == 200

    def test_admin_edit_invalid(self, client):
        token = create_token_internal()
        data = {
            'username': 'tes',
            'password': 'tes'
        }
        res=client.put('/admin', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data), 
                        content_type='application/json')

        res_json=json.loads(res.data)

        # TestBookCrud.id = res_json['id']
        assert res.status_code == 400

# 