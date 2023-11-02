import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

def WordDistPlot(DataFrame, x:str, y:str, rank:int=20, palette:str='Greens_r',size:float=15,ratio:int=3)-> sns.barplot:  
    
    plt.figure(figsize=(size,size/ratio), dpi = 1080) 
    #sns.set(rc={'figure.figsize': (size,size/ratio)})
    sns.set_style("ticks")
    
    
    ax = sns.barplot(x=x, y=y, palette=palette, data=DataFrame.head(rank))
    ax.set_xlabel(x,fontsize=size*0.75,labelpad=10)
    ax.set_ylabel(y,fontsize=size*0.75,labelpad =10)
    ax.tick_params(labelsize=size*0.50,rotation=90)

    sns.despine(bottom = False, left = False)
    
    ax = ax
    return ax
