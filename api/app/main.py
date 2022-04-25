from flask import jsonify

from app_factory import create_app

app = create_app()

@app.route('/')
def home():
    return jsonify({'it': 'works!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
