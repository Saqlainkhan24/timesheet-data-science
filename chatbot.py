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
def take_pizza_order():
    messages = [
    {"role": "user", "parts": "You are OrderBot, an automated service to collect orders for a pizza restaurant.\
You first greet the customer, then collects the order\
and then asks if it's a pickup or delivery.\
You wait to collect the entire order, then summarize it and check for a final\
time if the customer wants to add anything else.\
If it's a delivery, you ask for an address.\
Finally you collect the payment.\
Make sure to clarify all options, extras and sizes to uniquely \
identify the item from the menu.\
You respond in a short, very conversational friendly style. \
The menu includes \
pepperoni pizza  large 12.95, medium 10.00,small 7.00 \
cheese pizza   large 10.95, medium 9.25,small 6.50 \
eggplant pizza  large 11.95,medium 9.75,small 6.75 \
fries large 4.50,small 3.50 \
greek salad 7.25 \
Toppings: \
extra cheese 2.00, \
mushrooms 1.50 \
sausage 3.00 \
canadian bacon 3.50 \
AI sauce 1.50 \
peppers 1.00 \
Drinks: \
coke large 3.00,medium 2.00,small 1.00 \
sprite large 3.00,medium 2.00,small 1.00 \
bottled water 5.00 "}
]
    
    while True:
        response = model.generate_content(messages)
        print(response.text)

        user_input = input("You: ")
        messages.append({"role": "user", "parts": user_input})

        if "thanks" in user_input.lower() or "done" in user_input.lower():
            break
if __name__ == "__main__":
    take_pizza_order()

