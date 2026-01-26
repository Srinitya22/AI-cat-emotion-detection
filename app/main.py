from fastapi import FastAPI
from app.routers import auth, predict
from app.database import Base, engine
from app.models import user

# Create DB tables
Base.metadata.create_all(bind=engine)


# Create FastAPI app FIRST
app = FastAPI(
    title="Cat Emotion Detection Backend",
    description="Backend API for cat emotion detection using audio and/or image",
    version="1.0.0"
)

# Include routers
app.include_router(auth.router)
app.include_router(predict.router)

# Root endpoint
@app.get("/")
def root():
    return {"message": "Cat Emotion Detection Backend is running"}

# Health check
@app.get("/health")
def health():
    return {"status": "ok"}
