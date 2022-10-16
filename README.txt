# install virtual_environments
pip -m venv env

#install dependencies
python -m pip install -r requirements.txt

#run flask_app
FLASK_APP=wsgi.py
flask run