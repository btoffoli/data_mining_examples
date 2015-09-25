from numpy import array
from scipy.cluster.vq import vq, kmeans, whiten
features  = array([[ 1.9,2.3], [ 1.5,2.5], [ 0.8,0.6], [ 0.4,1.8], [ 0.1,0.1], [ 0.2,1.8], [ 2.0,0.5], [ 0.3,1.5], [ 1.0,1.0]])
whitened = whiten(features)
book = array((whitened[0],whitened[2]))
kmeans(whitened,book)
(array([[ 2.3110306 ,  2.86287398],
       [ 0.93218041,  1.24398691]]), 0.85684700941625547)

