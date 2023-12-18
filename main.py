from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vacation_spots.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()
db = SQLAlchemy(app)

class VacationSpot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    place = db.Column(db.String(255))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    description = db.Column(db.Text)




popular_spots = [
    {'place': 'Beach Resort', 'latitude': 25.0343, 'longitude': -77.2405, 'description': 'Beautiful sandy beaches and clear blue waters.'},
    {'place': 'Mountain Cabin', 'latitude': 36.5731, 'longitude': -118.2325, 'description': 'Cozy cabin with stunning mountain views.'},
    {'place': 'City Apartment', 'latitude': 40.7128, 'longitude': -74.0060, 'description': 'Modern apartment in the heart of the city.'},
    {'place': 'Historical Site', 'latitude': 41.9028, 'longitude': 12.4964, 'description': 'Explore the rich history of this ancient site.'},
]




@app.route('/')
def index():
    spots = VacationSpot.query.all()
    spot_data = [{'place': spot.place, 'latitude': spot.latitude, 'longitude': spot.longitude, 'description': spot.description} for spot in spots]
    return render_template('index.html', spots=spot_data)



if __name__ == '__main__':
    app.run(debug=True)
