import os

# Statement for enabling the development environment
DEBUG = True

BIND_HOST = "127.0.0.1"
BIND_PORT = 8080

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Define path to directory containing indexed data
INDEX_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data")

# Number of snippets to return for each batch
SEARCH_PAGINATION = 20