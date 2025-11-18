from google import genai

class PlannerAgent:
    def __init__(self):
        self.client = genai.Client(api_key="AIzaSyCUHeLlbjYNacxYtR4nKNfNpzfIvcrfO_c")

    async def run(self, data):
        destination = data.get("destination")
        days = data.get("days")
        budget = data.get("budget")
        interests = ", ".join(data.get("interests", []))

        prompt = f"""
Create a detailed travel plan:

Destination: {destination}
Days: {days}
Budget: ₹{budget}
Interests: {interests}

Provide:
- Day-wise itinerary
- Hotels
- Food recommendations
- Local travel tips
- Budget breakdown
"""

        response = self.client.models.generate_content(
            model="gemini-2.0-flash",   # FIXED MODEL
            contents=prompt
        )

        return response.text

