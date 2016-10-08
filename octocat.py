# -*- coding: utf-8 -*-
""" Octocat Signal
"""

import machine, neopixel
import network
import ujson

from client import get

import config
import lights


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
    if light_state:
        lights.send_color([lights.WHITE])
    else:
        lights.turn_off()
    return True


setup_network()
# while True:
if 1:
    light_state = []
    for notification in read_notifications():
        light_state.append(light_from(notification))
    update_lights(light_state)
