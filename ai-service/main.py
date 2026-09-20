"""
FitFlow AI Service - FastAPI Application
Author: Omindu Ayodya
Module: IT3060 - Human Computer Interaction
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI(
    title="FitFlow AI Service",
    description="AI-powered workout generation and nutrition recognition",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/health")
async def health_check():
    """Service health status"""
    return JSONResponse(
        status_code=200,
        content={
            "status": "healthy",
            "service": "FitFlow AI Service",
            "version": "1.0.0",
            "models_loaded": True
        }
    )

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "FitFlow AI Service",
        "documentation": "/docs",
        "health": "/health"
    }

# TODO: Import and include routers
# from routers import workout, nutrition
# app.include_router(workout.router, prefix="/api/v1/workouts", tags=["workouts"])
# app.include_router(nutrition.router, prefix="/api/v1/nutrition", tags=["nutrition"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
