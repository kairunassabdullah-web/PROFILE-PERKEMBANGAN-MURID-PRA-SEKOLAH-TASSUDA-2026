import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("Dashboard Perkembangan Murid TASSUDA 2026")

# Senarai fail anda
files = {
    "Kelas Pn. Siti Rokayah": "PROFILE PERKEMBANGAN MURID PRASEKOLAH TASSUDA 2026.xlsx - KELAS PN SITI ROKAYAH.csv",
    "Kelas Pn. Anita": "PROFILE PERKEMBANGAN MURID PRASEKOLAH TASSUDA 2026.xlsx - KELAS PN ANITA.csv"
}

# 1. Pilih kelas dari menu tepi
pilihan_kelas = st.sidebar.selectbox("Pilih Kelas:", list(files.keys()))

try:
    # Membaca fail berdasarkan pilihan
    df = pd.read_csv(files[pilihan_kelas])
    
    st.subheader(f"Data untuk {pilihan_kelas}")
    
    # 2. Carian Nama Murid
    nama_murid = st.text_input("Cari nama murid:")
    if nama_murid:
        df = df[df['NAMA'].str.contains(nama_murid, case=False, na=False)]
    
    # Paparkan jadual
    st.dataframe(df, use_container_width=True)
    
except Exception as e:
    st.error("Pastikan fail CSV berada dalam folder yang sama!")