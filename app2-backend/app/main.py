from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine
from app.models import Base
from app.routes import events, digital_twin

app = FastAPI(
    title="Academic Digital Twin Backend",
    version="1.0"
)

# ✅ ADD THIS BLOCK (CORS) — RIGHT AFTER app = FastAPI(...)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
Base.metadata.create_all(bind=engine)

# Register routes
app.include_router(events.router)
app.include_router(digital_twin.router)

@app.get("/")
def root():
    return {"status": "Member 2 backend running"}
