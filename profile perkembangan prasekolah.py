import streamlit as st
import pandas as pd

st.title("Sistem Perkembangan Murid TASSUDA 2026")

# Kod ini akan mencari fail CSV dalam folder yang sama
nama_fail = 'PROFILE PERKEMBANGAN MURID PRASEKOLAH TASSUDA 2026.xlsx - KELAS PN SITI ROKAYAH.csv'

try:
    df = pd.read_csv(nama_fail)
    st.write("Data Berjaya Dimuatkan:")
    st.dataframe(df) # Ini akan paparkan data murid dalam bentuk jadual yang cantik
except FileNotFoundError:
    st.error("Fail CSV tidak dijumpai. Pastikan fail berada dalam folder yang betul!")