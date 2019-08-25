import json
from . import app, client, cache, create_token_non_internal, create_token_internal
class TestClientDetailCrud():

    client_id = 0

######### client detail get
    # def test_client_get_valid(self, client):
    #     token = create_token_non_internal()
    #     res = client.get('/client/detail',
    #                     headers={'Authorization': 'Bearer ' + token}, 
    #                     content_type='application/json')
        
    #     res_json=json.loads(res.data)
    #     assert res.status_code == 200
    
    # def test_client_get_invalid(self, client):
    #     token = create_token_internal()
    #     res = client.get('/client/detail',
    #                     headers={'Authorization': 'Bearer ' + token}, 
    #                     content_type='application/json')
        
    #     res_json=json.loads(res.data)
    #     assert res.status_code == 403


# ######## client detail post & put valid

    def test_client_post_invalid(self, client):
        token =  create_token_non_internal()
        data = {
            "fullname": "tes1",
            "phone": "1234",
            "address": "tes1"
        }
        res=client.post('/client/detail', headers={'Authorization': 'Bearer ' + token}, 
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 200

#     def test_client_put_valid_1(self, client):
#         token = create_token_non_internal()
#         data = {
#             "fullname": "tes",
#             "phone": "1234",
#             "address": "tes"
#         }
#         res=client.put('/client/detail', headers={'Authorization': 'Bearer ' + token},
#                         data=json.dumps(data),
#                         content_type='application/json')

#         res_json=json.loads(res.data)

#         assert res.status_code == 200

# # ############## client detail put / edit

#     def test_client_put_valid(self, client):
#         token = create_token_non_internal()
#         data = {
#             "fullname": "tes1",
#             "phone": "1234",
#             "address": "tes1"
#         }
#         res=client.put('/client/detail', headers={'Authorization': 'Bearer ' + token},
#                         data=json.dumps(data),
#                         content_type='application/json')

#         res_json=json.loads(res.data)

#         assert res.status_code == 200

#     def test_client_put_valid_1(self, client):
#         token = create_token_non_internal()
#         data = {
#             "fullname": "tes",
#             "phone": "1234",
#             "address": "tes"
#         }
#         res=client.put('/client/detail', headers={'Authorization': 'Bearer ' + token},
#                         data=json.dumps(data),
#                         content_type='application/json')

#         res_json=json.loads(res.data)

#         assert res.status_code == 200
