import datetime

from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from sqlalchemy.orm import selectinload

from src import db
from src.models import Actor
from src.schemas import ActorSchema
from src.services import ActorService


class ActorListApi(Resource):
    """"""

    actor_schema = ActorSchema()

    def get(self, uuid=None):
        if not uuid:
            actors = ActorService.fetch_all_actors(db.session) \
                .options(selectinload(Actor.films)) \
                .all()
            return self.actor_schema.dump(actors, many=True), 200
        actor = ActorService.fetch_actor_by_uuid(db.session, uuid)
        if not actor:
            return "", 404
        return self.actor_schema.dump(actor), 200

    def post(self):
        try:
            actor = self.actor_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {"message": str(e)}, 400
        db.session.add(actor)
        db.session.commit()
        return self.actor_schema.dump(actor), 201

    def put(self, uuid):
        actor = ActorService.fetch_actor_by_uuid(db.session, uuid)
        if not actor:
            return "", 400
        try:
            actor = self.actor_schema.load(request.json, instance=actor, session=db.session)
        except ValidationError as e:
            return {"message": str(e)}, 400
        db.session.add(actor)
        db.session.commit()
        return self.actor_schema.dump(actor), 200

    def patch(self, uuid):
        actor = ActorService.fetch_actor_by_uuid(db.session, uuid)
        if not actor:
            return "", 404

        actor_json = request.json
        name = actor_json.get("name")
        birthday = datetime.datetime.strptime(actor_json.get('birthday'), '%B %d, %Y') if actor_json.get(
            'birthday') else None
        is_active = actor_json.get("is_active")

        if name:
            actor.name = name
        elif birthday:
            actor.birthday = birthday
        elif is_active:
            actor.is_active = is_active

        db.session.add(actor)
        db.session.commit()
        return self.actor_schema.dump(actor), 200

    def delete(self, uuid):
        actor = ActorService.fetch_actor_by_uuid(db.session, uuid)
        if not actor:
            return "", 404
        db.session.delete(actor)
        db.session.commit()
        return '', 204
