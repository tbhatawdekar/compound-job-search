from groq import Groq
import os

# globals
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

messages = []

# takes message & makes llm call
def call_llm(message): 
  response = groq_client.chat.completions.create(
    messages=message,
    model="groq/compound-mini"
  )
  return (response.choices[0].message.content, response.choices[0].message.executed_tools)

# logic
def job_board_bot(query):
  # invoke compound model
  messages.append(
    {
      "role": "user",
      "content": query,
    }
  )
  
  response, tools = call_llm(message=messages)
  messages.append({
      "role": "assistant",
      "content": response
    })
  return response
  
  
  # get user query
  # do some tool invocation based on user query
  # generate answer & return
  
  # multiturn chat client? -> get user input
  # call conversation bot & get reponse & will continue conversation
  
  # exit condition, if user types "bye"
  
  # loop - get user input
    # if user input != "bye"
      # get response
    # else quit
if __name__ == "__main__":
  user_input = input("enter query: ")
  while (user_input != "bye"):
    response = job_board_bot(user_input)
    print(response)
    user_input = input("enter query: ")