from pylab import *
import matplotlib.pyplot as plt
import os
import pyAgrum as gum
import pyAgrum.lib.notebook as gnb



#create empty bayesian network as well as give it a name
bn=gum.BayesNet('WaterSprinkler')
print(bn)

#creat labelized variable = random variable
c=bn.add(gum.LabelizedVariable('c','cloudy ?',2))
print(c) # value of the node in the DAG

#add 3 more variable s,r,and w
s, r, w = [ bn.add(name, 2) for name in "srw" ] 
print(s,r,w)
print(bn)


#connect nodes with an arc
bn.addArc(c,s)

for link in [(c,r),(s,w),(r,w)]:
    bn.addArc(*link)
print(bn)



