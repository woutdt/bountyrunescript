import time
from plyer import notification
import os
import datetime

print("initiated v1.2")
notification.notify(
    title='Initiated',
    message='script running v1.2',
    app_icon='raspberry.ico', 
    timeout=2, 
)
print("-------------------------------")
print("LOG")
print("-------------------------------")

time.sleep(30)

while True:
    print("bounty rune notification on:  " +format(datetime.datetime.now()))
    notification.notify(
        title='Bounty Runes',
        message='Bounty Runes spawning soon',
        app_icon='BR.ico', 
        timeout=5, 
    )
    time.sleep(300)
