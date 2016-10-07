import machine
import neopixel
from time import sleep


led_count = 12
np = neopixel.NeoPixel(machine.Pin(4), led_count)

# Colors

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
FUCSHIA = (255, 0, 255)
GREEN = (0, 255, 0)
MAGENTA = (0, 255, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GITHUB_BLUE = (141, 200, 232)


def send_color(color_array):
    for i in len(color_array):
        np[i] = color_array[i]
    np.write()


def turn_off():
    send_color(static_plain(BLACK))


def static_plain(color):
    return [color for i in range(led_count)]


def static_alternate(color1, color2):
    data = [color1 for i in range(led_count)]
    for i in range(led_count):
        if i % 2:
            data[i] = color2
    return data


# def static_gradient(color1, color2):
#     diff = ((color2[0] - color1[0])/led_count, (color2[1] - color1[1])/led_count, (color2[2] - color1[2])/led_count)
#     data = []
#     for i in range(led_count):
#         data[i] = color1 + diff * i
#     return data


def list_rotate(lst):
    copy = list(lst)
    for i in range(len(lst)):
        lst[i] = copy[i-1]
    return lst


def rotate(ring_color_data, led_count=led_count, rotations=5):
    data = ring_color_data
    for i in led_count * rotations:
        send_color(data)
        data = list_rotate(data)
        sleep(0.5)


def blink(color, times=20):
    for i in range(times):
        send_color(static_plain(color))
        sleep(0.5)
        turn_off()
        sleep(0.5)

c = static_alternate(RED, GREEN)
send_color(c)
sleep(1)
rotate(c)
turn_off()
blink(GITHUB_BLUE)
