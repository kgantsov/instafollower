from datetime import datetime

from peewee import Model
from peewee import CharField
from peewee import DateField
from peewee import BooleanField
from peewee import SqliteDatabase

db = SqliteDatabase('following.db')


class Following(Model):
    name = CharField(index=True)
    is_following = BooleanField(default=True)
    date_created = DateField(default=datetime.now)

    class Meta:
        database = db
        db_table = 'following'

    def __repr__(self):
        return '<Following ({id}, {is_following}, {date_created})>'.format(
            id=self.id,
            is_following=self.is_following,
            date_created=self.date_created
        )


class Comment(Model):
    url = CharField(index=True)
    comment = CharField()
    date_created = DateField(default=datetime.now)

    class Meta:
        database = db
        db_table = 'comments'

    def __repr__(self):
        return '<Comment ({id}, {url}, {comment}, {date_created})>'.format(
            id=self.id,
            url=self.url,
            comment=self.comment,
            date_created=self.date_created
        )


class Like(Model):
    url = CharField(index=True)
    date_created = DateField(default=datetime.now)

    class Meta:
        database = db
        db_table = 'likes'

    def __repr__(self):
        return '<Like ({id}, {url}, {date_created})>'.format(
            id=self.id,
            url=self.url,
            date_created=self.date_created
        )
