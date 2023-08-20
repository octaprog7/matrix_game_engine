import mge
import random
import time


if __name__ == '__main__':
    figures = "Камень|Rock", "Ножницы|Scissor", "Бумага|Paper"
    mge = mge.MetrixGameEngine(figures)
    mge.make_losers(figures[0], (figures[1],))     # для камня, проигравшим является ножницы
    mge.make_losers(figures[1], (figures[2],))     # для ножниц, проигравшим является бумага
    mge.make_losers(figures[2], (figures[0],))     # для бумаги, проигравшим является камень
    print("-----Фигуры-----")
    for item in mge.figures():
        print(item)
    print(16 * "-")
    cnt = 0
    while True:
        a, b = random.choice(figures), random.choice(figures)
        if a == b:
            continue
        winner = mge.solve(a, b)
        cnt += 1
        time.sleep(3)
        print(f"Шаг|Step: {cnt}. {a} против|vs {b}. Победитель|Winner: {winner}")
