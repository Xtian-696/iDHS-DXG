from sklearn.decomposition import TruncatedSVD
svd = TruncatedSVD(n_components =140,random_state=42).fit_transform(dataset)
