import sqlalchemy as sa
import sqlalchemy.orm as orm

engine = sa.create_engine("sqlite:///C:\\Users\\erick\\Desktop\\GitHubPosPUC\\CodigosAulas\\Bancodedadosrelacional\\ORM\\BD\\ocorrencias.db")
base = orm.declarative_base()

class dp(base):
    __tablename__ = "tbDP"

    codDP = sa.Column(sa.Integer, primary_key=True, index=True)
    nome = sa.Column(sa.VARCHAR(100), nullable=False)
    endereco = sa.Column(sa.VARCHAR(255), nullable=False)

class reponsaveldp(base):
    __tablename__ = "tbResponsavelDP"

    codDP = sa.Column(sa.Integer, primary_key=True, index=True)
    delegado = sa.Column(sa.VARCHAR(100), nullable=False)

class municipio(base):
    __tablename__ = "tbMunicipio"

    codIBGE = sa.Column(sa.Integer, primary_key=True, index=True)
    municipio = sa.Column(sa.VARCHAR(100), nullable=False)
    regiao = sa.Column(sa.VARCHAR(25), nullable=False)

class ocorrencia(base):
    __tablename__ = "tbOcorrencia"

    idRegistro = sa.Column(sa.Integer, primary_key=True, index=True)
    codDP = sa.Column(sa.Integer, sa.ForeignKey("tbDP.codDP", ondelete="no action", onupdate="cascade"), index=True)
    codIBGE = sa.Column(sa.Integer, sa.ForeignKey("tbMunicipio.codIBGE", ondelete="no action", onupdate="cascade"), index=True)
    ano = sa.Column(sa.CHAR(4), nullable=False)
    mes = sa.Column(sa.CHAR(2), nullable=False)
    ocorrencia = sa.Column(sa.VARCHAR(100), nullable=False)
    qtde = sa.Column(sa.Integer, nullable=False)

try:
    base.metadata.create_all(engine)
except Exception as e:
    print(f"Erro ao criar tabelas: {e}")
    




