import random
import logging

logging.basicConfig(filename='loto_log.log', level=logging.INFO)

while True:
    try:
        N = int(input("Введите натуральное число: "))
        assert N > 0
        logging.info('correct number input, n = {}'.format(N))
        break
    except AssertionError:
        print('Число должно быть натуральным !')
        logging.exception("num isn't natural")
    except ValueError:
        print('Неверный ввод')
        logging.exception('wrong num input')
N_list = [i for i in range(1, N + 1)]
random.shuffle(N_list)
print('Нажмите Enter чтобы увидеть число', end='')
for element in N_list:
    a = input()
    print(element, end='')