from math import gcd

class PhanSo:
    def __init__(self, x, y):
        self.tu = x
        self.mau = y
    def rutGon(self):
        ucln = gcd(self.tu, self.mau)
        self.tu //= ucln
        self.mau //= ucln
    def out(self):
        print(f'{self.tu}/{self.mau}')

x, y = map(int, input().split())
p = PhanSo(x, y)
p.rutGon()
p.out()
