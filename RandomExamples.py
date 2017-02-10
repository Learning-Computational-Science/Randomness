import math

def format_plot(a):
    """Format a plot for presenation.  Function takes one parameter, a matplotlib.axes object."""

    goldenratio = 1 / 2 * (1 + math.sqrt(5))  # The next few lines are used for the size of plots
    fsx = 7  # Width (in inches) for the figures.
    fsy = fsx / goldenratio  # Height (in inches) for the figures.

    a.tick_params(labelsize=12)
    a.xaxis.label.set_size(14)
    a.yaxis.label.set_size(14)
    a.title.set_size(16)
    a.legend(fontsize=12)
    a.get_figure().set_size_inches(fsx, fsy)
    a.grid(1)