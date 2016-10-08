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
    return get(server + url)


def read_notifications():
    notifications = github_request('/notifications?per_page=1')
    issues = github_request('/issues?per_page=1')
    print(notifications)
    print(issues)
    return notifications, issues


def light_from(notifications, issues):
    notifications = min(notifications, 63)
    issues = min(issues, 63)
    print(notifications)
    print(issues)
    light_state = []
    for x in range(6):
        if notifications % 2 == 1.0:
            light_state.append(lights.GREEN)
        else:
            light_state.append(lights.WHITE)
        notifications = int(notifications/2)
    for x in range(6):
        if issues % 2 == 1.0:
            light_state.append(lights.RED)
        else:
            light_state.append(lights.WHITE)
        issues = int(issues/2)
    print(light_state)
    return light_state
    

def update_lights(light_state):
    lights.send_color(light_state)
    return True


setup_network()
# while True:
if 1:
    light_state = light_from(*read_notifications())
    update_lights(light_state)
