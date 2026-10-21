import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

NAMA = "Mohammad Alif Rachman Setiaji"
NIM = "241041009"

st.set_page_config(page_title="Kasus 3 - Cuaca", layout="wide")
st.title("Kasus 3: Dataset Pengamatan Cuaca")
st.caption(f"Nama: {NAMA}  |  NIM: {NIM}")

rng = np.random.default_rng(3)
n = 40
kota = rng.choice(["Jakarta", "Bandung", "Surabaya", "Medan"], n)
base = {"Jakarta": 32, "Bandung": 25, "Surabaya": 33, "Medan": 30}
df = pd.DataFrame({
    "Kota": kota,
    "Suhu (°C)": [round(base[k] + rng.normal(0, 1.5), 1) for k in kota],
    "Kelembaban (%)": rng.integers(60, 95, n),
    "Kondisi": rng.choice(["Cerah", "Berawan", "Hujan"], n),
})

st.subheader("Data")
st.dataframe(df, use_container_width=True)

st.subheader("Diagnostik Tipe Data")
st.table(pd.DataFrame({
    "Kolom": df.columns,
    "Tipe": ["Kategorik", "Numerik", "Numerik", "Kategorik"],
    "Skala": ["Nominal", "Interval (0°C bukan 'tanpa suhu')", "Rasio (0% = tidak ada kelembaban)", "Nominal"],
    "Visualisasi": ["Bar/Pie Chart", "Histogram/Scatter", "Histogram/Scatter", "Bar/Pie Chart"],
}))

c1, c2 = st.columns(2)
c1.plotly_chart(px.bar(df["Kondisi"].value_counts().reset_index(), x="Kondisi", y="count",
                title="Jumlah Pengamatan per Kondisi (Bar - Nominal)"), use_container_width=True)
c2.plotly_chart(px.pie(df, names="Kota", title="Proporsi Pengamatan per Kota (Pie - Nominal)"), use_container_width=True)
c3, c4 = st.columns(2)
c3.plotly_chart(px.histogram(df, x="Suhu (°C)", nbins=10, title="Distribusi Suhu (Histogram - Interval)"), use_container_width=True)
c4.plotly_chart(px.scatter(df, x="Suhu (°C)", y="Kelembaban (%)", color="Kota",
                title="Suhu vs Kelembaban (Scatter - Numerik)"), use_container_width=True)