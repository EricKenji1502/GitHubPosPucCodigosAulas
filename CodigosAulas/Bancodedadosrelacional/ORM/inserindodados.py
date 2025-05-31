import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import vendas as vd

endereco = "C:\\Users\\erick\\Desktop\\GitHubPosPUC\\CodigosAulas\\Bancodedadosrelacional\\Dados\\Exemplo"

vendedor = pd.read_csv(endereco + "\\vendedor.csv", sep=";")


engine = sa.create_engine("sqlite:///vendas.db")

Sessao = orm.sessionmaker(bind=engine)
sessao = Sessao()

#tbVendedor
for i in range(len(vendedor)):
    dados_vendedor = vd.Vendedor(
        registro_vendedor=vendedor["registro_vendedor"][i],
        cpf=vendedor["cpf"][i],
        nome=vendedor["nome"][i],
        genero=vendedor["genero"][i],
        email=vendedor["email"][i]
    )
    try:
        sessao.add(dados_vendedor)
        sessao.commit()
        print("Dado inseridos com sucesso!")
    except FileNotFoundError:
        print(f"ERRO FATAL: Arquivo de vendedores não encontrado em {endereco + "\\vendedor.csv"}")
        if sessao.is_active: sessao.rollback()
    except KeyError as ke:
        print(f"ERRO de KeyError ao processar VENDEDORES (provavelmente nome de coluna errado no CSV ou no acesso ao DataFrame): {ke}")
        if sessao.is_active: sessao.rollback()
    except Exception as e:
        print(f"ERRO GERAL ao processar dados de VENDEDORES: {e}")
        if hasattr(e, 'orig'): print(f"  Detalhe DB: {e.orig}")
        if sessao.is_active: sessao.rollback()

#tbProduto
produto = pd.read_excel(endereco + "\\produto.xlsx")
DadosProduto = produto.to_dict(orient="records")
tabela_produto = vd.Produto.__table__

try:
    sessao.execute(tabela_produto.insert(), DadosProduto)
    sessao.commit()
    print("Dados inseridos com sucesso!")
except FileNotFoundError:
    print(f"ERRO FATAL: Arquivo de produtos não encontrado em {endereco + "\\vendedor.csv"}")
    if sessao.is_active: sessao.rollback()
except ValueError as ve: # Captura o ValueError da verificação de colunas
    print(f"ERRO DE VALOR (provavelmente coluna faltando) ao processar PRODUTOS: {ve}")
    if sessao.is_active: sessao.rollback()
except Exception as e:
    print(f"ERRO GERAL ao inserir dados de PRODUTOS: {e}")
    if hasattr(e, 'orig'):
        print(f"  Detalhe do erro original do DB: {e.orig}")
    if sessao.is_active: sessao.rollback()
finally:
    if sessao.is_active:
        sessao.close()
        print("Sessão fechada.")

sessao.close()