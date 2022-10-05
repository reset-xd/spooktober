from PIL import Image
from random import randint

def h1(avatar):
    mask = Image.open("./assets/h1_mask.png").resize((201, 201))
    base = Image.open("./assets/h1.png")
    base.paste(avatar.resize(mask.size), (80, 122), mask.convert("L"))

    a = randint(0,50)
    base.save(f"./trash/{a}.png")
    return a

def h2(avatar):
    mask = Image.open("./assets/h2_mask.jpg").resize((497, 497))
    base = Image.open("./assets/h2.png")
    base.paste(avatar.resize(mask.size), (72, 55), mask.convert("L"))

    a = randint(0,50)
    base.save(f"./trash/{a}.png")
    return a