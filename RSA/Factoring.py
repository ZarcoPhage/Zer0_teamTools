number = 510143758735509025530880200653196460532653147
q = 2
p = 3
result = 0
n= number
for x in range (2, n + 1):
    prime= True
    for y in range (2, x):
        if x % y == 0:
            prime= False
    if prime:
        print (x)
while result != number:
    result  = number