def pattern (n):
    if n==0:
        print(" ")
        return
    print("* " * n)
    pattern(n-1)

pattern(5)