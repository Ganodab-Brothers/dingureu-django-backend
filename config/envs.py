import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ.get(
    "SECRET_KEY", 't6p&4yojr&qu$8-@exk#(ptj9agmo6@+_1x5xjzs4_latwayhg')

DEBUG = os.environ.get("DEBUG", "true")

DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = os.environ.get("DB_PORT", "5432")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "1234")
DB_NAME = os.environ.get("DB_NAME", "database")

WAS_HOST = os.environ.get(
    "WAS_HOST") if not DEBUG else "http://localhost:8000/api/"
API_VERSION = os.environ.get("API_VERSION", "1.0")
BUCKET_NAME = os.environ.get("BUCKET_NAME", "dingureu-test")

LOGDNA_INGEST_KEY = os.environ.get("LOGDNA_INGEST_KEY")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")