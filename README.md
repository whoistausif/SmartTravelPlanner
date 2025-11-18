# Smart Travel Planner — AI Multi-Agent Travel Assistant

A fully-featured **AI Multi-Agent Travel Planner** that generates personalized, budget-optimized travel itineraries using FastAPI, LLM-powered agents, and a modern interactive frontend.

This project demonstrates multi-agent reasoning, tool use, backend–frontend integration, and deployment on a live environment.

---

## Problem

Travel planning is complicated and time-consuming. Users must search multiple websites for attractions, routes, weather, budget, and day-wise planning. Traditional LLM prompts often hallucinate or generate unrealistic plans.

---

## Why Agents?

Travel planning is a multi-step reasoning task.  
This system uses **specialized AI agents** that collaborate:

### 1. Research Agent  
Fetches attractions, weather insights, and local information.

### 2. Budget Agent  
Calculates cost and checks feasibility.

### 3. Planner Agent  
Creates the full day-by-day itinerary.

### 4. Review Agent  
Fixes errors, improves clarity, and finalizes the output.

This produces realistic, structured, accurate itineraries.

---

## Features

### Frontend (static/index.html)
- Clean soft-minimal UI  
- Dark/Light theme switch  
- Animated glow effects  
- Skeleton loading shimmer  
- Voice output (Speak / Stop)  
- Google Maps integration  
- Save itinerary as **TXT**  
- Save itinerary as **PNG**

### Backend (FastAPI)
- Multi-agent pipeline  
- `/plan-trip` endpoint  
- Serves index.html  
- Async processing  
- Ideal for deployment

### AI
- Gemini / Groq / OpenAI-ready  
- Multi-step reasoning  
- Context-aware travel plans  

---

## Architecture Overview
User Input
│
▼
Frontend (index.html)
│ fetch("/plan-trip")
▼
FastAPI Backend (main.py)
│
▼
Multi-Agent Engine
┌────────────┬────────────┬─────────────┐
│Research │Budget │ Planner │
│Agent │Agent │ Agent │
└────────────┴────────────┴─────────────┘
│
▼
Review Agent
│
▼
Final Itinerary → Shown in UI

---

## Project Structure
├── app/
│ ├── main.py
│ └── planner_agent.py
│
├── static/
│ └── index.html
│
├── venv/
│
├── Procfile
├── requirements.txt
└── README.md

---

## File Details

### app/main.py
- FastAPI server  
- `/plan-trip` endpoint  
- Serves UI  
- Runs PlannerAgent

### app/planner_agent.py
- Core multi-agent logic  
- Calls LLM  
- Creates final itinerary

### static/index.html
- UI + JS logic  
- Light/Dark theme  
- Speak/Stop  
- Glow & animation  
- PNG/TXT export  
- Maps integration

### Procfile
web: uvicorn app.main:app --host 0.0.0.0 --port $PORT

### requirements.txt
List of backend dependencies.

---

## Local Setup

### Clone
```bash
git clone https://github.com/YOUR_USERNAME/SmartTravelPlanner.git
cd SmartTravelPlanner

```
Install dependencies
```bash pip install -r requirements.txt ```
Run server
```bash uvicorn app.main:app --reload```
