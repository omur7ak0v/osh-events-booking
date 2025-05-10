from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Event, Booking
from app import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    events = Event.query.all()
    return render_template('index.html', events=events)

@bp.route('/book/<int:event_id>', methods=['GET', 'POST'])
def book_event(event_id):
    event = Event.query.get_or_404(event_id)
    if request.method == 'POST':
        booking = Booking(
            event_id=event.id,
            user_name=request.form['name'],
            tickets=int(request.form['tickets'])
        )
        db.session.add(booking)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('book.html', event=event)

@bp.route('/bookings')
def show_bookings():
    bookings = Booking.query.options(db.joinedload(Booking.event)).all()
    return render_template('bookings.html', bookings=bookings)