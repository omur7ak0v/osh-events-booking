from datetime import datetime
from app import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    location = db.Column(db.String(100), nullable=False)
    tickets_available = db.Column(db.Integer, default=100)
    bookings = db.relationship('Booking', backref='event', lazy=True)  # Добавьте эту строку

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    user_name = db.Column(db.String(50), nullable=False)
    tickets = db.Column(db.Integer, default=1)