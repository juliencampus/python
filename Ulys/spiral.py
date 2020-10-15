import math

import matplotlib.pyplot as plt


with open("spiral.dat", "a") as rfp:
    sigma = 0
    radius = 0.5

    while sigma < 4*math.pi:
        x = math.cos(sigma) * radius
        y = math.sin(sigma) * radius
        rfp.write(f"{x}   {y}\n")
        sigma += 0.1
        radius += 0.1


x = []
y = []
with open("spiral.dat", "r") as f_in:
    for line in f_in:
        coords = line.split()
        x.append(float(coords[0]))
        y.append(float(coords[1]))

plt.figure(figsize=(8, 8))
mini = min(x + y) * 1.2
maxi = max(x + y) * 1.2
plt.xlim(mini, maxi)
plt.ylim(mini, maxi)
plt.plot(x, y)
plt.savefig("spirale.png")