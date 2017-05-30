# coding: utf-8

from reportlab.pdfgen import canvas
from issue import Issue

issue1 = Issue('POF-861', 8, 'Tela: Fornecer Dados Veículo')
issue2 = Issue('POF-862', 8, 'Refatorar o código')
lista = Issue.get_all_issues(issue1, issue2)

print lista[0].title

c = canvas.Canvas("sample.pdf")
c.rect(55, 575, 220, 220, 1)
c.drawString(70, 770, str(lista[0].title))
c.drawString(250, 770, str(lista[0].points))
c.drawString(75, 720, str(lista[0].desc))
c.rect(325, 575, 220, 220, 1)
c.rect(55, 325, 220, 220, 1)
c.rect(325, 325, 220, 220, 1)
c.rect(55, 75, 220, 220, 1)
c.rect(325, 75, 220, 220, 1)
c.showPage()
c.rect(55, 575, 220, 220, 1)
c.drawString(70, 770, str(lista[0].title))
c.drawString(250, 770, str(lista[0].points))
c.drawString(75, 720, str(lista[0].desc))
c.rect(325, 575, 220, 220, 1)
c.rect(55, 325, 220, 220, 1)
c.rect(325, 325, 220, 220, 1)
c.rect(55, 75, 220, 220, 1)
c.rect(325, 75, 220, 220, 1)
c.save()