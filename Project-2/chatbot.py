import random
import json
import time
import datetime

#loading responses from 'responses.json'
def load_responses():
    try:
        with open('responses.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: responses.json file not found.")
        return {}
#generate agent names, 6 first names and 6 last names = 36 Names
    
def generatename():
    first_names = ['Mary', 'John', 'James', 'Michael', 'Sophia', 'Sara']
    last_names = ['Smith', 'Brown', 'Miller', 'Garcia', 'Rodriguez', 'Jones']
    return random.choice(first_names) + " " + random.choice(last_names)

# print(f'Hello my name is {generatename()}')

# logging the converstaion to a text file "logs.txt"

def log_convo(user_name, user_input, response):
    with open('logs.txt','+a') as logsfile:
        logsfile.write(f'User: {user_name} : {user_input}\n')
        logsfile.write(f'Agent: {response}\n')
        logsfile.write('-' * 50 + "\n")

# respond to user input

def agentrespond(user_input, responses, user_name):
    user_input = user_input.lower()
    # date time response 

    if "date" in user_input:
        current_date = datetime.date.today()  # get today's date
        return f"Today's date is {current_date}"
    
    elif "time" in user_input:
        current_time = datetime.datetime.now().time()  # get current time
        return f"The time is {current_time}"

    for keyword, response_list in responses.items():
        if keyword in user_input:
            response = random.choice(response_list)
            return response.format(user_name=user_name)
    return random.choice(responses["default"])

# main chatbot

def main():
    # responses from json
    responses = load_responses()
    
    
    # generate agent_name

    agent_name = generatename()
    print(f'Hello! My name is {agent_name} and I am your Personal Assistant. Feel free to ask me anything.')
    time.sleep(1)
    user_name = input('Before we start, may I ask what your name is? : ')
    time.sleep(1)
    if user_name == agent_name.split()[0]:
        print('It seems like we both share the same name. ')
    else:
        print(f'Greetings {user_name}!')

    while True:
        # get user input
        user_input = input(f"{user_name}: ")

        # exit the chat if the user says 'bye', 'quit', or 'exit'
        if user_input.lower() in ["bye", "quit", "exit"]:
            print(f"{agent_name}: Goodbye, {user_name}! Have a great day!")
            break

        # get a response based on the input
        response = agentrespond(user_input, responses, user_name)

        # display the response
        print(f"{agent_name}: {response}")
        
        # log the conversation
        log_convo(user_name, user_input, response)
        
        # randomly disconnect the chat (simulate disconnection with a small chance)
        if random.random() < 0.05:  # 5% chance of random disconnect
            print(f"{agent_name}: Oops, it seems like there's a technical issue. Please try again later.")
            time.sleep(5)  # simulate delay before reconnecting
            print(f"{agent_name}: I'm back! How can I assist you further, {user_name}?")

if __name__ == "__main__":
    main()