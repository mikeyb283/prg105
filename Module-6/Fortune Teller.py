# Magic 8-ball by Mike Balling
""" I remember how much fun the magic 8-ball was when I was a kid.
These answers are taken straight from a magic 8-ball so ask it any question you like!"""

import sys
import random

ans = True
answer = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
while ans:
    question = raw_input("Ask the magic 8 ball a question (press enter to quit):\n ")

    if question == "":
        sys.exit()
    else:
        print random.choice(answer)
