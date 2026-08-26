from sys import exit

class Rectangle:
    def __init__(self, l, w, c):
        self.l = l
        self.w = w
        self.c = c
    def perimeter(self):
        per = (self.l + self.w)*2
        return int(per)
    def area(self):
        area = self.l * self.w
        return area
    def color(self):
        f = self.c[:1].upper() + self.c[1::].lower()
        return f

arr = input().split()
r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
if r.l <= 0 or r.w <= 0:
    print('INVALID')
else:
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
exit()


# ham main dau bai sai
if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), int(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))