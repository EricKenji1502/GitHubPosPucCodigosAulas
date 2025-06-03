import sqlalchemy as sa
import sqlalchemy.orm as orm

engine = sa.create_engine("sqlite:///C:\\Users\\erick\\Desktop\\GitHubPosPUC\\CodigosAulas\\Bancodedadosrelacional\\ORM\\BD\\vendas.db")
base = orm.declarative_base()

#Tabela de Clientes
class Cliente(base):
    __tablename__ = "cliente"
    
    cpf = sa.Column(sa.CHAR(14), primary_key=True, index=True)
    nome = sa.Column(sa.VARCHAR(100), nullable=False)
    email = sa.Column(sa.VARCHAR(50), nullable=False, unique=True)
    genero = sa.Column(sa.VARCHAR(1))
    salario = sa.Column(sa.DECIMAL(10,2), nullable=False)
    dia_mes_aniversario = sa.Column(sa.CHAR(5), nullable=False)
    bairro = sa.Column(sa.VARCHAR(50))
    cidade = sa.Column(sa.CHAR(50))
    uf = sa.Column(sa.CHAR(2))

#Tabela de Fornecedores

class Fornecedor(base):
    __tablename__ = "fornecedor"
    
    registro = sa.Column(sa.INTEGER, primary_key=True, index=True)
    nome_fantasia = sa.Column(sa.VARCHAR(50), nullable=False)
    razao_social = sa.Column(sa.VARCHAR(100), nullable=False)
    cidade = sa.Column(sa.VARCHAR(50))
    uf = sa.Column(sa.CHAR(2))

#Tabela de Produtos

class Produto(base):
    __tablename__ = "produto"
    
    codBarras = sa.Column(sa.Integer, primary_key=True, index=True)
    registro = sa.Column(sa.Integer, sa.ForeignKey("fornecedor.registro", ondelete="no action", onupdate="cascade"), index=True)
    dscProduto = sa.Column(sa.VARCHAR(100), nullable=False)
    genero = sa.Column(sa.VARCHAR(1))

#Tabela de Vendedores

class Vendedor(base):
    __tablename__ = "vendedor"
    
    registro_vendedor = registro_venderdor = sa.Column(sa.Integer, primary_key=True, index=True)
    cpf = sa.Column(sa.CHAR(14), nullable=False)
    nome = sa.Column(sa.VARCHAR(100), nullable=False)
    genero = sa.Column(sa.VARCHAR(1))
    email = sa.Column(sa.VARCHAR(50))

#Tabela de Vendas

class Venda(base):
    __tablename__ = "vendas"
    
    idTransacao = sa.Column(sa.Integer, primary_key=True, index=True)
    cpf = sa.Column(sa.CHAR(14), sa.ForeignKey("cliente.cpf", ondelete="no action", onupdate="cascade"), index=True)
    registro_vendedor = sa.Column(sa.Integer, sa.ForeignKey("vendedor.registro_vendedor", ondelete="no action", onupdate="cascade"), index=True)
    codBarras = sa.Column(sa.Integer, sa.ForeignKey("produto.codBarras", ondelete="no action", onupdate="cascade"), index=True)
    dia_hora_venda = sa.Column(sa.DATETIME, nullable = False)
    vlrVenda = sa.Column(sa.DECIMAL(10,2), nullable = False)

try:
        base.metadata.create_all(engine)
        print("Tabelas criadas com sucesso!")
except ValueError as e:
        print(f"ERRO CRÍTICO ao criar tabelas em vendas.py: {e}")