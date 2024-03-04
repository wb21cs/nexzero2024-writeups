p = 94870544634437736510840762818333376841742882634831537595688230105812017096483
q = 101676806214782912623965046172630710699952727444649297357365091181445815602423
n = 9646133982286638553098289431708359597742962890715306079129512588482795237366648221809435629553015394294363896520120846912509011493091398851884343959578309
e = 2
c = 3119764668748711508220808235240851124304269759793108959684159670352119046143946860636807179972066427531672558917069675705801167306575858295827566698345153

def gcdExtended(a, b): 
    # Base Case 
    if a == 0 : 
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a) 
     
    # Update x and y using results of recursive 
    # call 
    x = y1 - (b//a) * x1 
    y = x1 
     
    return gcd,x,y 
 
mp = pow(c, (p+1)//4, p)
mq = pow(c, (q+1)//4, q)

_, yp, yq = gcdExtended(p, q)

r1 = (yp*p*mq + yq*q*mp) % n
r2 = n - r1
r3 = (yp*p*mq - yq*q*mp) % n
r4 = n - r3

print(bytes.fromhex(hex(r1)[2:]))
print(bytes.fromhex(hex(r2)[2:]))
print(bytes.fromhex(hex(r3)[2:]))
print(bytes.fromhex(hex(r4)[2:]))