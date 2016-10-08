# -*- coding: utf-8 -*-
""" Octocat Signal
"""

import network
from time import sleep
from client import get

from lights import blink, send_color, static_gradient, pulse, static_plain, static_alternate
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
    return get(server + url)


def read_notifications():
    notification = github_request('/notifications?per_page=1')
    print(notification)
    return notification


def light_from(notification):
    if notification == "PullRequest":
        blink(lights.YELLOW)
    elif notification == "Issue":
        blink(lights.RED)
    else:
        send_color(static_plain(lights.GITHUB_BLUE))


setup_network()
rotate(static_alternate(lights.GITHUB_BLUE, lights.BLUE))
while True:
    light_from(read_notifications())
    sleep(60)
