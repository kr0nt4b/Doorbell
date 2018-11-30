from DebouncedSwitch import DebouncedSwitch
from machine import Pin
from DebouncedSwitch import DebouncedSwitch
from umqtt.robust import MQTTClient

c = MQTTClient("umqtt_client", "192.168.1.135")


def meter_tick_callback(arg):
    c.publish(b"domoticz/in", "{ \"idx\" : %s, \"nvalue\" : 0, \"svalue\" : \"1\" }" % arg)


def sub_cb(topic, msg): pass


def setup():
    DebouncedSwitch(Pin(14, Pin.IN), meter_tick_callback, 61)

    c.set_callback(sub_cb)
    if not c.connect(clean_session=False):
        print("New session being set up")


setup()


while True:
    pass
