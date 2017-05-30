from reportlab.pdfgen import canvas

c = canvas.Canvas("sample.pdf")
c.rect(55, 575, 220, 220, 1)
c.drawString(70, 770, "POF-861")
c.drawString(250, 770, "5")
c.drawString(75, 720, "WWWWWWWWWWWWWWW")
c.rect(325, 575, 220, 220, 1)
c.rect(55, 325, 220, 220, 1)
c.rect(325, 325, 220, 220, 1)
c.rect(55, 75, 220, 220, 1)
c.rect(325, 75, 220, 220, 1)
c.save()