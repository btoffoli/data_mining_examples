# coding: utf-8
from sqlalchemy import BigInteger, Boolean, Column, DateTime, Float, ForeignKey, Index, Integer, String, Table, Text, text
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql.base import ARRAY
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry


Base = declarative_base()
metadata = Base.metadata


# class Afastamento(Base):
#     __tablename__ = 'afastamento'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('afastamento_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False)
#     habilitado = Column(Boolean, nullable=False)
#     assuncao_servico_id = Column(BigInteger, nullable=False, index=True)
#     tipo_id = Column(BigInteger, nullable=False, index=True)
#     observacao = Column(Text)
#     data_hora_fim = Column(DateTime(True), index=True)
#
#
# class Aisp(Base):
#     __tablename__ = 'aisp'
#
#     gid = Column(Integer, primary_key=True, server_default=text("nextval('aisp_gid_seq'::regclass)"))
#     aisp = Column(String(255))
#     id1 = Column(Integer)
#     geom = Column(NullType)
#     geom_wgs84 = Column(NullType)
#     estrutura_id = Column(BigInteger)
#     polygon_wgs84 = Column(NullType)
#
#
# class AssociacaoEstrutura(Base):
#     __tablename__ = 'associacao_estrutura'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('associacao_estrutura_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     controle_id = Column(BigInteger, nullable=False, index=True)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     estrutura_id = Column(BigInteger, nullable=False, index=True)
#     habilitado = Column(Boolean, nullable=False)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#
# class Assuncao(Base):
#     __tablename__ = 'assuncao'
#     __table_args__ = (
#         Index('idx_assuncao_1', 'veiculo_id', 'usuario_id'),
#         Index('idx_assuncao_2', 'usuario_id', 'veiculo_id')
#     )
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('assuncao_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     fim = Column(DateTime(True), index=True)
#     habilitado = Column(Boolean, nullable=False)
#     id_sessao = Column(BigInteger, nullable=False)
#     inicio = Column(DateTime(True), nullable=False, index=True)
#     responsavel = Column(Boolean, nullable=False)
#     tipo_id = Column(BigInteger, index=True)
#     usuario_id = Column(BigInteger, nullable=False, index=True)
#     veiculo_id = Column(BigInteger, nullable=False, index=True)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#

class AssuncaoServico(Base):
    __tablename__ = 'assuncao_servico'

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('assuncao_servico_id_seq'::regclass)"))
    version = Column(BigInteger, nullable=False)
    habilitado = Column(Boolean, nullable=False)
    data_hora_criacao = Column(DateTime(True), nullable=False)
    data_hora_atualizacao = Column(DateTime(True), nullable=False)
    veiculo_id = Column(BigInteger, nullable=False, index=True)
    atividade_id = Column(BigInteger, index=True)
    setor_id = Column(BigInteger, index=True)
    data_hora_fim = Column(DateTime(True))
    km = Column(String(255))


# class Atividade(Base):
#     __tablename__ = 'atividade'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('atividade_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     data_hora_atualizacao = Column(DateTime(True))
#     habilitado = Column(Boolean, nullable=False)
#     identificacao = Column(String, nullable=False, unique=True)
#     nome = Column(String, nullable=False)
#     apelido = Column(String)
#     atividade_pai_id = Column(BigInteger, index=True)
#
#
# class AtividadeEstrutura(Base):
#     __tablename__ = 'atividade_estrutura'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('atividade_estrutura_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     data_hora_atualizacao = Column(DateTime(True))
#     habilitado = Column(Boolean, nullable=False)
#     estrutura_id = Column(BigInteger, nullable=False, index=True)
#     atividade_id = Column(BigInteger, nullable=False, index=True)
#
#
# class Chamada(Base):
#     __tablename__ = 'chamada'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('chamada_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     habilitado = Column(Boolean, nullable=False)
#     numero = Column(String(255))
#     ramal_id = Column(ForeignKey(u'ramal.id'), nullable=False, index=True)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#     user_info = Column(String(255))
#     ucid = Column(String(255))
#
#     ramal = relationship(u'Ramal')


# class CircunscricaoEstrutura(Base):
#     __tablename__ = 'circunscricao_estrutura'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('circunscricao_estrutura_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     estrutura_id = Column(BigInteger, nullable=False, index=True)
#     habilitado = Column(Boolean, nullable=False)
#     nome = Column(String(255))
#     poligono = Column(NullType, nullable=False)
#     tipo_id = Column(BigInteger, index=True)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#
# class CircunscricaoSetor(Base):
#     __tablename__ = 'circunscricao_setor'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('circunscricao_setor_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     data_hora_atualizacao = Column(DateTime(True))
#     habilitado = Column(Boolean, nullable=False)
#     setor_id = Column(BigInteger, nullable=False, index=True)
#     poligono = Column(NullType, nullable=False)
#     tipo_id = Column(BigInteger, index=True)
#     nome = Column(String(255), nullable=False)
#
#
# class ClassificacaoRisco(Base):
#     __tablename__ = 'classificacao_risco'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('classificacao_risco_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     cor = Column(String(255))
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     descricao = Column(Text)
#     grau = Column(BigInteger)
#     habilitado = Column(Boolean, nullable=False)
#     nome = Column(String(255), nullable=False)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#
# class ContatoDadosPessoai(Base):
#     __tablename__ = 'contato_dados_pessoais'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('contato_dados_pessoais_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     destino_id = Column(BigInteger, nullable=False, index=True)
#     habilitado = Column(Boolean, nullable=False)
#     tipo_id = Column(BigInteger, nullable=False, index=True)
#     conteudo = Column(String(255))
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#
# class ContatoEstrutura(Base):
#     __tablename__ = 'contato_estrutura'
#     __table_args__ = (
#         Index('idx_contato_estrutura_2', 'destino_id', 'tipo_id'),
#         Index('idx_contato_estrutura_1', 'tipo_id', 'destino_id')
#     )
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('contato_estrutura_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     destino_id = Column(BigInteger, nullable=False, index=True)
#     habilitado = Column(Boolean, nullable=False)
#     tipo_id = Column(BigInteger, index=True)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#
# class ControleLogin(Base):
#     __tablename__ = 'controle_login'
#     __table_args__ = (
#         Index('idx_controle_login_1', 'usuario_id', 'data_hora_entrada'),
#     )
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('controle_login_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     data_hora_entrada = Column(DateTime(True), nullable=False, index=True)
#     data_hora_saida = Column(DateTime(True))
#     dominio = Column(String(255))
#     habilitado = Column(Boolean, nullable=False)
#     ip = Column(String(15))
#     tipo_logout = Column(String(255))
#     usuario_id = Column(BigInteger, nullable=False, index=True)
#     terminal_id = Column(BigInteger, index=True)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#
# class ControlePosicaoAtendimento(Base):
#     __tablename__ = 'controle_posicao_atendimento'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('controle_posicao_atendimento_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     controle_login_id = Column(BigInteger, nullable=False, index=True)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     data_hora_entrada = Column(DateTime(True), nullable=False)
#     data_hora_saida = Column(DateTime(True))
#     habilitado = Column(Boolean, nullable=False)
#     procedimento_id = Column(BigInteger, nullable=False, index=True)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#
# class DadosPessoai(Base):
#     __tablename__ = 'dados_pessoais'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('dados_pessoais_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     cpf = Column(String(255))
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     data_nascimento = Column(DateTime(True))
#     habilitado = Column(Boolean, nullable=False)
#     idade = Column(String(255))
#     nome = Column(String(255), nullable=False)
#     rg = Column(String(255))
#     sexo = Column(String(255))
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#
# class Databasechangelog(Base):
#     __tablename__ = 'databasechangelog'
#
#     id = Column(String(63), primary_key=True, nullable=False)
#     author = Column(String(63), primary_key=True, nullable=False)
#     filename = Column(String(200), primary_key=True, nullable=False)
#     dateexecuted = Column(DateTime(True), nullable=False)
#     orderexecuted = Column(Integer, nullable=False)
#     exectype = Column(String(10), nullable=False)
#     md5sum = Column(String(35))
#     description = Column(String(255))
#     comments = Column(String(255))
#     tag = Column(String(255))
#     liquibase = Column(String(20))
#
#
# class Databasechangeloglock(Base):
#     __tablename__ = 'databasechangeloglock'
#
#     id = Column(Integer, primary_key=True)
#     locked = Column(Boolean, nullable=False)
#     lockgranted = Column(DateTime(True))
#     lockedby = Column(String(255))
#
#
# class Desfecho(Base):
#     __tablename__ = 'desfecho'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('desfecho_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     habilitado = Column(Boolean, nullable=False)
#     nome = Column(String(255))
#     sigla = Column(String(255))
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#
# class DetalhesEstagioProcedimento(Base):
#     __tablename__ = 'detalhes_estagio_procedimento'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('detalhes_estagio_procedimento_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     habilitado = Column(Boolean, nullable=False)
#     nome = Column(String(255), nullable=False)
#     telefone = Column(String(255), nullable=False)
#     estagio_procedimento_id = Column(BigInteger, nullable=False)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#

class Empenho(Base):
    __tablename__ = 'empenho'

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('empenho_id_seq'::regclass)"))
    version = Column(BigInteger, nullable=False)
    data_hora_criacao = Column(DateTime(True), nullable=False)
    data_hora_fim = Column(DateTime(True), index=True)
    data_hora_inicio = Column(DateTime(True), nullable=False)
    habilitado = Column(Boolean, nullable=False)
    ocorrencia_id = Column(BigInteger, ForeignKey('ocorrencia.id'))
    data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
    assuncao_servico_id = Column(BigInteger, ForeignKey('assuncao_servico.id'))


# class Envolvido(Base):
#     __tablename__ = 'envolvido'
#     __table_args__ = (
#         Index('idx_envolvido_1', 'ocorrencia_id', 'empenho_id'),
#         Index('idx_envolvido_2', 'empenho_id', 'ocorrencia_id')
#     )
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('envolvido_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     dados_pessoais_id = Column(BigInteger, index=True)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     empenho_id = Column(BigInteger, index=True)
#     habilitado = Column(Boolean, nullable=False)
#     ocorrencia_id = Column(BigInteger, nullable=False, index=True)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#
# class Estagio(Base):
#     __tablename__ = 'estagio'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('estagio_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     habilitado = Column(Boolean, nullable=False)
#     nome = Column(String(255), nullable=False)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#
# class EstagioProcedimento(Base):
#     __tablename__ = 'estagio_procedimento'
#     __table_args__ = (
#         Index('idx_estagio_procedimento_1', 'estagio_procedimento_anterior_id', 'data_hora_gerado'),
#     )
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('estagio_procedimento_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_aceite = Column(DateTime(True), index=True)
#     data_hora_confirmacao = Column(DateTime(True))
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     data_hora_envio = Column(DateTime(True), index=True)
#     data_hora_espera = Column(DateTime(True))
#     data_hora_finalizacao = Column(DateTime(True), index=True)
#     data_hora_gerado = Column(DateTime(True))
#     estagio_id = Column(BigInteger, nullable=False, index=True)
#     estagio_procedimento_anterior_id = Column(BigInteger, index=True)
#     estagios_procedimentos_posteriores_id = Column(BigInteger, index=True)
#     estrutura_id = Column(BigInteger, index=True)
#     habilitado = Column(Boolean, nullable=False)
#     ocorrencia_id = Column(BigInteger, nullable=False, index=True)
#     procedimento_id = Column(BigInteger, nullable=False, index=True)
#     responsavel_id = Column(BigInteger, index=True)
#     tempo_espera = Column(BigInteger)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#
class Estrutura(Base):
    __tablename__ = 'estrutura'

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('estrutura_id_seq'::regclass)"))
    version = Column(BigInteger, nullable=False)
    data_hora_criacao = Column(DateTime(True), nullable=False)
    endereco = Column(String(255))
    habilitado = Column(Boolean, nullable=False)
    id_autorizacao = Column(BigInteger)
    localizacao = Column(NullType)
    nome = Column(String(255), nullable=False)
    tipo_id = Column(BigInteger, index=True)
    data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
    habilitado_recebimento_ocorrencia = Column(Boolean, nullable=False)


# class EventoEmCampo(Base):
#     __tablename__ = 'evento_em_campo'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('evento_em_campo_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False, index=True)
#     empenho_id = Column(BigInteger, nullable=False, index=True)
#     habilitado = Column(Boolean, nullable=False)
#     observacao = Column(String(255))
#     responsavel_id = Column(BigInteger, nullable=False, index=True)
#     tipo_id = Column(BigInteger, nullable=False, index=True)
#     tempo_estimado = Column(BigInteger)
#     rota = Column(NullType)
#     distancia = Column(BigInteger)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#
# class Forca(Base):
#     __tablename__ = 'forca'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('forca_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     habilitado = Column(Boolean, nullable=False)
#     nome = Column(String(255), nullable=False)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#
# t_geography_columns = Table(
#     'geography_columns', metadata,
#     Column('f_table_catalog', String),
#     Column('f_table_schema', String),
#     Column('f_table_name', String),
#     Column('f_geography_column', String),
#     Column('coord_dimension', Integer),
#     Column('srid', Integer),
#     Column('type', Text)
# )
#
#
# t_geometry_columns = Table(
#     'geometry_columns', metadata,
#     Column('f_table_catalog', String(256)),
#     Column('f_table_schema', String(256)),
#     Column('f_table_name', String(256)),
#     Column('f_geometry_column', String(256)),
#     Column('coord_dimension', Integer),
#     Column('srid', Integer),
#     Column('type', String(30))
# )
#
#
# class Grupo(Base):
#     __tablename__ = 'grupo'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('grupo_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     estrutura_id = Column(BigInteger, nullable=False, index=True)
#     grupo_superior_id = Column(BigInteger, index=True)
#     nome = Column(String(255), nullable=False)
#
#
# class GrupoNatureza(Base):
#     __tablename__ = 'grupo_natureza'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('grupo_natureza_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     habilitado = Column(Boolean, nullable=False)
#     nome = Column(String(255), nullable=False)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#
# class HipoteseDiagnostico(Base):
#     __tablename__ = 'hipotese_diagnostico'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('hipotese_diagnostico_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     habilitado = Column(Boolean, nullable=False)
#     nome = Column(String(255), nullable=False)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#
# class Historico(Base):
#     __tablename__ = 'historico'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('historico_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     conteudo = Column(String(255))
#     data = Column(DateTime(True), nullable=False)
#     obj_id = Column(BigInteger, nullable=False)
#     op = Column(String(255), nullable=False)
#     tipo = Column(String(255), nullable=False)
#
#
# class Link(Base):
#     __tablename__ = 'link'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('link_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     habilitado = Column(Boolean, nullable=False)
#     nome = Column(String(255), nullable=False)
#     link = Column(String(255), nullable=False)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)


class Localizacao(Base):
    __tablename__ = 'localizacao'

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('localizacao_id_seq'::regclass)"))
    version = Column(BigInteger, nullable=False)
    bairro = Column(String(255), index=True)
    cep = Column(String(255))
    complemento = Column(String(255))
    data_hora_criacao = Column(DateTime(True), nullable=False)
    habilitado = Column(Boolean, nullable=False)
    logradouro = Column(String(255))
    municipio = Column(String(255), nullable=False)
    numero = Column(String(255))
    ocorrencia_id = Column(BigInteger, ForeignKey('ocorrencia.id'))
    poligono = Column(Geometry('POLYGON'))
    referencia = Column(String(255), index=True)
    uf = Column(String(255), nullable=False)
    data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
    circunscricao_setor_id = Column(BigInteger)


# class Membro(Base):
#     __tablename__ = 'membro'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('membro_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     habilitado = Column(Boolean, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False)
#     assuncao_servico_id = Column(BigInteger, nullable=False, index=True)
#     usuario_id = Column(BigInteger, nullable=False, index=True)
#     funcao_id = Column(BigInteger, index=True)
#     flag_digitador = Column(Boolean)
#     celular = Column(String(255))
#
#
# class Natureza(Base):
#     __tablename__ = 'natureza'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('natureza_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     codigo = Column(String(255), nullable=False, unique=True)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     habilitado = Column(Boolean, nullable=False)
#     nome = Column(String(255), nullable=False, unique=True)
#     sigla = Column(String(255))
#     roteiro = Column(Text)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#
# class ObjetoEnvolvido(Base):
#     __tablename__ = 'objeto_envolvido'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('objeto_envolvido_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     habilitado = Column(Boolean, nullable=False)
#     nome = Column(String(255), nullable=False)
#     ocorrencia_id = Column(BigInteger, nullable=False, index=True)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#
# class Observacao(Base):
#     __tablename__ = 'observacao'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('observacao_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     descricao = Column(Text, nullable=False)
#     habilitado = Column(Boolean, nullable=False)
#     ocorrencia_id = Column(BigInteger, nullable=False, index=True)
#     responsavel_id = Column(BigInteger, nullable=False, index=True)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#
# class ObservacaoLida(Base):
#     __tablename__ = 'observacao_lida'
#     __table_args__ = (
#         Index('idx_observacao_lida_usuario_id_observacao_id', 'observacao_id', 'usuario_id'),
#         Index('idx_observacao_lida_observacao_id_usuario_id', 'usuario_id', 'observacao_id')
#     )
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('observacao_lida_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False, index=True)
#     observacao_id = Column(ForeignKey(u'observacao.id'), nullable=False, index=True)
#     usuario_id = Column(ForeignKey(u'usuario.id'), nullable=False, index=True)
#     data_hora_atualizacao = Column(DateTime(True), index=True)
#     habilitado = Column(Boolean, nullable=False, index=True)
#
#     observacao = relationship(u'Observacao')
#     usuario = relationship(u'Usuario')


class Ocorrencia(Base):
    __tablename__ = 'ocorrencia'
    __table_args__ = (
        Index('idx_ocorrencia_8', 'estrutura_id', 'tipo_id', 'data_hora_inicio'),
    )

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('ocorrencia_id_seq'::regclass)"))
    version = Column(BigInteger, nullable=False)
    cod_ocorrencia = Column(String(255), index=True)
    data_hora_criacao = Column(DateTime(True), nullable=False)
    data_hora_fim = Column(DateTime(True))
    data_hora_inicio = Column(DateTime(True), nullable=False, index=True)
    grupo_id = Column(BigInteger, index=True)
    habilitado = Column(Boolean, nullable=False)
    ocorrencia_reiterada_id = Column(BigInteger, index=True)
    protocolo = Column(String(255), nullable=False, index=True)
    tipo_id = Column(BigInteger, index=True)
    data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
    bopm = Column(String(255))
    ro = Column(String(255))
    estrutura_id = Column(BigInteger)
    chamada_id = Column(BigInteger)

    def __str__(self):
        return  self.protocolo.__str__()


class OcorrenciaNatureza(Base):
    __tablename__ = 'ocorrencia_natureza'

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('ocorrencia_natureza_id_seq'::regclass)"))
    version = Column(BigInteger, nullable=False)
    habilitado = Column(Boolean, nullable=False)
    data_hora_criacao = Column(DateTime(True), nullable=False)
    data_hora_atualizacao = Column(DateTime(True), nullable=False)
    ocorrencia_id = Column(BigInteger, nullable=False, index=True)
    natureza_id = Column(BigInteger, nullable=False, index=True)


# class Origem(Base):
#     __tablename__ = 'origem'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('origem_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     atributo_pesquisa_dados_pessoais = Column(String(255))
#     conteudo = Column(String(255), nullable=False)
#     conteudo2 = Column(String(255))
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     habilitado = Column(Boolean, nullable=False)
#     ocorrencia_id = Column(BigInteger, nullable=False, index=True)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#
# class Procedimento(Base):
#     __tablename__ = 'procedimento'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('procedimento_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     action = Column(String(255))
#     controller = Column(String(255), nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     escolher_estruturas = Column(Boolean, nullable=False)
#     habilitado = Column(Boolean, nullable=False)
#     nome = Column(String(255), nullable=False)
#     sigla = Column(String(255), nullable=False)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#
# class ProcedimentoPosterior(Base):
#     __tablename__ = 'procedimento_posterior'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('procedimento_posterior_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     habilitado = Column(Boolean, nullable=False)
#     procedimento_id = Column(BigInteger, nullable=False, index=True)
#     procedimento_posterior_id = Column(BigInteger, nullable=False, index=True)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#
# class Ramal(Base):
#     __tablename__ = 'ramal'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('ramal_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     habilitado = Column(Boolean, nullable=False)
#     numero = Column(String(255), nullable=False)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#
# t_raster_columns = Table(
#     'raster_columns', metadata,
#     Column('r_table_catalog', String),
#     Column('r_table_schema', String),
#     Column('r_table_name', String),
#     Column('r_raster_column', String),
#     Column('srid', Integer),
#     Column('scale_x', Float(53)),
#     Column('scale_y', Float(53)),
#     Column('blocksize_x', Integer),
#     Column('blocksize_y', Integer),
#     Column('same_alignment', Boolean),
#     Column('regular_blocking', Boolean),
#     Column('num_bands', Integer),
#     Column('pixel_types', ARRAY(TEXT())),
#     Column('nodata_values', ARRAY(DOUBLE_PRECISION(precision=53))),
#     Column('out_db', ARRAY(BOOLEAN())),
#     Column('extent', NullType)
# )
#
#
# t_raster_overviews = Table(
#     'raster_overviews', metadata,
#     Column('o_table_catalog', String),
#     Column('o_table_schema', String),
#     Column('o_table_name', String),
#     Column('o_raster_column', String),
#     Column('r_table_catalog', String),
#     Column('r_table_schema', String),
#     Column('r_table_name', String),
#     Column('r_raster_column', String),
#     Column('overview_factor', Integer)
# )
#
#
# class Regulacao(Base):
#     __tablename__ = 'regulacao'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('regulacao_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     avaliacao = Column(Text, nullable=False)
#     conduta = Column(Text, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False, index=True)
#     escore_trauma = Column(String(255))
#     fc = Column(String(255))
#     fr = Column(String(255))
#     glasgow = Column(String(255))
#     glicemia = Column(String(255))
#     habilitado = Column(Boolean, nullable=False)
#     pa = Column(String(255))
#     paciente_id = Column(ForeignKey(u'envolvido.id'), nullable=False, index=True)
#     responsavel_id = Column(ForeignKey(u'usuario.id'), nullable=False, index=True)
#     saturacao = Column(String(255))
#     temperatura = Column(String(255))
#     hipotese_id = Column(BigInteger, index=True)
#     risco_id = Column(BigInteger, index=True)
#     solicitacao_veiculo_id = Column(BigInteger, index=True)
#     destino_id = Column(BigInteger, index=True)
#     desfecho_id = Column(BigInteger, index=True)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#     paciente = relationship(u'Envolvido')
#     responsavel = relationship(u'Usuario')
#
#
# class Setor(Base):
#     __tablename__ = 'setor'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('setor_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     data_hora_atualizacao = Column(DateTime(True))
#     habilitado = Column(Boolean, nullable=False)
#     estrutura_id = Column(BigInteger, nullable=False)
#     setor_pai_id = Column(BigInteger, index=True)
#     nome = Column(String(255), nullable=False)
#     identificacao = Column(String, nullable=False, unique=True)
#     apelido = Column(String)
#     sigla = Column(String(255))
#
#
# class SetorAtividadeEstrutura(Base):
#     __tablename__ = 'setor_atividade_estrutura'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('setor_atividade_estrutura_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     data_hora_atualizacao = Column(DateTime(True))
#     habilitado = Column(Boolean, nullable=False)
#     atividade_estrutura_id = Column(BigInteger, nullable=False, index=True)
#     setor_id = Column(BigInteger, nullable=False, index=True)
#
#
# class Solicitante(Base):
#     __tablename__ = 'solicitante'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('solicitante_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     dados_pessoais_id = Column(BigInteger, index=True)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     habilitado = Column(Boolean, nullable=False)
#     ocorrencia_id = Column(BigInteger, nullable=False, index=True)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#
# class SpatialRefSy(Base):
#     __tablename__ = 'spatial_ref_sys'
#
#     srid = Column(Integer, primary_key=True)
#     auth_name = Column(String(256))
#     auth_srid = Column(Integer)
#     srtext = Column(String(2048))
#     proj4text = Column(String(2048))
#
#
# class Terminal(Base):
#     __tablename__ = 'terminal'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('terminal_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     habilitado = Column(Boolean, nullable=False)
#     nome = Column(String(255), nullable=False)
#     ip = Column(String(255))
#     data_final = Column(DateTime(True))
#     terminal_anterior_id = Column(ForeignKey(u'terminal.id'), index=True)
#     ramal_id = Column(ForeignKey(u'ramal.id'), index=True)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#     ramal = relationship(u'Ramal')
#     terminal_anterior = relationship(u'Terminal', remote_side=[id])
#
#
# class TipoAssuncao(Base):
#     __tablename__ = 'tipo_assuncao'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('tipo_assuncao_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     habilitado = Column(Boolean, nullable=False)
#     nome = Column(String(255), nullable=False, unique=True)
#     sigla = Column(String(255), nullable=False, unique=True)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#
# class TipoCircunscricao(Base):
#     __tablename__ = 'tipo_circunscricao'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('tipo_circunscricao_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     habilitado = Column(Boolean, nullable=False)
#     nome = Column(String(255), nullable=False, unique=True)
#     sigla = Column(String(255), nullable=False, unique=True)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#
# class TipoContato(Base):
#     __tablename__ = 'tipo_contato'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('tipo_contato_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     habilitado = Column(Boolean, nullable=False)
#     nome = Column(String(255), nullable=False, unique=True)
#     sigla = Column(String(255), nullable=False, unique=True)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#
# class TipoDadosPessoai(Base):
#     __tablename__ = 'tipo_dados_pessoais'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('tipo_dados_pessoais_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     habilitado = Column(Boolean, nullable=False)
#     nome = Column(String(255), nullable=False, unique=True)
#     sigla = Column(String(255), nullable=False, unique=True)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#
# class TipoEstrutura(Base):
#     __tablename__ = 'tipo_estrutura'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('tipo_estrutura_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     habilitado = Column(Boolean, nullable=False)
#     nome = Column(String(255), nullable=False, unique=True)
#     sigla = Column(String(255), nullable=False, unique=True)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#
# class TipoEventoAfastamento(Base):
#     __tablename__ = 'tipo_evento_afastamento'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('tipo_evento_afastamento_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False)
#     habilitado = Column(Boolean, nullable=False)
#     nome = Column(String(255), nullable=False, unique=True)
#     sigla = Column(String(255), nullable=False, unique=True)
#     codigo = Column(String(255), unique=True)
#
#
# class TipoEventoEmCampo(Base):
#     __tablename__ = 'tipo_evento_em_campo'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('tipo_evento_em_campo_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     habilitado = Column(Boolean, nullable=False)
#     nome = Column(String(255), nullable=False, unique=True)
#     sigla = Column(String(255), nullable=False, unique=True)
#     calcular_rota = Column(Boolean)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#     codigo = Column(String(255))
#

class TipoOcorrencia(Base):
    __tablename__ = 'tipo_ocorrencia'

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('tipo_ocorrencia_id_seq'::regclass)"))
    version = Column(BigInteger, nullable=False)
    data_hora_criacao = Column(DateTime(True), nullable=False)
    georeferenciavel = Column(Boolean, nullable=False)
    habilitado = Column(Boolean, nullable=False)
    nome = Column(String(255), nullable=False, unique=True)
    sigla = Column(String(255), nullable=False, unique=True)
    transferivel = Column(Boolean, nullable=False)
    data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)


# class TipoUsuario(Base):
#     __tablename__ = 'tipo_usuario'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('tipo_usuario_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     habilitado = Column(Boolean, nullable=False)
#     nome = Column(String(255), nullable=False, unique=True)
#     sigla = Column(String(255), nullable=False, unique=True)
#     tipo_pai_id = Column(BigInteger, index=True)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#
# class TipoVeiculo(Base):
#     __tablename__ = 'tipo_veiculo'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('tipo_veiculo_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     habilitado = Column(Boolean, nullable=False)
#     nome = Column(String(255), nullable=False, unique=True)
#     sigla = Column(String(255), nullable=False, unique=True)
#     tipo_pai_id = Column(BigInteger, index=True)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#
# class Usuario(Base):
#     __tablename__ = 'usuario'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('usuario_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     dados_pessoais_id = Column(BigInteger, index=True)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     data_hora_senha_alterada = Column(DateTime(True))
#     habilitado = Column(Boolean, nullable=False)
#     identificacao = Column(String(255), nullable=False, unique=True)
#     senha = Column(String(255), nullable=False)
#     senha_expirada = Column(Boolean)
#     tipo_id = Column(BigInteger, nullable=False, index=True)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#
# class Veiculo(Base):
#     __tablename__ = 'veiculo'
#
#     id = Column(BigInteger, primary_key=True, server_default=text("nextval('veiculo_id_seq'::regclass)"))
#     version = Column(BigInteger, nullable=False)
#     data_hora_criacao = Column(DateTime(True), nullable=False)
#     data_hora_ultima_conexao = Column(DateTime(True))
#     estado = Column(String(255))
#     habilitado = Column(Boolean, nullable=False)
#     id_conecta = Column(String(255), unique=True)
#     id_device = Column(String(255), unique=True)
#     id_siga = Column(String(255))
#     nome = Column(String(255), nullable=False)
#     placa = Column(String(255))
#     tipo_id = Column(ForeignKey(u'tipo_veiculo.id'), nullable=False, index=True)
#     data_hora_atualizacao = Column(DateTime(True), nullable=False, index=True)
#
#     tipo = relationship(u'TipoVeiculo')
