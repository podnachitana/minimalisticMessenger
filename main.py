import time
from datetime import datetime

# 1) Database

db = [
    {
        'text': 'hello',
        'name': 'Ivan',
        'time': time.time()
    },
    {
        'text': 'hello, Ivan',
        'name': 'Petr',
        'time': time.time()
    }
]


# 2) send_message

def send_message(text, name):
    message = {
        'text': text,
        'name': name,
        'time': time.time()
    }
    db.append(message)



# 3) get_message

def get_message(after):
    result = []

    for message in db:
        if message['time'] > after:
            result.append(message)

    return result


# messages = get_message(0)

def print_messages(messages):
    for message in messages:
        print(datetime.fromtimestamp(message['time']), message['name']
              )
        print(message['text'])
        print()
    print('-' * 40)


print_messages(db)
send_message('hi', 'Ivan')
send_message('hi', 'lol')
print_messages(db)
