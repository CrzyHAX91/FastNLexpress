import re
from fuzzywuzzy import fuzz
import random
from textblob import TextBlob
import json

class AdvancedAIHelpdesk:
    def __init__(self):
        self.context = []
        self.feedback_scores = []
        self.user_profiles = {}
        self.knowledge_base = self.load_knowledge_base()
    
    def load_knowledge_base(self):
        try:
            with open('knowledge_base.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Knowledge base file not found. Please ensure it exists.")
            return {}
        except json.JSONDecodeError:
            print("Error decoding the knowledge base JSON file. Please check the file format.")
            return {}

    def generate_response(self, prompt, user_id):
        prompt_lower = prompt.lower()
        best_match = None
        best_score = 0

        for key, response in self.knowledge_base.items():
            for k in key.split('|'):
                score = fuzz.partial_ratio(k, prompt_lower)
                if score > best_score:
                    best_score = score
                    best_match = response

        if best_score >= 70:  # Adjusted threshold
            self.context.append(prompt)
            response = self.personalize_response(best_match, user_id)
            follow_up = self.generate_follow_up(prompt_lower)
            return f"{response}\n\n{follow_up}"
        elif self.context:
            return self.handle_follow_up(prompt_lower, user_id)
        else:
            return "I apologize, but I don't have specific information about that. Would you like me to connect you with a human customer service representative? You can also check our services through Cloudflare."

    def personalize_response(self, response, user_id):
        if user_id in self.user_profiles:
            if "shipping" in response.lower() and "location" in self.user_profiles[user_id]:
                response += f"\n\nBased on your location in {self.user_profiles[user_id]['location']}, shipping might take an additional 1-2 days."
        return response

    def generate_follow_up(self, prompt):
        if "track" in prompt:
            return "Would you like to know about our shipping times as well?"
        elif "return" in prompt:
            return "Do you need any information about our refund process?"
        elif "shipping" in prompt:
            return "Would you like to know about our international shipping options?"
        else:
            return "Is there anything else I can help you with?"

    def handle_follow_up(self, prompt, user_id):
        prev_context = self.context[-1].lower()
        if "track" in prev_context and "shipping" in prompt:
            return self.personalize_response(self.knowledge_base["shipping time|delivery time|how long|when will I receive"], user_id)
        elif "return" in prev_context and "refund" in prompt:
            return "Refunds are typically processed within 5-10 business days after we receive the returned item. The refund will be issued to the original payment method."
        else:
            return f"Regarding your previous question about '{prev_context}', could you please provide more specific information about what you'd like to know?"

    def get_feedback(self):
        score = random.randint(1, 5)  # Simulating user feedback
        self.feedback_scores.append(score)
        return score

    def average_feedback(self):
        if self.feedback_scores:
            return sum(self.feedback_scores) / len(self.feedback_scores)
        return 0

    def analyze_sentiment(self, prompt):
        analysis = TextBlob(prompt)
        if analysis.sentiment.polarity < -0.2:  # Adjusted threshold
            return "I apologize for any inconvenience. Would you like me to connect you with a human customer service representative?"
        return None

    def set_user_profile(self, user_id, profile):
        self.user_profiles[user_id] = profile

# Usage example
if __name__ == "__main__":
    helpdesk = AdvancedAIHelpdesk()
    helpdesk.set_user_profile("user123", {"location": "California"})

    test_prompts = [
        "How can I track my order?",
        "Yes, tell me about shipping times.",
        "What's your return policy?",
        "Yes, I need information about refunds.",
        "Do you offer international shipping?",
        "This is frustrating, I can't find my order!",
        "I'm not happy with the service.",
    ]

    for prompt in test_prompts:
        sentiment_response = helpdesk.analyze_sentiment(prompt)
        if sentiment_response:
            print(f"Prompt: {prompt}")
            print(f"Response: {sentiment_response}")
        else:
            response = helpdesk.generate_response(prompt, "user123")
            print(f"Prompt: {prompt}")
            print(f"Response: {response}")
        feedback = helpdesk.get_feedback()
        print(f"Feedback score: {feedback}")
        print("-" * 50)

    print(f"Average feedback score: {helpdesk.average_feedback():.2f}")
