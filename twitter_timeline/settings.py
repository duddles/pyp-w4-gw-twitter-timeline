import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HOST = "ds013014.mlab.com"
USERNAME = "gk_guy"
PASSWORD = "rmotr1234"
PORT = "13014"
DATABASE_NAME = "twitterdb"

FULL_MONGO_HOST = "mongodb://{usr}:{pwd}@{host}:{port}/{db}".format(
    usr=USERNAME,
    pwd=PASSWORD,
    host=HOST,
    port=PORT,
    db=DATABASE_NAME)
