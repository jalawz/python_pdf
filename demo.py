# coding: utf-8

from reportlab.pdfgen import canvas
from reportlab.lib.colors import PCMYKColor, PCMYKColorSep, Color, black, blue, green, red, lightgrey


c = canvas.Canvas("sample.pdf")

c.setStrokeColor(lightgrey, alpha=None)
c.rect(55, 575, 220, 220, 1)
c.rect(325, 575, 220, 220, 1)
c.rect(55, 325, 220, 220, 1)
c.rect(325, 325, 220, 220, 1)
c.rect(55, 75, 220, 220, 1)
c.rect(325, 75, 220, 220, 1)

c.save()
