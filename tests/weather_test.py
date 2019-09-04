import json
from . import app, client, cache, create_token_non_internal, create_token_internal, reset_database


class TestWeatherCrud():
    reset_database()

# ################### post wishlist

    def test_client_get_weather_valid(self, client):
        res=client.get('/weather',
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 200

  
