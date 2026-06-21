import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Data Mining Penjualan", layout="wide")

st.title("📊 Dashboard Data Mining Penjualan")

df = pd.read_csv("sales_data_500.csv")

df["Total Penjualan"] = df["Harga"] * df["Jumlah"]

st.subheader("Dataset Penjualan")
st.dataframe(df)

st.subheader("Statistik Data")
st.write(df.describe())

st.subheader("Filter Data")
wilayah = st.multiselect(
    "Pilih Wilayah",
    options=df["Wilayah"].unique(),
    default=df["Wilayah"].unique()
)

df_filter = df[df["Wilayah"].isin(wilayah)]

col1, col2 = st.columns(2)

with col1:
    st.subheader("Total Penjualan per Produk")
    produk = df_filter.groupby("Produk")["Total Penjualan"].sum().sort_values()
    fig, ax = plt.subplots(figsize=(8,5))
    produk.plot(kind="barh", ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("Total Penjualan per Wilayah")
    wilayah_data = df_filter.groupby("Wilayah")["Total Penjualan"].sum()
    fig2, ax2 = plt.subplots(figsize=(6,6))
    wilayah_data.plot(kind="pie", autopct="%1.1f%%", ax=ax2)
    ax2.set_ylabel("")
    st.pyplot(fig2)

st.subheader("10 Transaksi dengan Penjualan Terbesar")
top = df_filter.sort_values("Total Penjualan", ascending=False).head(10)
st.dataframe(top)
