import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

keyboard.matrix = KeysScanner(
    pins=[
        board.D2,  # SW3  - lewo
        board.D3,  # SW11 - dół
        board.D7,  # SW12 - prawo
        board.D4,  # SW4  - góra
    ],
    value_when_pressed=False,
    pull=True,
)

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# (pin A, pin B, pin przycisku, odwrócony kierunek)
encoder_handler.pins = ((board.D0, board.D1, board.D5, False),)

keyboard.keymap = [
    [KC.LEFT, KC.DOWN, KC.RIGHT, KC.UP],
]

# obrót w lewo = ciszej, w prawo = głośniej, wciśnięcie = wyciszenie
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE),),
]

if __name__ == '__main__':
    keyboard.go()