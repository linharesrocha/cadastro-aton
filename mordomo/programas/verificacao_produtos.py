from mordomo.main import *
from mordomo.auxiliar import *
import pandas as pd


# Verificar se todas descrições estão no padrão

dados = pd.read_excel('excel/confere_descricao.xls')
pd.set_option('mode.chained_assignment', None)
# Você precisa entrar no cadastro de produtos
consultar_produtos_opcao_todos()
consultar_produtos_menu_cod_id()

tamanho_planinha = len(dados)


for i in range(tamanho_planinha):
    print(str(i) + '/' + str(tamanho_planinha) + ' -- ' + dados['Descrição'][i])
    print(' ')
    consultar_produtos_pesquisa()
    pyperclip.copy(dados['Código Interno'][0])
    pg.hotkey('ctrl', 'v')
    consultar_produtos_botao_consultar()
    consultar_produtos_select_resultado()
    cadastro_produtos_botao_alterar()
    cadastro_produtos_descricao()
    pg.moveTo(2947, 980)
    pg.click()

    # Titulo
    titulo = input('Há título no início da descricão? (SIM / S): ')
    titulo = titulo.upper()
    if titulo == 'S' or titulo == 'SIM':
        dados['Titulo'][i] = 'Consertar'
    else:
        dados['Titulo'][i] = 'OK'

    # Segurança
    seguranca = input('Breve texto indicando segurança e envio imediato? (SIM / S): ')
    seguranca = seguranca.upper()
    if seguranca == 'S' or seguranca == 'SIM':
        dados['Seguranca'][i] = 'Consertar'
    else:
        dados['Seguranca'][i] = 'OK'

    # Persuadir
    persuadir = input('Texto descrevendo o produto com intuito de persuadir o cliente com palavras chaves do título e '
                      'do nicho? (SIM / S): ')
    persuadir = persuadir.upper()
    if persuadir == 'S' or persuadir == 'SIM':
        dados['Persuadir'][i] = 'Consertar'
    else:
        dados['Persuadir'][i] = 'OK'

    # Recomendacoes
    recomendacoes = input('Recomendações de uso, fazendo perguntas e respondendo Por que Compra? (SIM / S): ')
    recomendacoes = recomendacoes.upper()
    if recomendacoes == 'S' or recomendacoes == 'SIM':
        dados['Recomendacoes'][i] = 'Consertar'
    else:
        dados['Recomendacoes'][i] = 'OK'

    # Especificacao
    especificacao = input('Especificações Técnicas? (SIM / S): ')
    especificacao = especificacao.upper()
    if especificacao == 'S' or especificacao == 'SIM':
        dados['Especificacao'][i] = 'Consertar'
    else:
        dados['Especificacao'][i] = 'OK'

    # Marca Empresa
    marcaEmpresa = input('Frase curta descrevendo a marca da empresa persuadindo o cliente? (SIM / S): ')
    marcaEmpresa = marcaEmpresa.upper()
    if marcaEmpresa == 'S' or marcaEmpresa == 'SIM':
        dados['MarcaEmpresa'][i] = 'Consertar'
    else:
        dados['MarcaEmpresa'][i] = 'OK'

    # Incentivar
    incentivar = input('Incentivar o cliente a chamar no chat e colocar no carrinho para adquirir promoções e '
                       'descontos excludivos? (SIM / S): ')
    incentivar = incentivar.upper()
    if incentivar == 'S' or incentivar == 'SIM':
        dados['Incentivar'][i] = 'Consertar'
    else:
        dados['Incentivar'][i] = 'OK'

    dados.to_excel('confere_descricao_check.xlsx', index=False)

    # Consultar outro produto
    cadastro_produtos_botao_salvar()
    cadastro_produtos_botao_consultar()