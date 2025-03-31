from random import choice, randint

def get_response(user_input:str) ->str:
   lowered: str = user_input.lower()

   if lowered == '':
       return 'Quite silent innit?'
   elif 'hello' in lowered:
       return 'hello there!'
   elif 'how are you' in lowered:
       return 'Quite jolly picking pennies'
   elif 'bye' in lowered:
       return 'later chap!'
   elif 'roll a dice' in lowered:
       return f'You rolled: {randint(1,6)} '
   else:
       return choice ([
    "Brain.exe has popped out for a cuppa. Try again?",
    "I think I left my understanding at the pub.",
    "That command went *right over me noggin*!",
    "If I had a quid for every time I was confused…",
    "Blimey! That one’s got me circuits in a twist!",
    "New command detected! Just pulling your leg, I haven't the foggiest.",
    "Are you speaking in riddles? Because I’m utterly baffled.",
    "404: Command not found, mate.",
    "I’d love to help, but I haven’t the faintest clue what you just said.",
    "That request was so advanced, I need a proper upgrade and a strong cuppa."
])
