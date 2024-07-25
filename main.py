import pyreadr
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import statsmodels.api as sm
# For each group, calculate mean, variance, and median of the standard deviation

def calculate_stats(group):
    mean_std = round(group.mean(), 3)
    var_std = round(group.var(), 3)
    median_std = round(group.median(), 3)
    return mean_std, var_std, median_std


if __name__ == "__main__":
    # Specify the path to your .rda file
    rda_file_path = 'data/case0202.rda'
    # Read the .rda file into a Pandas DataFrame
    result = pyreadr.read_r(rda_file_path)
    # Access the DataFrame from the result
    df = result['case0202']
    # Divide the DataFrame into two groups
    group_unaffect = df['Unaffect']
    group_affected = df['Affected']
    # Describe the data and the problem under study
    # You may print additional information about the groups if needed
    print("Group 'Unaffect':")
    print(group_unaffect.describe())
    print("\nGroup 'Affected':")
    print(group_affected.describe())
    # Calculate statistics for 'Unaffect' group
    unaffect_stats = calculate_stats(group_unaffect)
    # Calculate statistics for 'Affected' group
    affected_stats = calculate_stats(group_affected)
    # Print the results
    print("\nStatistics for 'Unaffect' group:")
    print("Mean of the corresponding Deviation:", unaffect_stats[0])
    print("Variance of the corresponding Deviation:", unaffect_stats[1])
    print("Median of the corresponding Deviation:", unaffect_stats[2])
    print("\nStatistics for 'Affected' group:")
    print("Mean of the corresponding Deviation:", affected_stats[0])
    print("Variance of the corresponding Deviation:", affected_stats[1])
    print("Median of the corresponding Deviation:", affected_stats[2])
    #=============================================================================
    #second task
    # Plot histograms for each group
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.hist(group_unaffect, bins=10, alpha=0.7, color='blue', label='Unaffect')
    plt.hist(group_affected, bins=10, alpha=0.7, color='orange', label='Affected')
    plt.title('Histograms')
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.legend()

    # Plot empirical distribution functions for each group
    plt.subplot(1, 2, 2)
    sorted_unaffect = np.sort(group_unaffect)
    sorted_affected = np.sort(group_affected)
    cdf_unaffect = np.arange(1, len(sorted_unaffect) + 1) / len(sorted_unaffect)
    cdf_affected = np.arange(1, len(sorted_affected) + 1) / len(sorted_affected)

    plt.plot(sorted_unaffect, cdf_unaffect, label='Unaffect', color='blue')
    plt.plot(sorted_affected, cdf_affected, label='Affected', color='orange')
    plt.title('Empirical Distribution Functions')
    plt.xlabel('Values')
    plt.ylabel('Cumulative Probability')
    plt.legend()

    plt.tight_layout()
    plt.show()


    #================

    # Plot KDE plots for each group with normalized PDF
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    kde_unaffect = sns.kdeplot(group_unaffect, label='Unaffect', color='blue', fill=True)
    kde_affected = sns.kdeplot(group_affected, label='Affected', color='orange', fill=True)

    # Normalize the KDE plots to represent PDF
    y_unaffect = kde_unaffect.get_lines()[0].get_data()[1]
    x_unaffect = kde_unaffect.get_lines()[0].get_data()[0]
    kde_unaffect.get_lines()[0].set_ydata(y_unaffect / np.trapz(y_unaffect, x_unaffect))

    y_affected = kde_affected.get_lines()[0].get_data()[1]
    x_affected = kde_affected.get_lines()[0].get_data()[0]
    kde_affected.get_lines()[0].set_ydata(y_affected / np.trapz(y_affected, x_affected))

    plt.title('Probability Density Function (PDF)')
    plt.xlabel('Values')
    plt.ylabel('Probability Density')
    plt.legend()

    # Plot ECDF plots for each group without vertical lines
    plt.subplot(1, 2, 2)
    ecdf_unaffect = sm.distributions.ECDF(group_unaffect)
    ecdf_affected = sm.distributions.ECDF(group_affected)

    x_unaffect = np.sort(group_unaffect)
    y_unaffect = ecdf_unaffect(x_unaffect)

    x_affected = np.sort(group_affected)
    y_affected = ecdf_affected(x_affected)

    plt.step(x_unaffect, y_unaffect, label='Unaffect', color='blue')
    plt.step(x_affected, y_affected, label='Affected', color='orange')
    plt.title('Empirical Cumulative Distribution Function (ECDF)')
    plt.xlabel('Values')
    plt.ylabel('Cumulative Probability')
    plt.legend()

    plt.tight_layout()
    plt.show()