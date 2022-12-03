# CRUD with Flask

Project name: **_TODO APP_**

**make and activate environment for project using command given**

**1: making environment and installing dependencies**
**_Install python 3.9.13 on local machine https://www.python.org/_**
**i: installing pipenv:**

**_windows:_** pip install pipenv
**_macOS/Linux:_** pip3 install pipenv

**ii: installing package:_**
open terminal in TODO-APP directory and run
**_macOS/Linux/Windows:_** pipenv install

after that use the command **pipenv --venv** so you will have current project venv interpretar path.
Select interpreter from this path and activate the environment.

**3: Setup .env to load environment variables**

add .env file in TODO-APP directory as same as .env.example and setup all variables.

**4: cd into server directory and run python shell**

commands to run:
_a:_ from app import app
_b:_ from app import db.create_all()

exit from python shell().

**5: Run the Application in termnal**
Make sure to activate the virtual environment and you are in backend-paradise directory
_​use command to run flask-server:_ python main.py

**Note:**
mrthod to decrypt the response is added and explained inside the server/app/utils.py
