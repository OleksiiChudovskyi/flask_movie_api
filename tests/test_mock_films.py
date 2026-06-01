import http
import json
from dataclasses import dataclass
from unittest.mock import patch


@dataclass
class FakeFilm:
    title = 'Fake Film'
    distributed_by = 'Fake'
    release_date = '2002-12-03'
    description = 'Fake description'
    length = 100
    rating = 8.0


class TestFilmsMock:

    @patch('src.services.film_service.FilmService.fetch_all_films', autospec=True)
    def test_get_films_mock_db(self, mock_db_call, app_mock, api_ver):
        client = app_mock.test_client()
        resp = client.get(f'{api_ver}/films')
        mock_db_call.assert_called_once()
        assert resp.status_code == http.HTTPStatus.OK
        assert len(resp.json) == 0

    def test_create_film_with_mock_db(self, app_mock, api_ver):
        with patch('src.db.session.add', autospec=True) as mock_session_add, \
                patch('src.db.session.commit', autospec=True) as mock_session_commit:
            client = app_mock.test_client()
            data = {
                'title': 'Test Title',
                'distributed_by': 'Test Company',
                'release_date': '2010-04-01',
                'description': '',
                'length': 100,
                'rating': 8.0
            }
            resp = client.post(f'{api_ver}/films', data=json.dumps(data), content_type='application/json')
            mock_session_add.assert_called_once()
            mock_session_commit.assert_called_once()

    def test_update_film_with_mock_db(self, app_mock, api_ver):
        with patch('src.services.film_service.FilmService.fetch_film_by_uuid') as mocked_query, \
                patch('src.db.session.add', autospec=True) as mock_session_add, \
                patch('src.db.session.commit', autospec=True) as mock_session_commit:
            mocked_query.return_value = FakeFilm()
            client = app_mock.test_client()
            url = f'{api_ver}/films/1'
            data = {
                'title': 'Update Title',
                'distributed_by': 'update',
                'release_date': '2010-04-01'
            }
            resp = client.put(url, data=json.dumps(data), content_type='application/json')
            mock_session_add.assert_called_once()
            mock_session_commit.assert_called_once()
