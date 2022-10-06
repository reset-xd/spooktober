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

def h3(avatar):
    mask = Image.open("./assets/h3_mask.png").resize((500, 500))
    base = Image.open("./assets/h3.png")
    base.paste(avatar.resize(mask.size), (0, 0), mask.convert("L"))

    a = randint(0,50)
    base.save(f"./trash/{a}.png")
    return a


def h4(avatar):
    images = [avatar.copy()]

    base = Image.open("./0_mask.gif").resize(avatar.size)
    mask = Image.open("./0.gif").resize(avatar.size)
    new = avatar.copy()
    new.paste(mask, (0, 0), base.convert("L"))

    images.append(new)

    new = avatar.copy()
    mask = Image.open("./1.gif").resize(avatar.size)
    new.paste(mask, (0, 0), base.convert("L"))


    new = avatar.copy()
    mask = Image.open("./2.gif").resize(avatar.size)
    new.paste(mask, (0, 0), base.convert("L"))

    images.append(new)
    images.append(Image.new("RGB", avatar.size, (0, 0, 0)))
    a = randint(0,50)
    images[0].save(f"./damn.gif", save_all=True, append_images=images[1:], optimized=False, duration=80, loop=False)
    return a

h4(Image.open("./avatar.png"))