import random as r

def e(a,b,c,d,e,f,g,h,i,j):
    return ((a or b) and (not c and d)) or (e and ((f or g) or (h or not i)) and j)

def create_case():
    var = [r.getrandbits(1) for _ in range(10)]
    result = e(var[0], var[1], var[2], var[3], var[4], var[5], var[6], var[7], var[8], var[9])
    result = str(result).replace('True', '1').replace('False', '0').replace('1', 't').replace('0', 'f')
    
    return f"_ {str(var).replace(',','').replace('[','').replace(']','')} {result}".replace(' ', '\t')
    
def create_table(x:int=25):
    table = "name a b c d e f g h i j target".replace(' ', '\t')
    
    for i in range(x):
        case = create_case()
        case = case.replace('_',f'x{i}')
        
        table = table + '\n' + case
        
    with open('case3.txt', 'w') as f:
        f.write(table)
        
create_table(50)
