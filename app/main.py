from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from app.planner_agent import PlannerAgent   # ← your real agent

app = FastAPI()
planner = PlannerAgent()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1️⃣ Serve Static Folder (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")


# 2️⃣ Serve UI (index.html)
@app.get("/", include_in_schema=False)
async def serve_frontend():
    return FileResponse("static/index.html")


# 3️⃣ Your API Model
class TripRequest(BaseModel):
    destination: str
    days: int
    budget: int
    interests: list


@app.post("/plan-trip")
async def plan_trip(req: TripRequest):
    result = await planner.run(req.dict())
    return {"plan": result}
