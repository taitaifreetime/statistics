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
        fontsize: int = 12, 
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
        fontsize (int): . Defaults to 12.
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

    fig, ax = plt.subplots(figsize=(8, 6))
    plt.rcParams["font.size"] = fontsize
    mean = data.mean().values
    sd = data.std().values
    for i, level in enumerate(levels):
        ax.bar(hist_list[i], mean[i], yerr=sd[i], capsize=5, ecolor='black', label=f"{level}", width = 0.7)
    
    flags = [False]*len(alphas)
    bracket_lists, flags = get_bracket(levels, pvalues, alphas, stars)
    annotate_brackets(bracket_lists, hist_list, mean+sd//2, dh=0.2, barh=0.03, fs=fontsize)

    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_xticks([])
    ax.set_ylabel(ylabel, fontsize=fontsize)
    ax.set_ylim(0, (max(data.max())+max(sd)//2)*1.5)
    ax.set_title(title)
    level_legend = ax.legend(loc='upper left', frameon=False)
    sig_labels = []
    for flag, star, alpha in zip(flags, stars, alphas):
        if flag:
            sig_labels.append(f"{star}(p<{alpha})")

    if sig_labels:
        custom_lines = [Line2D([0], [0], color='black', linestyle='none', marker='') for _ in sig_labels]
        ax.legend(custom_lines, sig_labels, loc='upper right', frameon=False)
        ax.add_artist(level_legend)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.savefig(save_path+"/"+title + ".png")
    plt.close(fig)

def main():
    np.random.seed(10)
    data = pd.DataFrame({
        'A': np.random.normal(8, 1, 30),
        'B': np.random.normal(10, 2, 30),
        'C': np.random.normal(9, 3, 30)
    })
    print(data.describe())

    from scipy.stats import ttest_ind
    pvalues = {
        ('A', 'B'): ttest_ind(data['A'], data['B']).pvalue,
        ('A', 'C'): ttest_ind(data['A'], data['C']).pvalue,
        ('B', 'C'): ttest_ind(data['B'], data['C']).pvalue,
    }
    print(pvalues)

    alphas = [0.001, 0.01, 0.05]
    stars = ['***', '**', '*']

    plot_hist_bracket(
        data=data,
        pvalues=pvalues,
        alphas=alphas,
        stars=stars,
        xlabel="Level",
        ylabel="Prob",
        title="Comparison",
        save_path="."
    )

if __name__ == "__main__":
    main()