"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def middle_value_algorithm(number: int = 1) -> int:
    """Для сравнения всегда предлагается середина диапазона, если загаданное 
    число отличается от предложенного числа, то диапазон уменьшается на 
    половину в ту сторону, в которую загаданное число отличае отличается 
    от предложенного.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Количество попыток.
    """
    
    predict_list = list(range(1, 101))

    count = 0
    predict_num = None
    while predict_num != number:
        count += 1
        predict_index = (len(predict_list)/2) - 1
        predict_num = predict_list[int(predict_index)]
        if predict_num > number:
            predict_list = predict_list[:int((predict_index))]
        else:
            predict_list = predict_list[int((predict_index+1)):]
            
    return count
    

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
