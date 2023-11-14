import matplotlib.pyplot as matplt

def plt(x, y, label, xlabel, ylabel, lim, path):
    matplt.style.use("default")

    fig, ax = matplt.subplots(
        figsize = (12, 8)
    )

    for i in range(0, len(x)):
        ax.plot(x[i], y[i], linewidth=2.0, label = label[i])

    ax.set(ylim = lim)
    ax.grid(True)

    ax.legend(loc = "lower right", framealpha = 0.8, edgecolor = "black", fontsize = 14)

    ax.tick_params(labelsize = 14)

    ax.set_xlabel(xlabel, fontsize = 16)
    ax.set_ylabel(ylabel, fontsize = 16)

    fig.tight_layout()

    matplt.savefig(path, dpi = 300)
    matplt.close()
