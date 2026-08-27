from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import engine, Base
from .routers import tickets, wazuh, auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SOC Ticketing System",
    description="A lightweight incident ticketing system with Wazuh alert ingestion, "
                 "built as a portfolio project.",
    version="0.1.0",
)

# Loosened for a public demo site — tighten allow_origins to your real domain
# once you know it (e.g. https://cyberjean98.github.io).
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router.router)
app.include_router(tickets.router)
app.include_router(wazuh.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
