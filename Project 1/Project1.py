import numpy as np
def predict(number= np.random.randint(1, 101)) -> int:
    i = 0
    left=1
    right=101
    b=(left+right)//2
    
    while True:
        b=(left+right)//2
        i+=1
        if b>number:
            right=b
        elif b<number:
            left=b
        else:
            break
    return i

def score_game(predict) -> int:

    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  
    for number in random_array:
        count_ls.append(predict(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    
    score_game(predict)

