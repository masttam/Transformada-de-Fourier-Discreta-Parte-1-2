import matplotlib.pyplot as plt


def continuous_plotter(t, x, title="x(t)"):
    fig = plt.figure()
    plt.plot(t, x)
    plt.title(title)
    plt.xlabel("t [s]")
    plt.ylabel("Amplitud")
    plt.grid(True)
    return fig


def discrete_plotter(f, y, title="|X(f)|"):
    fig = plt.figure()
    plt.stem(f, y)  # corregido: sin use_line_collection
    plt.title(title)
    plt.xlabel("f [Hz]")
    plt.ylabel("Amplitud (aprox.)")
    plt.grid(True)
    return fig

