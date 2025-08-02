from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.routes import crew, health
from app.utils.logger import setup_logging

# Setup logging
setup_logging()

# Create FastAPI app
app = FastAPI(
    title="CrewAI Backend API",
    description="Professional FastAPI backend with CrewAI integration",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router, prefix="/api/v1", tags=["health"])
app.include_router(crew.router, prefix="/api/v1", tags=["crew"])

@app.get("/")
async def root():
    return {"message": "CrewAI Backend API", "version": "1.0.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )