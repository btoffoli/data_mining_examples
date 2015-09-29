import numpy
from numpy import array
from scipy.cluster.vq import vq, kmeans, whiten


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, query
from models_tide import Ocorrencia, Localizacao
from shapely import wkb
from geoalchemy2.elements import WKBElement

def convert_point(p):
    if type(p) == WKBElement:
        return wkb.loads(bytes(p.data))
    return p


def locations():
    engine = create_engine('postgresql://geocontrol:geo007@localhost/tide', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    #a = array([])
    a = []
    locs = session.query(Localizacao).filter(Localizacao.poligono != None) .order_by(Localizacao.data_hora_criacao.desc()).slice(0,100).all()
    for l in locs:
        pos = convert_point(l.poligono)
        #numpy.append(a, [l.data_hora_criacao, pos.x, pos.y])
        a.append([pos.x, pos.y])

    return a



def kmeans1():
    features  = array([[ 1.9,2.3], [ 1.5,2.5], [ 0.8,0.6], [ 0.4,1.8], [ 0.1,0.1], [ 0.2,1.8], [ 2.0,0.5], [ 0.3,1.5], [ 1.0,1.0]])
    whitened = whiten(features)
    book = array((whitened[0],whitened[2]))
    kmeans(whitened,book)
    (array([[ 2.3110306 ,  2.86287398],
           [ 0.93218041,  1.24398691]]), 0.85684700941625547)

def kmeans2():
    features = locations()
    whitened = whiten(features)
    book = array((whitened[0],whitened[2]))
    kmeans(whitened,book)
    (array([[ 2.3110306 ,  2.86287398],
           [ 0.93218041,  1.24398691]]), 0.85684700941625547)

kmeans2()