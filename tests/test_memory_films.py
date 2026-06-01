import http
import json


class TestFilmsInMemory:
    uuid = []

    def test_get_films_with_db(self, app_memory, api_ver):
        client = app_memory.test_client()
        resp = client.get(f'{api_ver}/films')
        assert resp.status_code == http.HTTPStatus.OK

    def test_create_film_with_db(self, app_memory, api_ver):
        client = app_memory.test_client()
        data = {
            'title': 'Test Title',
            'distributed_by': 'Test Company',
            'release_date': '2010-04-01',
            'description': '',
            'length': 100,
            'rating': 8.0
        }
        resp = client.post(f'{api_ver}/films', data=json.dumps(data), content_type='application/json')
        assert resp.status_code == http.HTTPStatus.CREATED
        assert resp.json['title'] == 'Test Title'
        self.uuid.append(resp.json['uuid'])

    def test_update_film_with_db(self, app_memory, api_ver):
        client = app_memory.test_client()
        url = f'{api_ver}/films/{self.uuid[0]}'
        data = {
            'title': 'Update Title',
            'distributed_by': 'update',
            'release_date': '2010-04-01'
        }
        resp = client.put(url, data=json.dumps(data), content_type='application/json')
        assert resp.status_code == http.HTTPStatus.OK
        assert resp.json['title'] == 'Update Title'

    def test_delete_film_with_db(self, app_memory, api_ver):
        client = app_memory.test_client()
        url = f'{api_ver}/films/{self.uuid[0]}'
        resp = client.delete(url)
        assert resp.status_code == http.HTTPStatus.NO_CONTENT
