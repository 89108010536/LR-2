print('Решаем уравнение a•x²+b•x+c=0')
def get_number(s):
    while True:
        try:
            return float(input(s))
        except:
            print("Это не число.")

a = get_number('Введите значение a: ')
b = get_number('Введите значение b: ')
c = get_number('Введите значение c: ')
print(f"{a}·x²+{b}·x+{c}=0")

discriminant = b**2 - 4*a*c
print('Дискриминант = ' + str(discriminant))
if discriminant < 0:
    print('Корней нет')
elif discriminant == 0:
    x = -b / (2 * a)
    print('x = ' + str(x))
else:
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    print('x₁ = ' + str(x1))
    print('x₂ = ' + str(x2))