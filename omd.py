# Guido van Rossum <guido@python.org>
import random

def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print('Она посомневалась, но все-таки взяла зонтик.')
    print('Когда она вышла оказалось, что зонт сломан и она решила подбросить монету,')
    print('чтобы понять вернуться ли ей домой за другим или пойти в бар,надеясь что будет солнечно')
    print('Она больше хотела не возвращаться домой,но все в ваших руках')
    option = ''
    options2 = ['Орел', 'Решка']
    while option not in options2:
        print('Выберите: {}/{}'.format(*options2))
        option = input()
    if option == 'Орел':
        other_option = 'Решка'
    else:
        other_option = 'Орел'
    print(f'{option} - не возвращаться домой, {other_option} - вернуться домой')
    result = random.choice(options2)
    print('иииииииииии')
    if result == option:
        print(f'Ура {option}')
        return step3_bar()
    else:
        print(f'О нет {other_option}, ладно зайду за другим зонтом ')
        return step3_home()


def step2_no_umbrella():
    print('Не взяла она зонт и вдруг чувствует,что накрапывает дождь')
    print('чтобы спасти утку от ливня выберете число от 0 до 10')
    number = int(input())
    if number % 2 == 0:
        print('Дождь перестал капать и утка отправилась в бар')
        return step3_bar()
    else:
        print('К сожалению наши старания не помогли, уточке придется вернутся домой')
        return step3_home()


def step3_bar():
    print('Поздравляю тебя читатель, твоя утка добралась до бара')
    drinks = {'сок': '100', 'лимонад': '200', 'что-то покрепче': '300'}
    print('Она взяла меню:')
    for i in drinks.items():
        print(*i)
    print('Она конечно же выбрала что-то покрепче, потому что день выдался трудным, ')
    print('а что было дальше она и сама не помнит')


def step3_home():
    print('Очень злая утка вернулась домой и задумалась,а так ли ей нужно в этот бар,может лечь спать?')
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        print('"Хороший выбор, кто знает что в этом баре, ')
        print('а сон меня ещё никогда не подводил",- подумала утка и сладко заснула')
        return
    return step3_bar()


if __name__ == '__main__':
    step1()
