from Tkinter import Tk
from tkFileDialog import askopenfilename
from PIL import Image, ImageFont, ImageDraw
import subprocess

def main():
    """ Adds name and DOB to upper left hand corner of JPG"""
    name = raw_input("Please enter the name: ")
    dob = raw_input("Please enter the DOB: ")
    font = ImageFont.truetype("arial.ttf", 48)
    Tk().withdraw()
    image = askopenfilename()
    img = Image.open(image)
    img = img.rotate(180)
    draw = ImageDraw.Draw(img)
    draw.text((0, 10), name, (0, 0, 0), font=font)
    draw.text((0, 60), dob, (0, 0, 0), font=font)
    img.save('c:/~output/' + name + '.jpg')
    subprocess.Popen('explorer "c:\~output"')

if __name__ == "__main__":
    main()

