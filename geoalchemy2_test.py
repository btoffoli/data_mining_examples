
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, query

from models_tide import Ocorrencia, Localizacao

from shapely import wkb

# from geoalchemy2.elements import WKTElement


engine = create_engine('postgresql://geocontrol:geo007@localhost/tide', echo=True)


Session = sessionmaker(bind=engine)

session = Session()

qo = session.query(Ocorrencia).order_by(Ocorrencia.data_hora_atualizacao.desc())

o = qo.first()

print(o.id)
#Localizacao.poligono.ST_Touches(WKTElement('POINT(1 1)', srid=4326))
ql = session.query(Localizacao).filter(Localizacao.ocorrencia == o)
#.order_by(Ocorrencia.data_hora_atualizacao.desc())
l = ql.first()
y = wkb.loads(bytes(o.localizacao().poligono.data))
print(y)

