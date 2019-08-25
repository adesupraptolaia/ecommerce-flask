import pytest, json, logging
from flask import Flask, request, json
from blueprints import app
from app import cache

def call_client(request):
    client = app.test_client()
    return client

@pytest.fixture
def client(request):
    return call_client(request)

def create_token_non_internal():
    token = cache.get('token-non-internal')
    if token is None:
        ## prepare request input
        data = {
            'username': 'tes',
            'password': 'tes'
        }

        ## do request
        req = call_client(request)
        res = req.post('/token', data=json.dumps(data), content_type='application/json') # seperti nembak API luar (contoh weather.io)

        ## store response
        res_json = json.loads(res.data)

        logging.warning('RESULT : %s', res_json)

        ## assert / compare with expected result
        assert res.status_code == 200

        ## save token into cache
        cache.set('token-non-internal', res_json['token'], timeout=60)

        ## return because it useful for other test
        return res_json['token']
    else:
        return token


def create_token_internal():
    token = cache.get('token-internal')
    if token is None:
        ## prepare request input
        data = {
            'username': 'tes',
            'password': 'tes',
            'email' : 'tes@tes.com'
        }

        ## do request
        req = call_client(request)
        res = req.post('/token/admin', data=json.dumps(data), content_type='application/json') # seperti nembak API luar (contoh weather.io)

        ## store response
        res_json = json.loads(res.data)

        logging.warning('RESULT : %s', res_json)

        ## assert / compare with expected result
        assert res.status_code == 200

        ## save token into cache
        cache.set('token-internal', res_json['token'], timeout=60)

        ## return because it useful for other test
        return res_json['token']
    else:
        return token
        
            