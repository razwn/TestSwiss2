from utils.util import print_hello
from utils.api_requests import APIS
# pip install python-dotenv
from dotenv import load_dotenv
import os
load_dotenv(".env")

print_hello()
print(os.environ.get("API_KEY"))
print(os.environ.get("PAROLA_DB"))
