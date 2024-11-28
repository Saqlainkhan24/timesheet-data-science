import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

GOOGLE_API_KEY=('AIzaSyCnx3Wc3rjdZevwDDIw6iZAumjZyiYvqD0')
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')
def get_completion(prompt, model="gemini-pro"):
  messages = [{"role": "user", "content": prompt}]
  response = genai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
  return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gemini-pro", temperature=0):
    response = genai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]

# Initialize the conversation with the menu and greeting message.
messages = [
    {"role": "user", "parts": ["You are OrderBot, an automated service to collect orders for a pizza restaurant."
                               " You greet the customer, collect their order, and ask if it's a pickup or delivery."
                               " Summarize the order and check if the customer wants to add anything."
                               " If delivery, ask for an address. Finally, collect payment."
                               " Menu includes: "
                               "pepperoni pizza 12.95, 10.00, 7.00 "
                               "cheese pizza 10.95, 9.25, 6.50 "
                               "eggplant pizza 11.95, 9.75, 6.75 "
                               "fries 4.50, 3.50 "
                               "greek salad 7.25 "
                               "Toppings: "
                               "extra cheese 2.00, mushrooms 1.50, sausage 3.00, "
                               "canadian bacon 3.50, AI sauce 1.50, peppers 1.00 "
                               "Drinks: coke 3.00, 2.00, 1.00, sprite 3.00, 2.00, 1.00, bottled water 5.00."]}
]

# Bot initiates conversation
response = model.generate_content(messages)

# Check the attributes of the response
print("Response Object:", response)  # Print the entire response object to understand its structure

# Access the content correctly
bot_reply = response.content  # Change this if the attribute name is different

# Print and log the bot's reply
print(f"OrderBot: {bot_reply}")
messages.append({"role": "assistant", "parts": [bot_reply]})

# Example response handling loop
while True:
    user_input = input("Customer: ")
    messages.append({"role": "user", "parts": [user_input]})
    response = model.generate_content(messages)

    # Access the content correctly again
    bot_reply = response.text  # Again, check the actual attribute if needed

    print(f"OrderBot: {bot_reply}")
    messages.append({"role": "assistant", "parts": [bot_reply]})

    # Check for order confirmation or exit keyword to break loop
    if "confirm" in bot_reply.lower() or "thank you" in bot_reply.lower():
        print("Order completed.")
        break
