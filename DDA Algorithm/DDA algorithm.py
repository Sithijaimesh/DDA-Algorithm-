import matplotlib.pyplot as plt

def my_round(a):
    return int(a + 0.5)

def dda(x1, y1, x2, y2):
    x, y = x1, y1

    xx, yy = x1, y1

    xx, yy = [] , []

    length = abs((x2 - x1) if abs(x2 - x1) > abs(y2 - y1) else (y2 - y1))

    dx = (x2 - x1) / float(length)
    dy = (y2 - y1) / float(length)
    print(my_round(x), my_round(y))
    xx.append(my_round(x)); yy.append(my_round(y))
    for i in range(length):
        x += dx
        y += dy
        print(my_round(x), my_round(y))
        xx.append(my_round(x)); yy.append(my_round(y))

    return xx, yy

x_cords, y_cords = dda(20, 20, 60, 50)
print(list(zip(x_cords, y_cords)))

plt.scatter(x_cords, y_cords, color="green", s=50)
plt.title("DDA Line Drawing Algorithm")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.show()