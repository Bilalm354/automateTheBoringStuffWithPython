import random
messages = [
    'It is certain',
    'It is decidedly so',
    'Yes definietely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'outlook not so good',
    'Very doubtful'
    ]
print(messages[random.randint(0, len(messages)-1)])
