# 📌 INTRODUCTION  
The Smart Travel Planner is an AI-powered multi-agent system designed to generate structured, personalized, and budget-friendly travel itineraries. It analyzes user preferences such as destination, days, interests, and budget to create an optimized trip plan.

---

# 📌 PROBLEM STATEMENT  
Planning a trip is time-consuming and often unorganized. Users face challenges like:
- Selecting destinations based on interests  
- Managing budget effectively  
- Creating day-wise itineraries  
- Adjusting travel plans dynamically  

There is a need for a system that automates travel planning while ensuring personalization, clarity, and cost-effectiveness.

---

# 📌 PROPOSED SOLUTION  
This project introduces a **multi-agent AI system** where each agent performs a specialized task:

- **Planner Agent**: Creates initial itinerary  
- **Validator Agent**: Fixes inconsistencies and ensures budget feasibility  
- **Formatter Agent**: Produces structured JSON output  
- **Refiner Agent**: Enhances clarity and readability  

The system is accessed via a FastAPI backend and a clean frontend interface.

---

# 📌 ARCHITECTURE  

## 🔹 High-Level Flow  
```
User → Frontend → FastAPI Backend → Multi-Agent System → Final Itinerary
```

## 🔹 Multi-Agent Workflow  
```
[Input] → Planner Agent → Validator Agent → Formatter Agent → Output
```

## 🔹 Folder Structure  
```
project/
│── main.py
│── agents/
│     ├── planner_agent.py
│     ├── validator_agent.py
│     ├── formatter_agent.py
│── static/
│── templates/
│── README.md
│── requirements.txt
```

---

# 📌 INSTRUCTION FOR SETUP  

### 🚀 Requirements  
- Python 3.10+
- FastAPI
- Uvicorn
- OpenAI API / Local LLM

### 📦 Installation  
```bash
git clone <your-repo-link>
cd project
pip install -r requirements.txt
```

### ▶️ Run Backend  
```bash
uvicorn main:app --reload --port 8000
```

### 🌐 Run Frontend  
Open `index.html` in browser  
(or use Live Server)

---

# 📌 DIAGRAM  

## 🌐 System Architecture Diagram  
```
+-------------+        +-----------------+        +----------------------+
|   USER      | -----> | FRONTEND (UI)   | -----> | FASTAPI BACKEND     |
+-------------+        +-----------------+        +----------+-----------+
                                                           |
                                                           v
                                                +----------------------+
                                                |  MULTI-AGENT SYSTEM  |
                                                +----------------------+
                                                | Planner Agent        |
                                                | Validator Agent      |
                                                | Formatter Agent      |
                                                +----------------------+
                                                           |
                                                           v
                                                +----------------------+
                                                |  FINAL ITINERARY     |
                                                +----------------------+
```

## 🔄 Multi-Agent Flow Diagram  
```
[User Input]
      |
      v
[Planner Agent] → [Validator Agent] → [Formatter Agent] → [Final JSON Output]
```

---
