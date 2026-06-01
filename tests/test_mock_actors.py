import http
import json
from dataclasses import dataclass
from unittest.mock import patch


@dataclass
class FakeActor:
    name = 'Fake Actor'
    birthday = '2002-12-03'
    is_active = False


class TestActorsMock:

    @patch('src.services.actor_service.ActorService.fetch_all_actors', autospec=True)
    def test_get_actors_mock_db(self, mock_db_call, app_mock, api_ver):
        client = app_mock.test_client()
        resp = client.get(f'{api_ver}/actors')
        mock_db_call.assert_called_once()
        assert resp.status_code == http.HTTPStatus.OK
        assert len(resp.json) == 0

    def test_create_actor_with_mock_db(self, app_mock, api_ver):
        with patch('src.db.session.add', autospec=True) as mock_session_add, \
                patch('src.db.session.commit', autospec=True) as mock_session_commit:
            client = app_mock.test_client()
            data = {
                'name': 'Test Actor',
                'birthday': '2010-04-01',
                'is_active': False
            }
            resp = client.post(f'{api_ver}/actors', data=json.dumps(data), content_type='application/json')
            mock_session_add.assert_called_once()
            mock_session_commit.assert_called_once()

    def test_update_actor_with_mock_db(self, app_mock, api_ver):
        with patch('src.services.actor_service.ActorService.fetch_actor_by_uuid') as mocked_query, \
                patch('src.db.session.add', autospec=True) as mock_session_add, \
                patch('src.db.session.commit', autospec=True) as mock_session_commit:
            mocked_query.return_value = FakeActor()
            client = app_mock.test_client()
            url = f'{api_ver}/actors/1'
            data = {
                'name': 'Update Name',
                'birthday': '2010-04-01',
                'is_active': False
            }
            resp = client.put(url, data=json.dumps(data), content_type='application/json')
            mock_session_add.assert_called_once()
            mock_session_commit.assert_called_once()
