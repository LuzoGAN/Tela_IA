import pandas as pd
from sqlalchemy import create_engine
import win32com.client as client
import datetime as dt

outlook = client.Dispatch('Outlook.Application')
emissor = outlook.session.Accounts['luzo.neto@sicoob.com.br']
hoje = dt.datetime.now()



emails = pd.read_sql_table('TB_DIM_FOLHA_COLABORADOR', engine, columns=["cpf", "login"])
emails['cpf'] = emails['cpf'].astype('int64')

consorcio = pd.read_excel(r"C:\Users\luzo.neto\Downloads\Diario - Consorcio Completa.xlsx")
consorcio.rename(columns={'CPF_CNPJ_Vendedor': 'cpf'}, inplace=True)

#consorcio = consorcio[(consorcio['Data_Limite_Pagamento'] >= hoje) & (consorcio['Valor_Total_Pago_Cota'] > 0)]

final = pd.merge(consorcio, emails, how='left', on='cpf')
#final['login'] = final['login'] + '@sicoob.com.br'
final['login'] = 'gleuton.trindade@sicoob.com.br'

dados = final[['login','CPF_CNPJ','Numero_Contrato','Numero_Cota','Numero_Cota','Segmento_Consorcio','Data_Adesao','Data_Limite_Pagamento','Nome Cliente']].values.tolist()
def rodar():
    for dado in dados:
        destinatario = dado[0]

        nome_coperado = dado[8]
        cpf_cnpj = dado[1]
        contrato = dado[2]
        grupo = dado[3]
        cota = dado[4]
        segmento = dado[5]
        data_adesao = dado[6]
        data_limite = dado[7]

        mensagem = outlook.CreateItem(0)
        # mensagem.Display()
        mensagem.To = destinatario
        mensagem.Subject = 'Aviso Importante: Não Identificação de Pagamento do Boleto de Adesão - CONSÓRCIO'
        corpo_mensagem = f'''
    
        Aviso Importante: Não Identificação de Pagamento do Boleto de Adesão - CONSÓRCIO
        Prezado(a) Gerentes,
        Gostaríamos de informar que, conforme o fluxo estabelecido, o prazo para pagamento do boleto de adesão da cota comercializada é de 3 dias úteis a partir da data de aquisição. Até o momento, não identificamos o pagamento correspondente ao seu boleto/parcela de adesão, do consorciado relacionado abaixo:
        Nome cooperado – CPF/CNPJ – Contrato – Grupo – Cota – Segmento – Data de adesão – data limite de pagamento
        {nome_coperado} | {cpf_cnpj} | {contrato} | {grupo} | {cota} | {segmento} | {data_adesao} | {data_limite}
        Por favor, este comunicado é dirigido a você gerente no intuito de lembrar o consorciado do pagamento da cota de consórcio, evitando o cancelamento desta. Caso o pagamento já tenha sido realizado pelo consorciado, desconsiderar este comunicado.
        Lembramos que, após o pagamento do boleto de adesão, é necessário formalizar a venda dentro da plataforma GED para que possamos processar sua adesão de forma adequada e garantir a continuidade do seu processo de consórcio.
        Caso ainda não tenha efetuado o pagamento, solicitamos que o faça dentro do prazo estipulado para evitar quaisquer inconvenientes ou interrupções na contratação da cota.
        Agradecemos a sua atenção e cooperação.
        Atenciosamente,
        Equipe de Consórcios
        Superintendência de Produtos e Serviços
    
        '''
        mensagem.Body = corpo_mensagem
        mensagem._oleobj_.Invoke(*(64209, 0, 8, 0, emissor))
        mensagem.Save()
        mensagem.Send()

rodar()