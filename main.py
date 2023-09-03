from textbase import bot, Message
from textbase.models import OpenAI
from typing import List

# Load your OpenAI API key
OpenAI.api_key = "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"

# Define a system prompt for your chatbot
SYSTEM_PROMPT = """Welcome to EcoSavvy, your sustainable living assistant. I can help you make eco-friendly choices in your daily life. 
You can ask me about sustainability challenges, eco-friendly recipes, shopping for green products, and more."""

# Placeholder functions for various features
def provide_sustainability_challenge():
    # Generate a sustainability challenge for the user to tackle.
    return "Here's your new sustainability challenge: Reduce water consumption by 20% this week."

def generate_eco_action_plan():
    # Generate a personalized eco-action plan based on the user's preferences.
    return "Your personalized eco-action plan for this month includes reducing plastic waste, using public transportation, and adopting plant-based meals."

def suggest_eco_friendly_recipe():
    # Provide eco-friendly recipes based on user preferences and available ingredients.
    return "Here's a delicious and eco-friendly recipe: [Recipe Details]"

# Additional functions for shopping assistance, carbon offset calculator, etc.

@bot()
def on_message(message_history: List[Message], state: dict = None):
    user_message = message_history[-1].get("value", "").strip().lower()

    if "sustainability challenge" in user_message:
        bot_response = provide_sustainability_challenge()

    elif "eco-action plan" in user_message:
        bot_response = generate_eco_action_plan()

    elif "eco-friendly recipes" in user_message:
        bot_response = suggest_eco_friendly_recipe()

    # Add more conditionals and function calls for other features.

    else:
        bot_response = OpenAI.generate(
            system_prompt=SYSTEM_PROMPT,
            message_history=message_history,
            model="gpt-3.5-turbo",
        )

    response = {
        "data": {
            "messages": [
                {
                    "data_type": "STRING",
                    "value": bot_response
                }
            ],
            "state": state
        },
        "errors": [
            {
                "message": ""
            }
        ]
    }

    return {
        "status_code": 200,
        "response": response
    }
