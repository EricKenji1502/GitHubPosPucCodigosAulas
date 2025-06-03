import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import ocorrencias as oc

engine = sa.create_engine('sqlite:///C:\\Users\\erick\\Desktop\\GitHubPosPUC\\CodigosAulas\\Bancodedadosrelacional\\ORM\\BD\\ocorrencias.db')
Sessao = orm.sessionmaker(bind=engine)
sessao = Sessao()

RankDP = sessao.query(
    oc.dp.nome.label('Dp'),
    sa.func.sum(oc.ocorrencia.qtde).label('Total')
).join(
    oc.ocorrencia,
    oc.ocorrencia.codDP == oc.dp.codDP
).join(
    oc.municipio,
    oc.ocorrencia.codIBGE == oc.municipio.codIBGE
).where(
    oc.municipio.regiao == 'Capital'
).group_by(
    oc.dp.nome
).order_by(
    sa.func.sum(oc.ocorrencia.qtde).desc()
).all()

print(RankDP)