from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Text
import uuid
import hashlib

from setting import password_s

Base = declarative_base()


def get_unit_id():
    return uuid.uuid4().hex


def md5(password):
    return hashlib.md5("".join([password, password_s]).encode()).hexdigest()


class UserModel(Base):
    __tablename__ = 'users'
    user_id = Column(String(length=32), primary_key=True, autoincrement=False)
    name = Column(String(length=20))
    password = Column(String(length=32))
    description = Column(Text)
    created = Column(String(length=18))
    image_url = Column(String(length=32))

    def __repe__(self):
        return "UserModel(Table) --> {'name':%s}" % self.name

    def toString(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "password": self.password,
            "description": self.description,
            "created": self.created,
            "image_url": self.image_url,
        }


class ArticleModel(Base):
    __tablename__ = 'articles'
    article_id = Column(String(length=32),
                        primary_key=True, autoincrement=False)
    writor_id = Column(String(length=32))
    writor = Column(String(length=20))
    title = Column(Text)
    description = Column(Text)
    content = Column(Text)
    created = Column(String(length=18))

    def __repe__(self):
        return "ArticleModel(Table) --> {'title':%s}" % self.title

    def toString(self):
        return {
            "article_id": self.article_id,
            "writor_id": self.writor_id,
            "writor": self.writor,
            "title": self.title,
            "description": self.description,
            "content": self.content,
            "created": self.created,
        }


class CommentModel(Base):
    __tablename__ = 'comments'
    comment_id = Column(String(length=32),
                        primary_key=True, autoincrement=False)
    actor_id = Column(String(length=32))
    writor_id = Column(String(length=32))
    article_id = Column(String(length=32))
    content = Column(Text)
    actor = Column(String(length=20))
    writor = Column(String(length=20))
    created = Column(String(length=18))

    def __repe__(self):
        return "CommentModel(Table) --> {'name':%s}" % self.name

    def toString(self):
        return {
            "comment_id": self.article_id,
            "article_id": self.article_id,
            "actor_id": self.article_id,
            "writor_id": self.writor_id,
            "created": self.created,
            "actor": self.actor,
            "writor": self.writor,
            "content": self.content,
        }
