# Clustering with sklearn
## Datasets
* sklearn.datasets.load_digits
* sklearn.datasets.fetch_20newsgroups
## Algorithm
* K-Means
* Affinity propagation
* Mean-shift
* Spectral clustering
* Ward hierarchical clustering
* Agglomerative clustering
* DBSCAN
* Gaussian mixtures
## Evaluation
* labels_true and labels_pred
    ```python
    from sklearn import metrics
    labels_true = [0, 0, 0, 1, 1, 1]
    labels_pred = [0, 0, 1, 1, 2, 2]
    ```
* Normalized Mutual Information (NMI)
    ```python
    metrics.normalized_mutual_info_score(labels_true, labels_pred)
    ```
* Homogeneity: each cluster contains only members of a single class
    ```python
    metrics.homogeneity_score(labels_true, labels_pred)
    ```
* Completeness: all members of a given class are assigned to the same cluster
    ```python
    metrics.completeness_score(labels_true, labels_pred)
    ```
## Examples
* A demo of K-Means clustering on the
handwritten digits data
    * https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html#sphx-glr-auto-examples-cluster-plot-kmeans-digits-py
* Clustering text documents using kmeans
    * https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html#sphx-glr-auto-examples-text-plot-document-clustering-py
