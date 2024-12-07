def cascade(n):
    print(n)
    if n >= 10:
        cascade(n // 10)
        print(n)
        
