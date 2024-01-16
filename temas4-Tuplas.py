'''
Las tuplas son inmutable
'''

newTupla = ("uno","dos","tres")
print(newTupla)

twoTupla=(1,True,2.00,"Hola",12+5)
print(twoTupla)

triTupla=((123132,213213,3),("hola","pedro"),(1+2,4+5))
print(triTupla[1][0])

proTupla = newTupla + triTupla
print(proTupla)