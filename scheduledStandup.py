
from httplib2 import Http
# this is importing a specific type of library
from json import dumps
import schedule
# this is importing a specific type of library
import time
# this is importing a specific type of library



def main():
    url = 'https://chat.googleapis.com/v1/spaces/AAAAeBvXdN4/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=rlRfuLBPHz9n3Ol01YSoP48EcmD4VQEhNhITkkrN8hI%3D'
    bot_message = {
        'text' : 'Hello, I am Standup Stan! @all 1. What are you working on today? 2. What are you having trouble with? 3. Are you blocked on anything?'}

    message_headers = { 'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )

    print(response)

if __name__ == '__main__':
    main()

# nameOfLibrary.function.parameter
#schedule.every(1).minute.do(main)
schedule.every().day.at("011:00").do(main,'It is 011:00')

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute