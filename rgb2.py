import board
import neopixel

pixel = neopixel.NeoPixel(board.D18, 1, pixel_order=neopixel.RGBW)
pixel[0] = (30, 0, 20, 10)