import os
from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI()

# Get the URL from the Environment Group you linked
DATABASE_URL = os.environ.get("DATABASE_URL")

# Create the database connection engine
engine = create_engine(DATABASE_URL)

@app.get("/test-db")
def test_connection():
    try:
        # Use a context manager to open/close the connection safely
        with engine.connect() as connection:
            # Run a simple query to verify
            result = connection.execute(text("SELECT 1"))
            return {"status": "Database connected successfully!", "data": result.scalar()}
    except Exception as e:
        return {"status": "Connection failed", "error": str(e)}