class DeskSetUp:
    """An object to define the desk setup in a room"""
    __slots__ = "_monitor", "_mouse", "_keyboard", "_laptop", "_speaker", "_headset"

    def __init__(self, monitor, mouse, keyboard, laptop, speaker, headset):
        self._monitor = monitor
        self._mouse = mouse
        self._keyboard = keyboard
        self._laptop = laptop
        self._speaker = speaker
        self._headset = headset
        print(vars())


import copy

warmtones = [[0], [1]]
pallet = copy.copy(warmtones)

pallet.append(2)
pallet[0].append(1)

print(warmtones)
print(pallet)
