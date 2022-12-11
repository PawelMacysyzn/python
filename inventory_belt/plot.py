import matplotlib.pyplot as plt
import numpy as np
from typing import List


def do_plot(list: List[str]) -> None:
    '''
    # Pie chart, where the slices will be ordered and plotted
    '''

    lbls = list
    sizes = [1 for _ in lbls]

    # Intended to serve something like a global variable
    class MyClass:
        i = 0

    def func(labels, vals):
        MyClass.i -= 1
        # Returns absolute value against the default percentage
        # absolute = int(pct/100.*np.sum(vals))
        # Combine labels and values
        return "{:s}\n".format(labels[MyClass.i])

    fig1, ax1 = plt.subplots()
    # Pie wedgeprops with width being the donut thickness
    ax1.pie(sizes, wedgeprops=dict(width=0.6), autopct=lambda pct: func(lbls, sizes),
            shadow=False, startangle=90)
    sumstr = 'Total size = '+str(np.sum(sizes))
    # String on the donut center
    ax1.text(0., 0., sumstr, horizontalalignment='center',
             verticalalignment='center')
    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.axis('equal')

    plt.show(block=False)
    plt.pause(1)
    plt.close()


