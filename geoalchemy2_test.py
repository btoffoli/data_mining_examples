
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, query

from models_tide import Ocorrencia, Localizacao



engine = create_engine('postgresql://geocontrol:geo007@localhost/tide', echo=True)


Session = sessionmaker(bind=engine)

session = Session()

q = session.query(Ocorrencia).order_by(Ocorrencia.data_hora_atualizacao)

o = q.first()
print(o)
