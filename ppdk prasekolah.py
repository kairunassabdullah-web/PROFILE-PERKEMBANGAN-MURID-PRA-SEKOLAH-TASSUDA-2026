import streamlit as st
import pandas as pd

st.title("Sistem Perkembangan Murid TASSUDA 2026")

# Masukkan nama fail CSV anda di sini
file_name = "PROFILE PERKEMBANGAN MURID PRASEKOLAH TASSUDA 2026.xlsx - KELAS PN SITI ROKAYAH.csv"

try:
    # Membaca fail CSV
    df = pd.read_csv(file_name)
    st.write("Data Murid:")
    st.dataframe(df)
except Exception as e:
    st.error(f"Error: {e}. Pastikan nama fail dalam kod sama dengan nama fail dalam folder.")