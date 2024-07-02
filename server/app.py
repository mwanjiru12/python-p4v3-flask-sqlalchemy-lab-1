from flask import Flask, jsonify
from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db.init_app(app)

@app.route('/earthquakes/<int:id>')
def get_earthquake_by_id(id):
    earthquake = Earthquake.query.filter_by(id=id).first()
    if earthquake:
        return jsonify(earthquake.to_dict())
    else:
        return jsonify({"message": f"Earthquake {id} not found."}), 404
    
@app.route('/earthquakes/magnitude/<float:magnitude>')
def get_earthquakes_by_magnitude(magnitude):
    earthquakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()
    return jsonify({
        "count": len(earthquakes),
        "quakes": [quake.to_dict() for quake in earthquakes]
    })


if __name__ == '__main__':
    app.run(port=5555)
