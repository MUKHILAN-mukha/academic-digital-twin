from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine
from app.models import Base
from app.routes import events, digital_twin, auth, admin

# ✅ CREATE APP FIRST
app = FastAPI(title="Academic Digital Twin Backend")

# ✅ MIDDLEWARE
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ CREATE DB TABLES
Base.metadata.create_all(bind=engine)

# ✅ REGISTER ROUTES
app.include_router(auth.router)
app.include_router(events.router)
app.include_router(digital_twin.router)
app.include_router(admin.router)

@app.get("/")
def root():
    return {"status": "Backend running"}
