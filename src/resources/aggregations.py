from flask_restful import Resource
from sqlalchemy import func

from src import db
from src.models import Film, Actor


class AggregationApi(Resource):
    """Endpoint for displaying aggregated statistics of films and actors.."""

    def get(self):
        # combine all about the movies in ONE entry to the database
        films_stats = db.session.query(
            func.count(Film.id),
            func.max(Film.rating),
            func.min(Film.rating),
            func.avg(Film.rating),
            func.sum(Film.rating)
        ).one()

        # optimizing actor support.
        actor_count = db.session.query(func.count(Actor.id)).scalar()
        count_isactive = db.session.query(func.count(Actor.id)).filter(Actor.is_active.is_(True)).scalar()
        count_nonactive = db.session.query(func.count(Actor.id)).filter(Actor.is_active.is_(False)).scalar()

        return {
            "result": {
                'films': {
                    'count': films_stats[0],
                    'max_rating': films_stats[1],
                    'min_rating': films_stats[2],
                    'avg_rating': float(films_stats[3]) if films_stats[3] else 0.0,
                    'sum_rating': films_stats[4]
                },
                'actors': {
                    'count': actor_count,
                    'count_isactive': count_isactive,
                    'count_nonactive': count_nonactive
                }
            }
        }, 200
