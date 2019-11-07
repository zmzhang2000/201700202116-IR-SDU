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
## Results
### digits
|        | time(s)   | NMI  | Homogeneity | Completeness |
| ------ | ------ |-------|---|---|
| K-means    |  0.57  |  0.623 | 0.600 | 0.647  |
| Affinity propagation   | 8.02  | 0.616  | 0.932 | 0.460 |
| Mean-shift   |  4.36 | 0.470  | 1.000 | 0.307 |
Spectral clustering | --- | --- | --- | --- |
| Ward hierachical clustering   | 0.38 | 0.796|0.758|0.836|
| Agglomeractive clustering   | 0.34|0.014|0.007|0.238|
| DBSCAN  |1.02|0.470|1.000|0.307|
| Gaussian Mixture   | 0.57|0.612|0.569|0.663|
### news
|        | time(s)   | NMI  | Homogeneity | Completeness |
| ------ | ------ |-------|---|---|
| K-means    | 0.81|0.251|0.210|0.314|
| Affinity propagation   | 9.67|0.408|0.483|0.354|
| Mean-shift   | 5.07|0.000|0.000|1.000|
Spectral clustering | --- | --- | --- | --- |
| Ward hierachical clustering   |0.24|0.213|0.149|0.376|
| Agglomeractive clustering   | 0.24|0.070|0.038|0.401|
| DBSCAN  |0.07|0.000|0.000|1.000|
| Gaussian Mixture   | 1.13|0.201|0.145|0.329|