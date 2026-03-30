import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Belajar Streamlit", layout="wide")

# Judul
st.title("1. Elemen Dasar di Streamlit 📝")
st.header("Ini adalah Header (Level 2)")
st.subheader("Ini adalah Subheader (Level 3)")

# Garis Pembatas
st.divider()

# Teks
st.write("Ini pakai **st.write()**. Bisa buat nampilin teks, dataframe, dll")
st.markdown("Ini pakai **st.markdown()**. Cocok buat teks panjang dengan *styling* khusus.")
st.text("Ini pakai st.text(). Styling bintang **tidak** jadi tebal.")
st.caption("Ini pakai st.caption(). Teks kecil dan pudar, cocok buat footnote.")

st.divider()

df = pd.read_csv('data_hp.csv')

st.write("Bisa juga nampilin data:")
st.write(df)

st.write("Visualisasi Data:")
fig = plt.figure(figsize=(10, 5))

plt.bar(df['ID_HP'], df['Terjual_Bulan_Ini'], color='skyblue')
plt.title("Total Penjualan Smartphone Bulan Ini")
plt.xlabel("ID Smartphone")
plt.ylabel("Jumlah Terjual (Unit)")

st.pyplot(fig)

st.divider()

# Kode
st.write("Ini contoh menampilkan kodingan pakai `st.code()`:")
st.code("""
# Script Python sederhana
def sapa_praktikan():
    print("Halo, selamat datang di lab!")
""", language="python")

st.write("Ini contoh rumus matematika pakai `st.latex()`:")
st.latex(r"E = mc^2")

# ===============================================================

st.title("2. Widget Dasar di Streamlit 🎛️")
st.write("Widget biar bisa interaksi sama user")
st.divider()

# Input
nama = st.text_input("Siapa namamu?", placeholder="Masukkan nama panggilan")
umur = st.number_input("Berapa umurmu?", min_value=0, max_value=100, step=1)
pesan = st.text_area("Tulis pesan singkat untuk hari ini:")

st.divider()

# Option
gender = st.radio("Pilih Jenis Kelamin:", ["Laki-laki", "Perempuan", "Custom"])
if gender == 'Custom':
    custom_gender = st.text_input("Gender custom")
hobi = st.selectbox("Hobi Utama (Pilih 1):", ["Membaca", "Coding", "Olahraga", "Tidur"])
skills = st.multiselect("Skill yang dikuasai (Bisa >1):", ["Python", "SQL", "C++", "Java"])

st.divider()

# Slider dan checkbox
kepuasan = st.slider("Seberapa puas kamu dengan kinerja pemerintah?", min_value=0, max_value=100, step=1, value=50)
setuju = st.checkbox("Saya mengonfirmasi bahwa data di atas benar.")

st.divider()

# Button
if st.button("Simpan Data", disabled=not setuju):
    st.success(f"Halo {nama}, {umur} tahun. Datamu berhasil disimpan!")
    st.info(f"Hobi: {hobi} | Tingkat Kepuasan: {kepuasan}%")

# ===============================================================

st.title("3. Dasar Layout di Streamlit 🖼️")
st.write("Mengatur letak elemen biar web terlihat rapi")

# Sidebar
with st.sidebar:
    st.header("Menu Sidebar")
    st.write("Khatama Putra / 123230053")
    st.button("Tombol di Sidebar")

# Tab
tab1, tab2, tab3 = st.tabs(["Tab Pertama", "Tab Kedua", "Tab Ketiga"])

with tab1:
    st.subheader("Ini Isi Tab Pertama")
    st.write("Isi konten untuk halaman pertama ditaruh di sini.")

with tab2:
    st.subheader("Ini Isi Tab Kedua")
    
    # Column
    st.write("Bagi layar jadi 3 kolom:")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.success("Ini Kolom 1 (Kiri)")
    with col2:
        st.warning("Ini Kolom 2 (Tengah)")
    with col3:
        st.error("Ini Kolom 3 (Kanan)")

with tab3:
    st.subheader("Ini Isi Tab Ketiga")
    
    # Expander
    with st.expander("Klik di sini untuk melihat kejutan"):
        st.image('https://pbs.twimg.com/media/HC9Ji4IWYAAWlEU.jpg')
        st.markdown("""
            Sebuah mahakarya yang sangat konseptual! Album ini dibuka dengan manisnya harapan lewat intro 'MBG Untukmu', seolah memberi kita janji makan siang yang indah. Tapi, transisi ke track 'Jatuh Rupiah' benar-benar menampar kita dengan realita kerasnya inflasi. Vokal serak basahnya di track 'DiYordania (Studio Live)' kerasa banget vibes pengasingannya—penuh luka tapi tetap aesthetic. Ditutup dengan outro yang sama, ngingetin kita kalau ujung-ujungnya mah kita cuma butuh makan. 10/10 Masterpeace! 🍽️🔥🦅
        """)
        
    # Container
    with st.container(border=True):
        st.write("Teks ini berada di dalam sebuah Container yang dikasih border (garis tepi).")
        st.write("Fungsinya untuk membingkai beberapa elemen agar terlihat menyatu.")