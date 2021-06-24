def ksmallServer(n, m, k):
    if m % n == 0:
        return m//n
    else:
        s = m//n
        t = m%n
        if t + k > n:
            return s+1
        else:
            return s

print(ksmallServer(10, 34, 7))
    