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
    mmheight = 15
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


#
# class NorwegianRapport():
#
#     def createReport(self):
#         canvas = Canvas(f"test.pdf", pagesize=A4)
#         canvas.setTitle("Provsvar")
#         # canvas.setFont("Helvetica-Oblique", 11.5)
#         # canvas.drawString(1 * cm, 29 * cm, date_formatted)
#         textobject = canvas.beginText()
#         textobject.setTextOrigin(2 * cm, 26.1 * cm, )
#         # textobject.setFont("Helvetica-Oblique", 14)
#         textobject.setFont("Helvetica-Bold", 26.1)
#         # textobject.setFont("Arial", 26.1)
#         textobject.textLine("CORONA / COVID-19 TEST RESULT")
#         textobject.setTextOrigin(2 * cm, 25.5 * cm, )
#         textobject.setFont("Helvetica", 13.9)
#         canvas.line(2 * cm, 17.4 * cm, 12.3 * cm, 17.4 * cm)
#         canvas.line(2 * cm, 13.3 * cm, 2 * cm, 17.4 * cm)
#
#         canvas.setStrokeColorRGB(0.8, 0.8, 0.8)
#
#
#         textobject.setFillColorRGB(0, 0, 0)
#         textobject.setTextOrigin(2.45 * cm, 16.5 * cm, )
#         textobject.setFont("Helvetica-Bold", 13.7)
#         textobject.textLines("Analysis / Analyse:")
#         textobject.setTextOrigin(2.45 * cm, 15.85 * cm, )
#         textobject.setFont("Helvetica", 13.7)
#         textobject.textLines(f"""Us-SARS-relatert koronavirus (inkl. SARS-
#             CoV-2) RNA""")
#         textobject.setTextOrigin(2.45 * cm, 14.6 * cm, )
#         textobject.setFont("Helvetica-Bold", 13.7)
#         textobject.textLines("Result / Resultat:")
#
#         canvas.drawText(textobject)
#         canvas.showPage()
#         canvas.save()





# """ Setting up the main pathing """
# this_dir, this_filename = os.path.split(__file__)
# GRAPHICS_PATH = os.path.join(this_dir, "graphics/climacons/")
# images = convert_from_path('example.pdf', 50)
#
#
#
# for image in images:
#     image.save('output.png')





# if __name__ == '__main__':
#     rapport = NorwegianRapport()
#     rapport.person_name = "Alajeva Malika Mutalijevna"
#     rapport.person_number = "17015823429"
#     rapport.date = '30.04.2021'
#     rapport.count = 7
#     rapport.createReport()

create_report()