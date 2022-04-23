from app_factory import create_app

app = create_app()

@app.route('/')
def home():
    return 'uepa'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
