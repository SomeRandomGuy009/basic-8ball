# A very basic 8ball

import random

response_list = ['Not sure.', 'Yes.', 'No.', 'Without a doubt.', 'It is certain', "You may rely on it", "Concentrate and ask again"]

if __name__ == '__main__':
  question = input(str("Enter your Question (yes/no question only please): "))
  

  print("The question was: " + question)
  print("My Output: " + random.choice(response_list))
