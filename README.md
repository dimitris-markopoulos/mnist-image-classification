# MNIST Project

This repository presents two complementary analyses on the MNIST handwritten digits dataset:

---

## Part 1 – Classical Classification Methods  
**Notebook:** `notebooks/MNIST_ImageClassification.ipynb`  
**Report (PDF):** [View here](./notebooks/01_MNIST_ImageClassification_Report.pdf), [View here](./notebooks/03_GroupLassoMultinomialRegressionReport.pdf)

This section compares classical supervised classifiers including Logistic Regression (OVR & Multinomial), LDA, Naive Bayes, and Linear SVM on digits {3, 5, 8}.  
Multinomial Regression achieved the best accuracy (~93.8%) while maintaining interpretability. Runtime trade-offs were also analyzed.  

A secondary experiment using Group LASSO Multinomial Regression introduced structured feature selection and spatial grouping of pixels, improving interpretability and runtime efficiency.  

These results are summarized in `mnist.pdf`, which includes detailed comparisons, confusion matrices, and reflections on model behavior.

---

## Part 2 – Unsupervised Representation Learning  
**Website:** [View Interactive Report](https://dimitris-markopoulos.github.io/mnist-image-classification/)

This section explores linear (PCA, NMF, ICA) and non-linear (Kernel PCA, Spectral Embedding, t-SNE, UMAP, Autoencoder) dimensionality reduction methods.  
Each technique was tuned using downstream KNN or K-means evaluations, and assessed quantitatively with the Adjusted Rand Index (ARI).  

**Key Finding:**  
UMAP achieved the strongest performance, yielding the highest ARI (~0.51) and producing the most interpretable 2D manifold visualization.  

---

## Summary
| Part | Focus | Core Method | Best Performer | Deliverable |
|------|--------|--------------|----------------|--------------|
| 1 | Supervised Classification | Logistic & Group LASSO Regression | Multinomial Regression (~93.8%) | `mnist.pdf` |
| 2 | Unsupervised Dimensionality Reduction | UMAP, t-SNE, Kernel PCA, etc. | UMAP (ARI ≈ 0.51) | Interactive HTML report |

---

**Note:**  
Part 1 is provided as a static PDF report located in the `notebooks` subfolder.  
Part 2 is hosted as a live interactive visualization via GitHub Pages.

