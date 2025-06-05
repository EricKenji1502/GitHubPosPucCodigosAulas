import sqlalchemy as sa
import ocorrencias as oc

engine = sa.create_engine("sqlite:///CodigosAulas\\Bancodedadosrelacional\\ORM\\BD\\ocorrencias.db")

metadata = sa.MetaData()
sa.MetaData.reflect(metadata, bind=engine)

tbMunicipio = metadata.tables[oc.municipio.__tablename__]

atualiza_regiao = sa.update(tbMunicipio).values(
    {"regiao":"Capital"}
).where(
    tbMunicipio.c.municipio == "Rio de Janeiro"
)

try:
    with engine.connect() as conn:
        conn.execute(atualiza_regiao)
        conn.commit()
    print("Dados atualizados com sucesso!")
except ValueError:
    ValueError()