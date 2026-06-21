import os
import pymysql
from fastapi import FastAPI
from contextlib import asynccontextmanager

def test_database_connection():
    try:
        connection = pymysql.connect(
            host=os.environ.get('DB_HOST'),
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASSWORD'),
            database=os.environ.get('DB_NAME'),
            port=3306,
            connect_timeout=10
        )
        print("✅ DATABASE CONNECTED SUCCESSFULLY TO HOSTINGRAJA!", flush=True)
        connection.close()
    except Exception as e:
        print(f"❌ DATABASE CONNECTION FAILED: {e}", flush=True)

# This triggers the test immediately when Uvicorn starts the app
@asynccontextmanager
async def lifespan(app: FastAPI):
    test_database_connection()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"status": "running"}