import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(0, 1, 500)

# Successione di funzioni

for n in [1, 2, 5, 10]:

    plt.plot(

        x,

        x**(1/n),

        linewidth=1.5,

        label=fr"$f_{{{n}}}(x)=x^{{\frac{{1}}{{{n}}}}}$"

    )

# Funzione limite

x_lim = np.linspace(0, 1, 499)

plt.plot(

    x_lim,

    np.ones_like(x_lim),

    linewidth=4,

    label=r"$f(x)=1,\quad x\in]0,1]$",

    color="black"

)

# Punto (1,1) della funzione limite

plt.plot(

    0, 0,

    marker="o",

    markersize=8,

    label=r"$f(0)=0$",

    color="black"

)

plt.xlabel(r"$x$")

plt.ylabel(r"$f_n(x)$")

plt.title(r"Successione $f_n(x)=x^{\frac{1}{n}}$ e funzione limite")

plt.grid(True)

plt.legend()

plt.xlim(-0.05, 1)

plt.ylim(-0.05, 1.05)


plt.savefig("Appunti/img/succ_funz_3.png")