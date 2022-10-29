import time
from PoEsTaT import screen
from PIL import Image

im = screen.getPart(1000, 400)

sqarray = screen.getSquares(50, 79, 11, 70, 70, im, n=6)
for n in sqarray:
    n.show()
    time.sleep(0.5)

img = Image.open(r"C:\Users\squabbitunited\PycharmProjects\pythonProject\PoEsTaT\dat\Purity_of_Elements_skill_icon.webp")
