# coding: utf-8

from issue import Issue

issue1 = Issue('POF-861', 8, 'Tela: Fornecer Dados Veículo')
issue2 = Issue('POF-862', 5, 'Refatorar Métodos')

issues = [issue1, issue2]

test = Issue.get_all_issues(issues)

print test[0].title
