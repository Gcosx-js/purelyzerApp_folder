s=input('1: ').lower()
f=input('2: ').lower()
vowels = ['a','e','i','o','u','y']
i=0
j=0

while True:
    print(i,j)
    if s[i]==f[j]:
        if s[i]!=s[-1]:
            break
        else:
            i+=1
            j+=1
    else:
        if f[j] not in vowels:
            print('Different')
            break
            
        else:
            j+=1
            
            