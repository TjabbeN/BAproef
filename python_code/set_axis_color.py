import matplotlib.pyplot as plt

def set_axis_color(ax=None, color="#000000"):
    """Takes an axis object or uses the current axes, and a HEX color, and applies the color to the axes and plot border"""
    if ax is None:
        ax = plt.gca()  # Get current axes if no axis object is provided
    
    ax.spines['top'].set_color(color)
    ax.spines['bottom'].set_color(color)
    ax.spines['left'].set_color(color)
    ax.spines['right'].set_color(color)
    ax.xaxis.label.set_color(color)
    ax.yaxis.label.set_color(color)
    ax.tick_params(axis='x', colors=color)
    ax.tick_params(axis='y', colors=color)

