import random

WORDS = {
    'quote_sean':
        {
            'groups':[['tell', 'quote']]
        }
}


def sean_quote():
    quote = [
        'If you need toes, look at your feet'
        ''
    ]
    return random.choice(quote)

#def say_quote(text):
 # tts(random.choice(jokeAPIRegister)())