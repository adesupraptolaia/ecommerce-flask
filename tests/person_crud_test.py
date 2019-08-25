import json
from . import app, client, cache, create_token

class TestPersonCrud():
    def test_person_list(self, client):
        token = create_token()
        res = client.get('/tes',
                        headers={'Authorization': 'Bearer ' + token})
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

    def test_person_invalid_token(self, client):
        res = client.get('/tes', 
                        headers={'Authorization': 'Bearer abc'})
        res_json=json.loads(res.data)
        assert res.status_code == 500

    def test_person_invalid_input_name(self, client):
        token = create_token()
        data = {
            'age' : 60,
            'sex' : 'Male'
        }
        res=client.post('/tes', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        assert res.status_code == 400