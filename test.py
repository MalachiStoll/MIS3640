def factors(n):
    for a in range( 1, n , +1):
            if n % a == 0:
                print(a)

factors(10)