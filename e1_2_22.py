"""
Температура воздуха с учетом влияния ветра. Т - температура в граду­
сах Фаренгейта; v - скорость ветра в милях в час. Национальная служба
погоды определяет эффективную температуру воздуха (с учетом влия­
ния ветра) так:
w = 35.74 + 0.6215 * Т + (О.4275 * Т - 35.75) v ** 0.16
Составьте программу, получающую в аргументах командной строки два
значения, t и v типа float, и выводящую температуру воздуха с учетом
влияния ветра. Примечание: эта формула недопустима, если t больше 50
в абсолютном значении или если v больше 120 либо меньше 3 (подразу­
мевается, что вводимые значения находятся в этом диапазоне).
"""
import sys

t = float(sys.argv[1])
v = float(sys.argv[2])

if (t > 50):
    print("Недопустимое значение t")
    exit(0)

if ((v < 3) or (v > 120)):
    print("Недопустимое значение v")
    exit(0)

w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * (v ** 0.16)
print(w)