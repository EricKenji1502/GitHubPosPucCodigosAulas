import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import ocorrencias as oc

engine = sa.create_engine('sqlite:///C:\\Users\\erick\\Desktop\\GitHubPosPUC\\CodigosAulas\\Bancodedadosrelacional\\ORM\\BD\\ocorrencias.db')
Sessao = orm.sessionmaker(bind=engine)
sessao = Sessao()

RankMunic = sessao.query(
    oc.municipio.municipio.label('Municipio'),
    sa.func.sum(oc.ocorrencia.qtde).label('Total')
).join(
    oc.ocorrencia,
    oc.ocorrencia.codIBGE == oc.municipio.codIBGE
).where(
oc.ocorrencia.ocorrencia == 'roubo_veiculo'
).group_by(
    oc.municipio.municipio
).order_by(
    sa.func.sum(oc.ocorrencia.qtde).desc()
).all()
print(RankMunic)