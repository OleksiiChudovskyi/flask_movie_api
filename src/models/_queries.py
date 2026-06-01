from sqlalchemy import and_
from flask import current_app

from src import db
from src import models


def queries_select():
    """
    SELECT QUERIES
    """

    # all
    films1 = db.session.query(models.Film).all()
    print(type(films1))
    print(films1)

    # order_by
    films2 = db.session.query(models.Film).order_by(models.Film.rating).all()  # asc
    # films22 = db.session.query(models.Film).order_by(models.Film.rating.asc()).all()  # asc
    # films23 = db.session.query(models.Film).order_by(models.Film.rating.desc()).all()  # desc
    print("\n", type(films2))
    print(films2)

    # filter = uses for more complex queries
    # filter_by = uses for common, simple queries
    harry_potter_and_ch_s = db.session.query(models.Film).filter(
        models.Film.title == "Harry Potter and Chamber of Secrets"
    ).first()
    print("\n", type(harry_potter_and_ch_s))
    print(harry_potter_and_ch_s)

    harry_potter_and_priz_az = db.session.query(models.Film).filter_by(
        title="Harry Potter and the Prizoner of Azkaban"
    ).first()
    print(type(harry_potter_and_priz_az))
    print(harry_potter_and_priz_az)
    print("\n")

    # and statment, way 1
    and_statment_harry_potter_1 = db.session.query(models.Film).filter(
        models.Film.title != "Harry Potter and the Half-Blood Prince",
        models.Film.rating >= 7.5
    ).first()
    and_statment_harry_potter_11 = db.session.query(models.Film).filter(
        models.Film.title != "Harry Potter and the Half-Blood Prince",
        models.Film.rating >= 7.5
    )[:2]  # [:3] = the first three values from the list
    and_statment_harry_potter_2 = db.session.query(models.Film).filter(
        models.Film.title != "Harry Potter and the Half-Blood Prince",
        models.Film.rating >= 7.5
    ).all()
    print("The first value from the list = ", and_statment_harry_potter_1)
    print("The first and second values from the list = ", and_statment_harry_potter_11)
    print("All list = ", and_statment_harry_potter_2)

    # and statment, way 2
    and_statment_harry_potter_3 = db.session.query(models.Film). \
        filter(models.Film.title != "Harry Potter and the Half-Blood Prince"). \
        filter(models.Film.rating >= 7.5
               ).all()
    print(and_statment_harry_potter_3)

    # and statment, way 3, uses and_
    and_statment_harry_potter_4 = db.session.query(models.Film).filter(
        and_(
            models.Film.title != "Harry Potter and the Half-Blood Prince",
            models.Film.rating >= 7.5
        )
    ).all()
    print(and_statment_harry_potter_4)
    print("\n")
    # all have the same value = and_statment_harry_potter_2 = and_statment_harry_potter_3 = and_statment_harry_potter_4

    # Search with text = like, ilike (isn't sensitive to the register of letters)
    deathy_hallows_1 = db.session.query(models.Film).filter(
        models.Film.title.like("%Deathly Hallows%")
    ).all()
    print(deathy_hallows_1)

    deathy_hallows_2 = db.session.query(models.Film).filter(
        models.Film.title.ilike("%deathly hallows%")
    ).all()
    print(deathy_hallows_2)
    print("\n")

    # in_ = select films whose duration is 146 and 161
    harry_potter_sorted_by_length_1 = db.session.query(models.Film).filter(
        models.Film.length.in_([146, 161])
    ).all()
    print(harry_potter_sorted_by_length_1)

    # ~ in_ = select films whose duration is NOT equal to 146 and 161, i.e. the opposite in_
    harry_potter_sorted_by_length_2 = db.session.query(models.Film).filter(
        ~models.Film.length.in_([146, 161])
    ).all()
    print(harry_potter_sorted_by_length_2)
    print("\n")


def queries_joins():
    """
    QUERYING WITH JOINS
    for many-to-many
    """
    films_with_actors = db.session.query(models.Film).join(models.Film.actors).all()
    # before you need to add {self.actors} in __repr__
    print(films_with_actors)


if __name__ == "__main__":
    app = current_app()
    with app.app_context():
        queries_select()
        queries_joins()
