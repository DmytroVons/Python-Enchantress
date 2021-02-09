from freezegun import freeze_time
from Amazon_killer import amazon_killer as app
import pytest


@pytest.fixture
def store_app():
    app.config['TESTING'] = True
    with app.test_client() as client:
        return client


@freeze_time('2021-02-08 14:16:41')
def test_create_user(store_app):
    response = store_app.post(
        '/users',
        json={
            "name": "Illia",
	    "email": "illia.sukonnik@gmail.com",
	})
    assert response.status_code == 201
    assert response.json == {
        "user_id": 1,
	"registration_timestamp": '2021-02-08T14:16:41'
    }
