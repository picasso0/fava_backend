from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.procedures import router as procedures_router
from routes.views import router as views_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(views_router, prefix="/api/v1")
app.include_router(procedures_router, prefix="/api/v1")

@app.get("/health")
def health_check():
    return {"status": "healthy"}
