import random

question = (input('What is your question? '))

answer = random.choices(['Yes - definitely.' , 
'It is decidedly so.' ,
'Without a doubt.',
'Reply hazy, try again.',
'Ask again later.',
'Better not tell you now.',
'My sources say no.',
'Outlook not so good.',
'Very doubtful.'])

print(answer)