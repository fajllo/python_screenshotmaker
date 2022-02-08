


import datetime

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageDraw, ImageFont
import pyscreenshot


def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result


def screenshot():
    try:

        name = inp.get() + ".png"

        image = pyscreenshot.grab(bbox=(0, 0, 1920, 1040))
        image.save(f'{name}')
        im = Image.open(name).convert('RGBA')
        im_new = add_margin(im, 0, 0, 40, 0, (0, 0, 0))
        base = im_new
        txt = Image.new('RGBA', base.size, (0, 0, 0, 1))
        fnt = ImageFont.truetype('C:\\Windows\\Fonts\\ARIALN.TTF', size=28)
        _, y = base.size
        d = ImageDraw.Draw(txt)
        date_time = datetime.datetime.now().strftime("%H:%M:%S %m/%d/%Y")
        d.text((0, y - 35), date_time, font=fnt, fill=(255, 240, 0, 1000))
        out = Image.alpha_composite(base, txt)

        out.save(f'{name}')
        print(f"success: {name}")

    except Exception as e:
        print(e)


root = Tk()
frm = ttk.Frame(root, padding=20)
frm.grid()
ttk.Label(frm, text="Take a screenshot").grid(column=0, row=0)
inp = Entry(root)
inp.grid(columnspan=2,row=1,pady=10)
ttk.Button(frm, text="Smile 😂", command=screenshot).grid(column=1, row=0)
root.mainloop()
