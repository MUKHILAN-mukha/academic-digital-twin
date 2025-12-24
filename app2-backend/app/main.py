from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine
from app.models import Base
from app.routes import events, digital_twin, auth

# ✅ CREATE APP FIRST
app = FastAPI(title="Academic Digital Twin Backend")

# ✅ THEN USE app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create DB tables
Base.metadata.create_all(bind=engine)

# Register routes
app.include_router(auth.router)
app.include_router(events.router)
app.include_router(digital_twin.router)


@app.get("/")
def root():
    return {"status": "Backend running"}
