# PY_MLClusterProjector
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


def brain_projector():
    """
    Loads a CSV file based on a provided filepath and plots the given xyz coordinates onto a 3D space.

    :return: None
    """

    # User greeting
    print("\nHey Colin! This is brain_projector(). \nBooting up protocol now...")

    # Asking for filepath to be analyzed
    filepath = input("\nEnter file you would like to 3D map: ")

    # Loading CSV file with pandas package
    df = pd.read_csv(filepath, header=0, float_precision='high')

    # Printing head table to ensure proper loading of data
    print(f"\nHEAD TABLE OF LOADED DATA FRAME: {filepath}")
    print(df.head())

    # Asking what cluster parameter/ID to label
    print("\nOf the 4 options: {4, 6, 8, 13}...")
    cluster_choice = input("How many clusters would you like to visualize?: ")
    if cluster_choice == '4':
        cluster_id = df['4_clusters']
    elif cluster_choice == '6':
        cluster_id = df['6_clusters']
    elif cluster_choice == '8':
        cluster_id = df['8_clusters']
    elif cluster_choice == '13':
        cluster_id = df['13_clusters']
    else:
        print("Invalid cluster choice. Play nice :( ")
        return

    # Extracting x, y, z coordinates
    x = df['X']
    y = df['Y']
    z = df['Z']

    # Create a 3D scatter plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Scatter plot with colored points based on cluster_id
    scatter = ax.scatter(x, y, z, c=cluster_id, cmap='viridis')

    # Customize the plot
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    # Add a colorbar
    colorbar = fig.colorbar(scatter, ax=ax, label='Cluster ID')

    # Show the plot
    plt.show()


if __name__ == '__main__':
    brain_projector()

