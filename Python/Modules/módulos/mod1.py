def hello():
    "imprime oi mundo"
    
    a=int(input('Digite um número: '))
    
    while(a > 10 or a < 2):
        a=int(input('Digite um número: '))
    
    for x in range(0,a):
        print('Hello World!')
    
    return()