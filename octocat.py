# -*- coding: utf-8 -*-
""" Octocat Signal
"""

import machine, neopixel
import network
import ujson

from client import get

import config


def setup_network():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('PixelsCamp', 'IamAPixelCamper')
    while not sta_if.isconnected():
        pass
    print(sta_if.ifconfig())


def github_request(url, data=None):
    server = 'http://silvaneves.org/proxy/index.php?https://api.github.com'
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, compress',
        'User-Agent': 'Octocat-Signal/1.0',
    }
    print(server + url)
    return get(server + url)


def read_notifications():
    return ujson.loads(github_request('/notifications?per_page=1'))


def light_from(notification):
    return {}


def update_lights(light_state):
    np = neopixel.NeoPixel(machine.Pin(4), 12)
    np[len(light_state) % 12] = (255, 0, 0)
    return True


setup_network()
# while True:
if 1:
    lights = []
    for notification in read_notifications():
        lights.append(light_from(notification))
    update_lights(lights)
