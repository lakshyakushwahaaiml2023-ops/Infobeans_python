'''30. Chatbot Reply System
Problem Statement

Different bots reply differently.

Create:

SupportBot
SalesBot
FAQBot

'''

import os
from abc import ABC, abstractmethod
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class ChatBot(ABC):

    def __init__(self, system_prompt):

        self.__client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

        self.__messages = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]

    @property
    @abstractmethod
    def name(self):
        pass

    def get_response(self, user_input):

        self.__messages.append({
            "role": "user",
            "content": user_input
        })

        response = self.__client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=self.__messages
        )

        reply = response.choices[0].message.content

        self.__messages.append({
            "role": "assistant",
            "content": reply
        })

        return reply

    @abstractmethod
    def start(self):
        pass

    def chat(self):

        print(f"\n{self.name} Started!")
        print("Type 'exit' to return to menu.\n")

        while True:

            user_input = input("You: ").strip()

            if user_input.lower() == "exit":
                print("Returning to menu...")
                break

            if not user_input:
                continue

            try:
                reply = self.get_response(user_input)
                print(f"\n{self.name}: {reply}\n")

            except Exception as e:
                print("Error:", e)



class SupportBot(ChatBot):

    def __init__(self):

        super().__init__(
            "You are a customer support assistant. "
            "Help users resolve complaints, technical problems "
            "and provide troubleshooting steps. Be polite and clear."
        )

    @property
    def name(self):
        return "Support Bot"

    def start(self):
        self.chat()



class SalesBot(ChatBot):

    def __init__(self):

        super().__init__(
            "You are a professional sales assistant. "
            "Help customers understand products, compare features "
            "and make purchasing decisions. Never invent prices."
        )

    @property
    def name(self):
        return "Sales Bot"

    def start(self):
        self.chat()


class FAQBot(ChatBot):

    def __init__(self):

        super().__init__(
            "You are an FAQ assistant. "
            "Answer frequently asked questions clearly and concisely. "
            "If you don't know an answer, admit it."
        )

    @property
    def name(self):
        return "FAQ Bot"

    def start(self):
        self.chat()


class UI:

    def __init__(self):

        self.__bots = {
            1: SupportBot,
            2: SalesBot,
            3: FAQBot
        }

    def run(self):

        while True:

            print("\n========== CHATBOT SYSTEM ==========")
            print("1. Support Bot")
            print("2. Sales Bot")
            print("3. FAQ Bot")
            print("4. Exit")

            try:
                choice = int(input("Enter choice: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if choice == 4:
                print("Application closed!")
                break

            bot_class = self.__bots.get(choice)

            if bot_class is None:
                print("Invalid choice!")
                continue

            bot = bot_class()
            bot.start()


app = UI()
app.run()
