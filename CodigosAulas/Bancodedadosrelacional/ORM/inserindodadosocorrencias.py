import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import ocorrencias as oc

#Modificar de acordo com seu PC
endereco = "C:\\Users\\erick\\Desktop\\GitHubPosPUC\\CodigosAulas\\Bancodedadosrelacional\\Dados\\Exercício"

dp = pd.read_csv(endereco + "\\DP.csv", sep=",")
responsavelDP = pd.read_excel(endereco + "\\ResponsavelDP.xlsx")
municipio = pd.read_csv(endereco + "\\Municipio.csv", sep=",")
ocorrencias = pd.read_excel(endereco + "\\ocorrencias.xlsx")

engine = sa.create_engine("sqlite:///C:\\Users\\erick\\Desktop\\GitHubPosPUC\\CodigosAulas\\Bancodedadosrelacional\\ORM\\BD\\ocorrencias.db")
Sessao = orm.sessionmaker(bind=engine)
sessao = Sessao()

#DP
DadosDP = dp.to_dict(orient="records")
tabela_DP = oc.dp.__table__
try:
    sessao.execute(tabela_DP.insert(), DadosDP)
    sessao.commit()
    print("Dados de DP inseridos com sucesso!")
except ValueError:
    ValueError()

#ResponsavelDP
DadosRespDP = responsavelDP.to_dict(orient="records")
tabela_respDP = oc.reponsaveldp.__table__

try:
    sessao.execute(tabela_respDP.insert(), DadosRespDP)
    sessao.commit()
    print("Dados de Responsável DP inseridos com sucesso!")
except ValueError:
    ValueError()

#MunicipioDP
DadosMunicipio = municipio.to_dict(orient="records")
tabela_municipio = oc.municipio.__table__
try:
    sessao.execute(tabela_municipio.insert(), DadosMunicipio)
    sessao.commit()
    print("Dados de Município inseridos com sucesso!")
except ValueError:
    ValueError()

#Ocorrencias
DadosOcorrencia = ocorrencias.to_dict(orient="records")
tabela_ocorrencia = oc.ocorrencia
try:
    sessao.execute(tabela_ocorrencia.__table__.insert(), DadosOcorrencia)
    sessao.commit()
    print("Dados de Ocorrências inseridos com sucesso!")
except ValueError:
    ValueError()

sessao.close()
print("Sessão encerrada com sucesso!")