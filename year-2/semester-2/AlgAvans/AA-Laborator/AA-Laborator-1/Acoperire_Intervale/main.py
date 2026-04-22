

#citiam intervalul de la tastatura 
a,b=map(int,input().split())


#citim numarul de doctori
n=int(input())

program = []
#citim programul doctorilor
for i in range(n):
    x,y = map(int,input().split())
    program.append((x,y))
