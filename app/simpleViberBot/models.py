# -*- coding: utf-8 -*-
from sqlalchemy.orm import relationship
from app import db


class Cities(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(100), index=True, unique=True)
    city_url = db.Column(db.Text(), index=True, unique=True)
    author = db.Column(db.String(100), unique=True)
    photos = relationship('CityPhotos')

    def __repr__(self):
        return '<City name %r>' % self.city_name


class CityPhotos(db.Model):
    __tablename__ = 'city_photos'
    id = db.Column(db.Integer, primary_key=True)
    photo_url = db.Column(db.Text(), index=True, unique=True)
    parent_id = db.Column(db.Integer, db.ForeingKey('cities.id'))

    def __repr__(self):
        return '<Photo URL %r>' % self.photo_url
