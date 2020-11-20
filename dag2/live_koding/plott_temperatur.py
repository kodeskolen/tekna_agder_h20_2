
#from matplotlib.pyplot import *
#from matplotlib.pyplot import plot, legend, grid, ylim, title, show, figure

import matplotlib.pyplot as plt

mnd = ["januar", "februar", "mars", "april", "mai",
       "juni", "juli", "august", "september",
       "oktober", "november", "desember"]

tmp_2018 = [-10, -5.5, 0.3, 5.5, 10.4, 12.8, 16.1, 15.3,
       10.1, 8.7, 4.2, -1.3]
tmp_2019 = [-4, -6.5, 1.3, 4.2, 12.4, 14.8, 12.1, 13.3,
       7.1, 5.7, 2.2, -5.3]

plt.figure(figsize=(13, 6))

plt.plot(mnd, tmp_2018, "o-", label="2018")
plt.plot(mnd, tmp_2019, "o-", label="2019")
plt.legend()
plt.grid()
plt.ylim(-20, 20)

plt.title("Temperatur")

plt.show()



