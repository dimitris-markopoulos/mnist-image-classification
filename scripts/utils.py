import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import StandardScaler

def create_data():
    """
    Returns X, y
    """
    mnist = fetch_openml("mnist_784")
    X, y = mnist.data, mnist.target.astype(int)

    print(X.shape)
    print(y.shape)
    return X, y

def plot_image(vec, ax=None, cmap='gray'):
    """Display one digit image from a flattened 784-vector."""
    mat = np.reshape(vec[:784], (28, 28))
    if ax is None:
        plt.imshow(mat, cmap=cmap)
        plt.axis('off')
    else:
        ax.imshow(mat, cmap=cmap)
        ax.axis('off')

def plot_5by5_images(X : pd.DataFrame, path : str):
    scaler = StandardScaler(with_std=False)
    X_centered = scaler.fit_transform(X) # Center only
    print(f"Data shape: {X.shape}")

    fig, axes = plt.subplots(5, 5, figsize=(8, 8))
    rand_idx = np.random.choice(len(X), size=25, replace=False)

    for ax, idx in zip(axes.ravel(), rand_idx):
        plot_image(X.iloc[idx], ax=ax, cmap='gray')

    plt.tight_layout()
    plt.savefig(path)
    # plt.show()

if __name__ == '__main__':
    X, y = create_data()

    path = 'docs/digits_initial_viz.png'
    plot_5by5_images(X=X, path=path)