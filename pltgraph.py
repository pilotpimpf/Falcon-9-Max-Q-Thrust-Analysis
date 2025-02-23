import matplotlib.pyplot as plt
#%matplotlib qt

def plt_data(x, y, description = None):
    if not description == None: fig = plt.figure(num=description["title"],figsize=(6,4), dpi=100)
    else: fig = plt.figure(figsize=(6,4), dpi=100)

    if not type(y) == tuple:y = (y,)
    for i in y: plt.plot(x, i)
    
    if not description == None:
        plt.xlabel(description["xLable"])
        plt.ylabel(description["yLable"])
        plt.title(description["title"])
        if not description.get("ylims")  == None: plt.ylim(description["ylims"][0], description["ylims"][1])
    plt.ticklabel_format(style="plain")
    fig.patch.set_facecolor('xkcd:white')
    plt.show()