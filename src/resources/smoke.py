from flask_restful import Resource


class Smoke(Resource):
    """Smoke"""

    def get(self):
        return {"message": "OK"}, 200
