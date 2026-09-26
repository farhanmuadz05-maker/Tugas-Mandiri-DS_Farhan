import streamlit as st
import pandas as pd

st.title("Clustering Karakteristik Wilayah Kota Bogor")

# Membaca hasil clustering
df = pd.read_csv("hasil_clustering_kota_bogor.csv")

st.subheader("Data Hasil Clustering")
st.dataframe(df)

st.subheader("Jumlah Data Setiap Cluster")

cluster_count = df["Cluster"].value_counts().sort_index()

st.bar_chart(cluster_count)

st.subheader("Rata-rata Karakteristik Setiap Cluster")

features = [
    "Jumlah_Penduduk",
    "Kepadatan_Penduduk",
    "Jumlah_UMKM",
    "Jumlah_Sekolah",
    "Fasilitas_Kesehatan",
    "Fasilitas_Olahraga",
    "Jumlah_Restoran",
    "Ruang_Terbuka",
    "Jumlah_Kendaraan"
]

cluster_summary = df.groupby("Cluster")[features].mean()

st.dataframe(cluster_summary)