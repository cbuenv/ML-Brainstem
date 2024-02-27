# PY_MLBrainHACk
# Colin Buenvenida


# Importing global packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import plotly.graph_objects as go

# Choosing a matplotlib backend to ensure plot pop-up will deploy
import matplotlib
matplotlib.use('TkAgg')


def brain_hac():
    """
    Loads a CSV file based on provided filepath and performs hierarchical agglomerative clustering based on
    the data frame contained.

    :return: None
    """

    # User greeting
    print("\nHey Colin! This is brainHACk2(). Booting up protocol now...")

    # Asking for filepath to be analyzed
    filepath = input("\nEnter file to be HAC_ked: ")

    # Loading CSV file with pandas package
    df = pd.read_csv(filepath, header=0, float_precision='high')

    # Printing head table to ensure proper loading of data
    print(f"\nHEAD TABLE OF LOADED DATA FRAME: {filepath}")
    print(df.head())

    # Pulling summary statistics and initial size of data frame
    print("\nSUMMARY STATISTICS OF LOADED DATA FRAME:")
    print(df.describe())
    print("\nOVERALL SIZE OF LOADED DATA FRAME")
    print(df.shape)
    print("MAXIMUM:", df.max().max(), "@", df.max().idxmax())
    print("MINIMUM:", df.min().min(), "@", df.min().idxmin())

    # Generate dendrogram
    linkage_matrix = linkage(df.T, method='ward')  # Transpose the DataFrame for gene-wise clustering
    plt.figure(figsize=(15, 8))
    dendrogram(linkage_matrix, labels=df.columns, leaf_rotation=90)
    plt.title("Dendrogram")
    plt.show(block=True)

    # Initialize PCA with a range of components
    n_components = min(df.shape[0], df.shape[1])
    pca = PCA(n_components=n_components)
    pca.fit(df)

    # Calculate the cumulative explained variance
    cumulative_variance = np.cumsum(pca.explained_variance_ratio_)

    # Calculate the rate of change in the cumulative explained variance
    rate_of_change = np.diff(cumulative_variance)

    # Plot the knee plot
    plt.figure(figsize=(10, 6))
    plt.plot(np.arange(1, n_components), rate_of_change, marker='o')
    plt.title('Knee Plot for PCA')
    plt.xlabel('Number of Principal Components')
    plt.ylabel('Rate of Change in Cumulative Explained Variance')
    plt.grid(True)
    plt.show(block=True)
