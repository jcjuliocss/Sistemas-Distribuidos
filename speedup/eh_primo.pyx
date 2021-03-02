def TestaPrimo(int n):
    cdef int EhPrimo = 1
    cdef int d = 2
    if (n <= 1):
        EhPrimo = 0

    while EhPrimo == 1 and d <= n / 2:
        if n % d == 0:
            EhPrimo = 0
        d = d + 1

    return EhPrimo

def testa_primo2(int n):
    if n <= 1:
        return 0

    cdef int primo = 1
    cdef int d = 2
    while primo == 1 and d <= (n / 2):
        if n % d == 0:
            return 0
        d += 1

    return 1

def testa_primo3(int n):
    if (n != 2 and n % 2 == 0) or n <= 1:
        return 0

    cdef int primo = 1
    cdef int d = 3
    while primo and d <= (n / 2):
        if n % d == 0:
            return 0
        d += 1

    return 1
