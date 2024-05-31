WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHTGRAY = (200, 200, 200)
GRAY = (127, 127, 127)
DARKGRAY = (50, 50, 50)
BLUE = (0, 0, 255)

BACKGROUND = LIGHTGRAY

color = {
    '_': LIGHTGRAY,
    '=': GRAY,
    '.': WHITE,
    '@': BLACK,
    '#': DARKGRAY,
    ' ': BACKGROUND,
}
inverter = {
    '_': '=',
    '=': '_',
    '.': '@',
    '@': '.',
}
