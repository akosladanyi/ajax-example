cd server
pipenv install
pipenv shell
export FLASK_APP=main.py
flask run
xdg-open http://127.0.0.1:5000/
