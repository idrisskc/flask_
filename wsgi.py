import os
from app import create_app

app = create_app()

@app.route('/')
def index():
    return '<h1>Hello!</h1>'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run() 