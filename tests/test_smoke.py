import http


def test_smoke(app_dev, api_ver):
    client = app_dev.test_client()
    resp = client.get(f"{api_ver}/smoke")
    assert resp.status_code == http.HTTPStatus.OK
