def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x
    

class Fraction:
    def __init__(self, x=0, y=1):
        g = gcd(x, y)
        self.numerator = x // g
        self.denominator = y // g
          
    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        return str(self.numerator) + '/' + str(self.denominator)
    
    def __add__(self, other):
        a, b, c, d = self.numerator, other.numerator, self.denominator, other.denominator
        return Fraction(a * d + b * c, c * d)
    
    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        a, b, c, d = self.numerator, other.numerator, self.denominator, other.denominator
        return Fraction(a * d - b * c, c * d)

    def __rsub__(self, other):
        return -(self - other)
        
    def __neg__(self):
        a, b = self.numerator, self.denominator
        return Fraction(-a, b)

    def __mul__(self, other):
        a, b, c, d = self.numerator, other.numerator, self.denominator, other.denominator
        return Fraction(a * b, c * d)

    def __rmul__(self, other):
        return self * other

    def __floordiv__(self, other):
        a, b, c, d = self.numerator, other.numerator, self.denominator, other.denominator
        return Fraction(a * d, c * b)

    def __rfloordiv__(self, other):
        a, b, c, d = self.numerator, other.numerator, self.denominator, other.denominator
        return Fraction(c * b, a * d)

    def __eq__(self, other):
        a, b, c, d = self.numerator, other.numerator, self.denominator, other.denominator
        return a * d == b * c
    
    def __ne__(self, other):
        a, b, c, d = self.numerator, other.numerator, self.denominator, other.denominator
        return a * d != b * c
    
    def __lt__(self, other):
        a, b, c, d = self.numerator, other.numerator, self.denominator, other.denominator
        return a * d < b * c
        
    def __le__(self, other):
        a, b, c, d = self.numerator, other.numerator, self.denominator, other.denominator
        return a * d <= b * c
    
    def __gt__(self, other):
        a, b, c, d = self.numerator, other.numerator, self.denominator, other.denominator
        return a * d > b * c
    
    def __ge__(self, other):
        a, b, c, d = self.numerator, other.numerator, self.denominator, other.denominator
        return a * d >= b * c

#Egyptian fractions
def close(a):
    x = a.numerator
    y = a.denominator
    if x == 1:
        return a
    else:
        b = y // x + 1
        return Fraction(1, b)


x, y = input().split('/')
x = int(x)
y = int(y)
a = Fraction(x, y)
c = []
d = 0
left = a
while left > 0:
    d = close(left)
    left -= d
    c.append(str(d.denominator))
print('1/' + '+1/'.join(c))


#From continued fraction to normal
n = int(input())
a = list(map(int, input().split()))
x = 0
b = 0
for i in range(n):
    if i == 0:
        x = Fraction(a[n - 1])
    else:
        b = 1 // x
        x = b + a[n - i - 1]
print(x)


#From normal to continued
a = list(map(int, input().split('/')))
if len(a) == 1:
    print(a[0])
elif a[0] == 1:
    print('0', str(a[1]))
else:
    n = Fraction(a[0], a[1])
    x = a[0]
    y = a[1]
    while x != 1:
        print(x // y, end = ' ')
        n = 1 // (n - x // y)
        x = n.numerator
        y = n.denominator


#Closest fraction with limited denominator
a, b = list(map(int, input().split('/')))
q = int(input())
ans = Fraction(1, 1)
x = Fraction(a, b)
for i in range(q):
    up1 = int((a * (i + 1) / b) // 1)
    up2 = int((a * i / b) // 1 + 1)
    f1 = Fraction(up1, i + 1)
    f2 = Fraction(up2, i + 1)
    d = min(abs(x - f1), abs(x - f2))
    if abs(x - f1) == d:
        f = f1
    else:
        f = f2
    if d == 0:
        ans = f
        break
    if abs(x - ans) >= d:
        ans = f
print(ans)


#Repeating decimal to fraction
a = input().strip().split('.')
b = a[1].split('(')
x = int(a[0])
if '(' not in a[1]:
    y = int(b[0])
    yl = len(list(b[0]))    
    print(x + Fraction(y, 10 ** yl))
else:
    z = int(''.join(list(b[1])[:-1]))
    yl = len(list(b[0]))
    zl = len(list(b[1])) - 1
    up = Fraction(z, 10 ** (yl + zl))
    dwn = 1 - Fraction(1, 10 ** zl)
    if b[0] != '':
        y = int(b[0])
        yl = len(list(b[0]))        
        print(x + Fraction(y, 10 ** yl) + up // dwn)
    else:
        print(x + up // dwn)