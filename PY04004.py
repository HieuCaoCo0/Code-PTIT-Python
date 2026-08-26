from math import gcd
class PhanSo:
    def __init__(self, x, y):
        self.tu = x
        self.mau = y
    def rutGon(self):
        ucln = gcd(self.tu, self.mau)
        self.tu //= ucln
        self.mau //= ucln
        return self
    def __add__(self, other):
        mau = self.mau * other.mau
        tu = self.tu*other.mau + self.mau*other.tu
        return PhanSo(tu, mau).rutGon()
    def __str__(self):
        return f'{self.tu}/{self.mau}'


x1, y1, x2, y2 = map(int, input().split())
p, q = PhanSo(x1, y1), PhanSo(x2, y2)
r = p.rutGon() + q.rutGon()
print(r)
    