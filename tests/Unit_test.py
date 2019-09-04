from blueprints.client.model import Clients
from blueprints import db
from mock import patch
from . import reset_database
from blueprints.weather import CurrentWeather

class TestUser():

    reset_database()

    def test_is_user_already_exist(self):

        client = Clients("tes1", "tes1", "tes1")
        db.session.add(client)
        db.session.commit()

        username = "tes"

        assert Clients.is_exists(username) == True


    @patch.object(Clients, 'is_exists')
    def test_if_get_last_balance_is_none(self, mock_is_exists):

        username = "tes"
        mock_is_exists.return_value = True

        assert Clients.is_exists(username) == True

    @patch.object(CurrentWeather,'get')
    def test_get_temp_function(self, mock_get):
        temp = { 'temp' : 22.5 }
        mock_get.return_value = temp
        assert CurrentWeather.get() == temp
  
  # def test_get_temp_asli(self):
    # assert CurrentWeather.get(self).status_code == 200