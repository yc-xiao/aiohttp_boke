from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Text
import uuid, hashlib

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

    def __repe__(self):
        return "UserModel(Table) --> {'name':%s}" % self.name

    def toString(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "password": self.password
        }

class ArticleModel(Base):
    __tablename__ = 'articles'
    article_id = Column(String(length=32), primary_key=True, autoincrement=False)
    writor_id = Column(String(length=32))
    title = Column(Text)
    content = Column(Text)

    def __repe__(self):
        return "ArticleModel(Table) --> {'title':%s}" % self.title

    def toString(self):
        return {
            "article_id": self.article_id,
            "writor_id": self.writor_id,
            "title": self.title,
            "content": self.content,
        }


class CommentModel(Base):
    __tablename__ = 'comments'
    comment_id = Column(String(length=32), primary_key=True, autoincrement=False)
    actor_id = Column(String(length=32))
    writor_id = Column(String(length=32))
    article_id = Column(String(length=32))
    content = Column(Text)


    def __repe__(self):
        return "CommentModel(Table) --> {'name':%s}" % self.name

    def toString(self):
        return {
            "comment_id": self.article_id,
            "article_id": self.article_id,
            "actor_id": self.article_id,
            "writor_id": self.writor_id,
            "content": self.content,
        }
