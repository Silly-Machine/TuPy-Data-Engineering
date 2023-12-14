import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

def WordDistPlot(DataFrame, x: str, y: str, rank: int = 20, palette: str = 'Greens_r', size: float = 15, ratio: int = 3) -> sns.barplot:
    """
    Generate a bar plot to visualize the distribution of words in a DataFrame.

    Parameters:
    - DataFrame (pd.DataFrame): The input DataFrame containing the data.
    - x (str): The column name for the x-axis.
    - y (str): The column name for the y-axis.
    - rank (int, optional): The number of top entries to display. Default is 20.
    - palette (str, optional): The color palette to use for the plot. Default is 'Greens_r'.
    - size (float, optional): The size of the plot. Default is 15.
    - ratio (int, optional): The aspect ratio of the plot. Default is 3.

    Returns:
    - sns.barplot: The Seaborn bar plot.

    Example:
    ```python
    WordDistPlot(my_dataframe, 'Word', 'Frequency', rank=15, palette='Blues', size=12, ratio=2)
    ```
    """
    plt.figure(figsize=(size, size / ratio), dpi=1080)
    sns.set_style("ticks")

    ax = sns.barplot(x=x, y=y, palette=palette, data=DataFrame.head(rank))
    ax.set_xlabel(x, fontsize=size * 0.75, labelpad=10)
    ax.set_ylabel(y, fontsize=size * 0.75, labelpad=10)
    ax.tick_params(labelsize=size * 0.50, rotation=90)

    sns.despine(bottom=False, left=False)

    return ax

