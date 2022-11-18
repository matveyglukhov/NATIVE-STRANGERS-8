import random
import logging

logging.basicConfig(filename='log.log', level=logging.INFO)

while True:
    try:
        a = int(input("Ввведите число бочонков:"))
        assert a > 0
        logging.info('correct number input, n = {}'.format(a))
        break
    except AssertionError:
        print('Число обязательно должно быть натуральным')
        logging.exception("num isn't natural")
    except ValueError:
        print('Некорректный ввод')
        logging.exception('wrong num input')
list = [i for i in range(1, a + 1)]
random.shuffle(list)
print('Нажмите Enter чтобы вывести число', end='')
for elem in list:
    b = input()
    print(elem, end='')