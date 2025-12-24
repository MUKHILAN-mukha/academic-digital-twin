from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base
from app.routes import auth, events, digital_twin, admin

app = FastAPI(title="Academic Digital Twin Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Create tables AFTER importing models
Base.metadata.create_all(bind=engine)

# ✅ Register routes AFTER app creation
app.include_router(auth.router)
app.include_router(events.router)
app.include_router(digital_twin.router)
app.include_router(admin.router)


@app.get("/")
def root():
    return {"status": "Backend running"}
