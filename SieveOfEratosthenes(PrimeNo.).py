def SieveOfEratosthenes(n):
    prime = [True]*(n+1)
    prime[0] = prime[1] = False
    p=2
    while (p*p<=n):
        if prime[p]==True:
            for i in range(p*p, n+1, p):
                prime[i] = False
        p+=1
    
    for key,val in enumerate(prime):
        print(key," -> ",val)

N =int(input("Enter value to find Prime no. till that ->"))
SieveOfEratosthenes(N)