from clas import person
def can(wasre):
    for w in wasre:
        print(w)
fake = ['waste','wrest','make','fuck']
can(fake)

def dic(dictinoary):
    for x , y in dictinoary.items():
        print(x,y)
w = {'key':'value','key2':'value','key3':'value','key':'val'}
dic(w)

def tup(tupl):
    for x in tupl:
        print(x)
c =('s','y','z','c','k','l')
tup(c)

def wa(mak):
    for x,y in mak.items():
        print(x)
        fu = y['this']
        fu1 = y['where']
        fu2 = y['which']
        print(fu + fu2 + fu1)
k = {'key':{'this':'that','where':'what','which':'then'}}
wa(k)

v = lambda x : x*x
v(12)

wa.person