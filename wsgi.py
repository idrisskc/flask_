import os
from app import create_app
from waitress import serve

app = create_app()

@app.route('/')
def index():
    return '<h1>Hello!</h1>'

# serve(app, host='0.0.0.0', port=8080, threads=1)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run() 