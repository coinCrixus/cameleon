# settings.py
from dotenv import load_dotenv
load_dotenv()

import os

db_string = os.getenv("DB_STRING")


