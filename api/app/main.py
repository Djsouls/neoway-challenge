from flask import jsonify

from flask_sqlalchemy import SQLAlchemy

from app_factory import create_app
from extensions import db

app = create_app()

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return jsonify({'it': 'works!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
