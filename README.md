# TODO CRUD with Flask
to run the project please follow the instructions given

**1: making environment and installing dependencies**

**i:** Install python 3.9.13 on local machine https://www.python.org/_

**ii:** clone the project and open terminal inside TODO-APP

**iii:** installing pipenv

```
pip install pipenv
```

**iv:** installing package:

open terminal in TODO-APP directory and run
```
pipenv install
``` 

**2: activate environment: **
```
pipenv shell
```

**3: Setup .env to load environment variables**

add .env file in TODO-APP directory as same as .env.example and setup all variables.

**4: cd into server directory and run python shell**

commands to run:
```
from app import db
```
```
db.create_all()
```

**5: Run the Application in termnal**

Make sure to activate the virtual environment and you are in server directory

use command to run flask-server:
```
python main.py
```

**Note:**
method to decrypt the response is added and explained inside the server/app/utils.py
