# Hippocampus Size Analysis Project

## Overview

This project aims to analyze the differences in hippocampus size between two groups: "Unaffect" and "Affected". Using data from an `.rda` file, the project calculates statistical measures and visualizes the distribution of values for both groups.

## Features

- **Statistical Analysis**: Calculation of mean, variance, and median for each group.
- **Data Visualization**: Histograms, empirical distribution functions (ECDF), and kernel density estimates (KDE) for visualizing the data distribution.
- **Empirical Distribution Functions**: Both ECDF and PDF are plotted for a detailed understanding of data distribution.

## Core Components

### `hypocampus_size.ipynb`
- A Jupyter notebook for interactive data analysis and visualization.
- Allows users to explore the data and perform statistical analysis in an interactive manner.

## Dependencies

Ensure the following Python packages are installed:

- `pyreadr`
- `pandas`
- `matplotlib`
- `numpy`
- `seaborn`
- `statsmodels`

You can install the dependencies using pip:

```bash
pip install pyreadr pandas matplotlib numpy seaborn statsmodels
```
## Usage

1. **Data Loading**: The data is read from a specified `.rda` file and divided into two groups: "Unaffect" and "Affected".

2. **Statistical Calculations**: The notebook includes functions to calculate the mean, variance, and median for each group's standard deviation.

3. **Data Visualization**: The notebook provides cells to generate histograms, ECDF, and KDE plots for both groups.

## Running the Notebook

To use the notebook:

1. Open `hypocampus_size.ipynb` in Jupyter Notebook or JupyterLab.

2. Run the cells in sequence to load the data, perform statistical calculations, and visualize the results.

### Example Code

Example code snippets provided in the notebook include:

```python
# Example for statistical calculations

group_unaffect = df['Unaffect']
group_affected = df['Affected']

unaffect_stats = calculate_stats(group_unaffect)
affected_stats = calculate_stats(group_affected)
```
