from fastapi import FastAPI

# Create the app instance
app = FastAPI(title="Hotel AI Concierge")

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Server is running"}

# Run with: uvicorn main:app --reload