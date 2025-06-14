from vistats import annotate_brackets
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from matplotlib.lines import Line2D

def plot_hist_bracket(
        data: pd.DataFrame, 
        pvalues: dict, 
        alphas: list, 
        stars: list, 
        err_type: str = "std", 
        figsize: tuple = (8, 6), 
        fontsize: int = 14, 
        xlabel = "x", 
        ylabel = "y", 
        title = "Histogram with p bracket", 
        save_path = "."):
    """visualize histogram with brackets

    Args:
        data (pd.DataFrame): 
        pvalues (dict): 
        alphas (list): significant thresholds [0.001, 0.01, 0.05]
        stars (list): ["***", "**", "*"]
        err_type (str, optional): . Defaults to "std".
        figsize (tuple, optional): . Defaults to (8,6).
        fontsize (int, optional): . Defaults to 14.
        xlabel (str, optional): . Defaults to "x".
        ylabel (str, optional): . Defaults to "y".
        title (str, optional): . Defaults to "Histogram with p bracket".
        save_path (str, optional): . Defaults to ".".
    """

    def get_bracket(levels: list, pvalues: dict, alphas: list, stars: list, offset: int=0):
        """get bracket only if p is less than alpha threshold

        Args:
            levels (list): 
            pvalues (dict): 
            alphas (list): significant thresholds [0.001, 0.01, 0.05]
            stars (list): ["***", "**", "*"]
            offset (int, optional): _description_. Defaults to 0.

        Returns:
            bracket list and flag for each significant level
        """
        bracket_list = []
        flags = [False]*len(levels) 
        used_pairs = []
        for pair in pvalues.keys():
            cond1, cond2 = pair
            p = pvalues[pair]
            for i, (star, alpha) in enumerate(zip(stars, alphas)):
                if p < alpha:
                    flags[i] = True
                    idx1 = levels.index(cond1)+offset
                    idx2 = levels.index(cond2)+offset
                    bracket_list.append((idx1, idx2, star))
                    used_pairs.append((idx1, idx2))
                    break
        return bracket_list, flags

    num_levels = len(data)
    hist_list = np.arange(num_levels)
    levels = list(data.columns[:])
    fig, ax = plt.subplots(figsize=figsize, constrained_layout=True) # auto space adjustment 
    plt.rcParams["font.size"] = fontsize
    mean = data.mean().values
    err = []
    if   err_type == "std": err = data.std().values
    elif err_type == "sem": err = data.sem().values
    else:                   err = data.std().values

    # visualization setting
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_xticks([])
    ax.set_ylabel(ylabel, fontsize=fontsize)
    ax.set_title(title)
    ax.set_ylim(0, (max(data.max())+max(err)//2)*2)

    # draw histogram
    for i, level in enumerate(levels):
        ax.bar(hist_list[i], mean[i], yerr=err[i], capsize=5, ecolor='black', label=f"{level}", width = 0.7)
    
    # draw significant level
    flags = [False]*len(alphas)
    bracket_lists, flags = get_bracket(levels, pvalues, alphas, stars)
    annotate_brackets(
        bracket_lists, 
        hist_list, 
        mean+err, 
        dh=0.03,    # offset, mean+err+dh = bracket height 
        barh=0.015, # length of legs of bracket
        fs=fontsize)

    # legend for type of data and significant levels
    level_legend = ax.legend(loc='upper left', frameon=False, prop={'family': 'monospace'})
    sig_labels = []
    max_star_len = max(len(s) for s in stars)                # used to arange length of legend text
    max_alpha_len = max(len(str(alpha)) for alpha in alphas) # used to arange length of legend text
    for flag, star, alpha in zip(flags, stars, alphas):
        if flag:
            sig_labels.append(f"{star.ljust(max_star_len)} ($p$ < {str(alpha).ljust(max_alpha_len)})")

    if sig_labels:
        custom_lines = [Line2D([0], [0], color='black', linestyle='none', marker='') for _ in sig_labels]
        ax.legend(custom_lines, sig_labels, loc='upper right', frameon=False, prop={'family': 'monospace'})
        ax.add_artist(level_legend)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.savefig(save_path+"/"+title + ".png")
    plt.close(fig)

def main():
    np.random.seed(10)
    data = pd.DataFrame({
        'A': np.random.normal(8, 1, 20),
        'B': np.random.normal(10, 2, 20),
        'C': np.random.normal(9, 3, 20),
        'D': np.random.normal(12, 0.5, 20)
    })
    print(data.describe())

    from scipy.stats import ttest_ind
    pvalues = {
        ('A', 'B'): ttest_ind(data['A'], data['B']).pvalue,
        ('A', 'C'): ttest_ind(data['A'], data['C']).pvalue,
        ('A', 'D'): ttest_ind(data['A'], data['D']).pvalue,
        ('B', 'C'): ttest_ind(data['B'], data['C']).pvalue,
        ('B', 'D'): ttest_ind(data['B'], data['D']).pvalue,
        ('C', 'D'): ttest_ind(data['C'], data['D']).pvalue,
    }
    print(pvalues)

    alphas = [0.001, 0.01, 0.05]
    stars = ['***', '**', '*']

    plot_hist_bracket(
        data=data,
        pvalues=pvalues,
        alphas=alphas,
        stars=stars,
        err_type="std",
        figsize=(8,8),
        xlabel="Level",
        ylabel="Prob",
        title="Comparison",
        save_path="../results"
    )

if __name__ == "__main__":
    main()