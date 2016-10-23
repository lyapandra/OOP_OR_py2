#https://lancelote.gitbooks.io/intermediate-python/content/book/generators.html
# generator version
def fibon_g(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
# tulips version
def fibon_t(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result
		
		
for x in fibon_g(1000): #1000000):
    print(x)
