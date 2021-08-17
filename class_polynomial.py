from fractions import Fraction 
NUMERIC_TYPES = {int, float}
d = {'0': chr(8304), '1': chr(185), '2': chr(178), '3': chr(179), '4': chr(8308), '5': chr(8309), '6': chr(8310), '7': chr(8311), '8': chr(8312), '9': chr(8313)}


def one(co, deg, ind):
    ans = ''
    if co == 0:
        return ''
    if type(co) == str and float(co) != (int(float(co))):
        co = float(co)
    elif type(co) == str:
        co = int(co)
    if co < 0:
        if ind == 0:
            ans += '-'
        else:
            ans += ' - '
    else:
        if ind != 0:
            ans += ' + '
    if co < 0:
        co = -co
    if deg != 0 and abs(co) == 1:
        co = ''
    elif type(co) != Fraction:
        co = round(co, 3)
    if type(co) == Fraction:
        if co.denominator != 1:
            co = '(' + str(co) + ')'
    co = str(co)
    if deg == 0:
        ans += co
        return ans
    else:
        ans += co
        ans += 'x'
        if deg == 1:
            return ans
        for i in str(deg):
            ans += d[i]
        return ans


def fastExp(same, ours, n):
    if n == 1:
        return same
    if n == 0:
        return Poly([1])
    if n % 2 == 1:
        same = fastExp(same, ours, n - 1)
        return same * ours
    if n % 2 == 0:
        same = fastExp(same, ours, n // 2)
        return same * same


def value(p, c):
    a = p._coeff
    r = a[len(a) - 1]
    for i in range(2, len(a) + 1):
        r = a[len(a) - i] + c * r
    return r
        
        
class Poly:
    def unzero(self):
        while self._coeff[-1] == 0 and len(self._coeff) > 1:
            self._coeff.pop()

    def __init__(self, x = (0,)):
        if type(x) in NUMERIC_TYPES:
            self._coeff = [x]
        elif type(x) == Poly:
            self._coeff = x._coeff[:]
        elif type(x) == Fraction:
            self._coeff = [x]
        elif type(x) == str:
            a = x.split()
            b = []
            for i in a:
                if '.' in i:
                    b.append(float(i))
                else:
                    b.append(int(i))
            self._coeff = b
        elif hasattr(x, '__iter__'):
            self._coeff = list(x)
        self.unzero()

    def __repr__(self):
        a = []
        for i in self._coeff:
            if type(i) == Fraction:
                a.append('Fraction' + '(' + str(i.numerator) + ', ' + str(i.denominator) + ')')
            else:
                a.append(str(i))
        return 'Poly' + "((" + ', '.join(a) + '))'

    def __str__(self):
        res = ''
        ind = 0
        maxx = 1
        for i in self._coeff:
            if ind == len(self._coeff) - 1:
                maxx = 0
            res = one(i, ind, maxx) + res
            ind += 1
        if len(res) == 0:
            return '0'
        else:
            return res

    def __eq__(self, other):
        other = Poly(other)
        if len(other._coeff) != len(self._coeff):
            return False
        for i in range(len(other._coeff)):
            if other._coeff[i] != self._coeff[i]:
                return False
        return True
    
    def __ne__(self, other):
        other = Poly(other)
        if len(other._coeff) != len(self._coeff):
            return True
        for i in range(len(other._coeff)):
            if other._coeff[i] != self._coeff[i]:
                return True
        return False
    
    def __neg__(self):
        co = []
        for i in self._coeff:
            co.append(-i)
        return Poly(co)
    
    def __pos__(self):
        return self
    
    def __bool__(self):
        if self._coeff == [0] or self._coeff == ['0']:
            return False
        return True
    
    def __add__(self, other):
        other = Poly(other)
        co = []
        s = self._coeff
        oth = other._coeff
        for i in range(max(len(s), len(oth))):
            co.append(0)
            if i < len(s):
                co[i] += s[i]
            if i < len(oth):
                co[i] += oth[i]
        return Poly(co)
    
    def __radd__(self, other):
        return self + other
    
    def __iadd__(self, other):
        other = Poly(other)
        co = []
        s = self._coeff
        oth = other._coeff
        for i in range(max(len(s), len(oth))):
            co.append(0)
            if i < len(s):
                co[i] += s[i]
            if i < len(oth):
                co[i] += oth[i]
        while co[-1] == 0:
            co.pop()
        self._coeff = co
        return self
    
    def __sub__(self, other):
        other = Poly(other)
        co = []
        s = self._coeff
        oth = other._coeff
        for i in range(max(len(s), len(oth))):
            co.append(0)
            if i < len(s):
                co[i] += s[i]
            if i < len(oth):
                co[i] -= oth[i]
        return Poly(co)
    
    def __rsub__(self, other):
        return -(self - other)
    
    def __isub__(self, other):
        other = Poly(other)
        co = []
        s = self._coeff
        oth = other._coeff
        for i in range(max(len(s), len(oth))):
            co.append(0)
            if i < len(s):
                co[i] += s[i]
            if i < len(oth):
                co[i] -= oth[i]
        while co[-1] == 0:
            co.pop()
        self._coeff = co
        return self
    
    def __mul__(self, other):
        other = Poly(other)
        s = self._coeff
        oth = other._coeff
        co = [0] * (len(s) * len(oth))
        for i in range(len(s)):
            for j in range(len(oth)):
                co[i + j] += s[i] * oth[j]
        while co[-1] == 0 and len(co) > 1:
            co.pop()
        return Poly(co)

    def __rmul__(self, other):
        return self * other
    
    def __imul__(self, other):
        other = Poly(other)
        s = self._coeff
        oth = other._coeff
        co = [0] * (len(s) * len(oth))
        for i in range(len(s)):
            for j in range(len(oth)):
                co[i + j] += s[i] * oth[j]
        while co[-1] == 0 and len(co) > 1:
            co.pop()
        self._coeff = co
        return self
    
    def __pow__(self, other):
        if other == 0:
            return 1
        else:
            s = self._coeff
            co = Poly(s)
            co = fastExp(co, co, int(other))
        return co
    
    def __ipow__(self, other):
        s = self._coeff
        co = Poly(s)
        co = fastExp(co, co, int(other))
        self._coeff = co._coeff
        return self
    
    def __or__(self, other):
        return value(self, other)
    
    def __iter__(self):
        for i in self._coeff:
            yield i
            
    def __divmod__(self, other):
        ans = []
        a = []
        b = []
        other = Poly(other)
        n1 = len(self._coeff)
        n2 = len(other._coeff)
        if n2 > n1:
            return(Poly(0), self)        
        a += self._coeff
        b += other._coeff
        for n in range(n1 - n2 + 1):
            if len(a) != 0:
                ans.append(Fraction(a[-1], b[-1]))
                x = ans[-1]
                for i in range(n2):
                    a[- i - 1] -= x * b[- i - 1]
                if a[-1] == 0:
                    a.pop()                
            else:
                ans = ans[::-1]
                return(Poly(ans), self - b * Poly(ans))
        ans = ans[::-1]
        return(Poly(ans), self - b * Poly(ans))
    
    def __rdivmod__(self, other):
        other = Poly(other)
        self = Poly(self)
        return divmod(other, self)
    
    def __floordiv__(self, other):
        other = Poly(other)
        self = Poly(self)
        a = divmod(self, other)
        return a[0]
    
    def __rfloordiv__(self, other):
        other = Poly(other)
        self = Poly(self)
        a = divmod(other, self)
        return a[0]
    
    def __ifloordiv__(self, other):
        self._coeff = (self // other)._coeff
        return self
    
    def __mod__(self, other):
        other = Poly(other)
        self = Poly(self)
        a = divmod(self, other)
        return a[1]
    
    def __rmod__(self, other):
        other = Poly(other)
        self = Poly(self)
        a = divmod(other, self)
        return a[1]
    
    def __imod__(self, other):
        self._coeff = (self % other)._coeff
        return self
X = Poly((0, 1))
exec(open('input.txt').read())