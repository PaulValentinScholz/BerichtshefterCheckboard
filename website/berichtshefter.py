import datetime

from website import db
from website.models import Berichtshefter


def create_berichtshefter(uid):
    vonDate = datetime.date(2022, 8, 29)
    bisDate = vonDate + datetime.timedelta(days=4)
    for week in range(157):
        new_berichtshefter = Berichtshefter(vonDatum=vonDate, bisDatum=bisDate, user_id=uid)
        db.session.add(new_berichtshefter)
        vonDate=vonDate + datetime.timedelta(days=7)
        bisDate=vonDate + datetime.timedelta(days=4)
    db.session.commit()
