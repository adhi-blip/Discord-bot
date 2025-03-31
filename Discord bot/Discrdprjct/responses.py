from random import choice, randint
from Respnse  import chat_with_ollama

def get_response(user_input:str) ->str:
   lowered: str = user_input.lower()

   if lowered == '':
       return 'Quite silent innit?'
   elif 'hello ' in lowered:
       return 'hello there!'
   elif 'how are you' in lowered:
       return 'Quite jolly picking pennies'
   elif 'bye' in lowered:
       return 'later chap!'
   elif 'roll a dice' in lowered:
       return f'You rolled: {randint(1,6)} '
   else:
       return chat_with_ollama(lowered)