import os
import pymysql
from fastapi import FastAPI
from contextlib import asynccontextmanager

def test_database_connection():
    print("⏳ Attempting to connect to HostingRaja database...", flush=True)
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
        
        # Verify read access
        with connection.cursor() as cursor:
            cursor.execute("SELECT VERSION();")
            version = cursor.fetchone()
            print(f"📊 HostingRaja Database Version: {version[0]}", flush=True)
            
        connection.close()
    except Exception as e:
        print(f"❌ DATABASE CONNECTION FAILED: {e}", flush=True)

# The lifespan context manager handles tasks when the app starts up and shuts down
@asynccontextmanager
async def lifespan(app: FastAPI):
    # This runs exactly when Uvicorn starts the server application
    test_database_connection()
    yield
    # Any cleanup code can go here after the yield

# Initialize FastAPI with the lifespan handler
app = FastAPI(lifespan=lifespan)

# Root route required for Render's HTTP health checks
@app.get("/")
def read_root():
    return {
        "status": "online",
        "message": "FastAPI service is running smoothly."
    }