def notas(*nots, sit=False):
    """
    -> Função para analisar a nota e situação de vários alunos.
    :param nots: Uma ou mais notas dos alunos (aceita várias).
    :param sit: situação do aluno (opcional).
    :return: retorna um dicionário com todas as informações da turma.
    """
    nota = dict()
    aluno = list()
    sm = 0
    nota['total'] = len(nots)
    nota['maior'] = max(nots)
    nota['menor'] = min(nots)
    for c in nots:
        sm += c
    m = sm / len(nots)
    nota['média'] = f'{m:.1f}'
    if sit:
        if m >= 7:
            nota['situação'] = 'APROVADO'
        elif 7 > m >= 5:
            nota['situação'] = 'RECUPERAÇÃO'
        else:
            nota['situação'] = 'REPROVADO'
    aluno.append(nota.copy())
    return aluno


resp = notas(5.0, 6.5, 10, 6.5, sit=True)
print(resp)
help(notas)
