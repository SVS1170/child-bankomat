import urllib
import json
import time
import os
from pdf2image import convert_from_path
from PIL import Image, ImageDraw, ImageFont
import reportlab
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas


import datetime
import qrcode
import random

APP_DIR = os.path.dirname(os.path.realpath(__file__))


def register_fonts():
    reportlab.rl_config.TTFSearchPath.append(os.path.join(APP_DIR, "fonts/"))
    pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
    pdfmetrics.registerFont(TTFont('Raleway_BlackItalic', 'Raleway-BlackItalic.ttf'))
    pdfmetrics.registerFont(TTFont('Raleway_Black', 'Raleway-Black.ttf'))
    pdfmetrics.registerFont(TTFont('Raleway_Bold', 'Raleway-Bold.ttf'))
    pdfmetrics.registerFont(TTFont('Raleway_SemiBold', 'Raleway-SemiBold.ttf'))
    pdfmetrics.registerFont(TTFont('Raleway_Italic', 'Raleway-Italic.ttf'))
    pdfmetrics.registerFont(TTFont('Raleway_Medium', 'Raleway-Medium.ttf'))
    pdfmetrics.registerFont(TTFont('Raleway_Regular', 'Raleway-Regular.ttf'))

    return 0


register_fonts()

# Create an image with 300DPI, 58mm by 150mm.
def create_report():
    dpi = 165
    mmwidth = 58
    mmheight = 150
    pixwidth = int(mmwidth / 25.4 * dpi)
    pixheight = int(mmheight / 25.4 * dpi)
    im = Image.new("RGB", (pixwidth, pixheight), "white")
    dr = ImageDraw.Draw(im)
    dr.text((10, 10), "I should be 150mm x 105mm ", fill="black")
    im.save("safaripdf.png", dpi=(dpi, dpi))

    # Create a PDF with a page that just fits the image we've created.
    pagesize = (58*mm, 150*mm)
    c = reportlab.pdfgen.canvas.Canvas("safaripdf.pdf", pagesize=pagesize)
    c.scale(0.24, 0.24) # Scale so that the image exactly fits the canvas.
    c.drawImage("safaripdf.png", 0, 0) # , width=pixwidth, height=pixheight)

    c.showPage()
    c.save()



create_report()
