import sys
import time
sys.path.append('/usr/local/lib/python3.7/site-packages')

from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback
from pubnub.pubnub import PubNub

from gpiozero import LED
from time import sleep

SUBSCRIBE_KEY = 'sub-c-fee6fbae-4fb6-11ea-80a4-42690e175160'
PUBLISH_KEY = 'pub-c-ac3f9dde-c7c3-4c3c-8ea1-b90ca3c38521'
CHANNEL = 'messages'

# Setting up PubNub
pnconfig = PNConfiguration()
pnconfig.subscribe_key = SUBSCRIBE_KEY
pnconfig.publish_key = PUBLISH_KEY
pubnub = PubNub(pnconfig)

pubnub.add_listener(SubscribeCallback())
pubnub.subscribe().channels(CHANNEL).execute()

led = LED(21) # initlize the LED on pin 21

class SubscribeCallback(SubscribeCallback):
    def message(self, pubnub, message):
        print('Received message: %', message.message)

        if message.message == 'blink':
            blink()

        # Handle other messages..
        # ..

def blink():
    print('I should blink.')
    led.on()  # turn on the led
    sleep(1)  # then wait 1 second
    led.off() # then turn it off