from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans,DBSCAN
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

# 300 örnekten 4 tane küme merkezinden 0.60 standart sapma (küme dağılım)
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=42)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Veriyi 2 boyuta indirgemek için PCA kullanıyoruz. Görselleştirme amacıyla.
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)


algorithms = {
    'KMeans' : KMeans(n_clusters=4,random_state=42), #4 küme
    'DBSCAN' : DBSCAN(eps=0.5, min_samples=5) # eps komşu kabul edilen maksimum uzaklık / min_samples bir küme için gereken minimum nokta sayısı
}

plt.figure(figsize=(15, 5))  # 15x5 boyutunda bir grafik penceresi oluştur

plt.subplot(131)  # 1 satır, 3 sütunluk grafik alanının 1. kısmını seç
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y)  # Orijinal veriyi çiz
plt.title('Original Data')  # Başlık ekle

for i, (name, algorithm) in enumerate(algorithms.items(), 2): # 2'den başla çünkü 1. subplot'u zaten kullandık
    labels = algorithm.fit_predict(X_scaled)

    plt.subplot(1, 3, i)  # i. grafik alanını seç
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='viridis')  # Küme etiketlerini çiz / viridis renk haritasını kullan
    plt.title(f'{name} Clustering')  # Algoritma adını başlığa yaz

plt.tight_layout()  # Grafikleri düzenle (overlap'ı önle)
plt.show()  # Grafikleri göster

inertias = []  # Inertia değerlerini saklamak için boş liste / Inertia, küme içi mesafelerin karelerinin toplamıdır
n_clusters_range = range(1, 11)  # Küme sayısı 1'den 10'a kadar

for n_clusters in n_clusters_range:
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)  # KMeans'i her küme sayısı için yeniden oluştur
    kmeans.fit(X_scaled)  # Veriyi kümelere ayır
    inertias.append(kmeans.inertia_)  # Inertia değerini listeye ekle

plt.figure(figsize=(8, 5))  # 8x5 boyutunda grafik penceresi
plt.plot(n_clusters_range, inertias, 'bo-')  # Mavi çizgi ve daire noktalarla çiz
plt.xlabel('Number of Clusters')  # X-ekseni etiketi
plt.ylabel('Inertia')  # Y-ekseni etiketi
plt.title('Elbow Method for Optimal k')  # K-Means için optimal grup sayısını belirler
plt.show()  # Grafiği göster