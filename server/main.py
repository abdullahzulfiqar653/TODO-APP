"""starting point of flask"""

from app import app
from dotenv import dotenv_values
env_variables = dotenv_values("../.env")

if __name__ == '__main__':
    app.run(debug=True)
