import http
import json


class TestActors:
    uuid = []

    def test_get_actors_with_db(self, app_dev, api_ver):
        client = app_dev.test_client()
        resp = client.get(f'{api_ver}/actors')
        assert resp.status_code == http.HTTPStatus.OK

    def test_create_actor_with_db(self, app_dev, api_ver):
        client = app_dev.test_client()
        data = {
            'name': 'Test Actor',
            'birthday': '2010-04-01',
            'is_active': False
        }
        resp = client.post(f'{api_ver}/actors', data=json.dumps(data), content_type='application/json')
        assert resp.status_code == http.HTTPStatus.CREATED
        assert resp.json['name'] == 'Test Actor'
        self.uuid.append(resp.json['uuid'])

    def test_update_actor_with_db(self, app_dev, api_ver):
        client = app_dev.test_client()
        url = f'{api_ver}/actors/{self.uuid[0]}'
        data = {
            'name': 'Update Name',
            'birthday': '2010-04-01',
            'is_active': False
        }
        resp = client.put(url, data=json.dumps(data), content_type='application/json')
        assert resp.status_code == http.HTTPStatus.OK
        assert resp.json['name'] == 'Update Name'

    def test_delete_actor_with_db(self, app_dev, api_ver):
        client = app_dev.test_client()
        url = f'{api_ver}/actors/{self.uuid[0]}'
        resp = client.delete(url)
        assert resp.status_code == http.HTTPStatus.NO_CONTENT
