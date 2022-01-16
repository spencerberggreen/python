def bdft():
    result = ((t * w * l) / 144)* q
    return result

t = 1.5 #input('thickness: ')
w = 6 #input('width: ')
l = 96 #input('length: ')
q = 10 #input('quantity: ')

t = float(t)
w = float(w)
l = float(l)
q = float(q)

print(bdft())