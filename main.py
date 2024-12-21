import pandas as pd
from fuzzywuzzy import process

# Fungsi untuk memfilter data berdasarkan input pengguna menggunakan fuzzy matching
def filter_data_by_user_input(data, release_year, rating_category, duration):
    # Fuzzy matching untuk kategori tahun rilis (Jadul vs Modern)
    if release_year == "jadul":
        filtered_data = data[data['release_year'] <= 2000]
    elif release_year == "modern":
        filtered_data = data[data['release_year'] > 2000]
    
    # Fuzzy matching untuk kategori rating (memuaskan, biasa aja, buruk)
    valid_ratings = ['R', 'PG', 'PG-13']
    rating_choice = process.extractOne(rating_category, ['memuaskan', 'biasa aja', 'buruk'])
    
    if rating_choice[0] == "memuaskan":
        filtered_data = filtered_data[filtered_data['rating'] == 'R']
    elif rating_choice[0] == "biasa aja":
        filtered_data = filtered_data[filtered_data['rating'] == 'PG']
    elif rating_choice[0] == "buruk":
        filtered_data = filtered_data[filtered_data['rating'] == 'PG-13']
    
    # Filter berdasarkan durasi
    if duration == "pendek":
        filtered_data = filtered_data[filtered_data['duration'] <= 90]
    elif duration == "sedang":
        filtered_data = filtered_data[(filtered_data['duration'] > 90) & (filtered_data['duration'] <= 120)]
    elif duration == "panjang":
        filtered_data = filtered_data[filtered_data['duration'] > 120]
    
    return filtered_data

# Fungsi untuk meminta input pengguna
def get_user_input():
    print("Masukkan kriteria pencarian film:")
    
    # Meminta input untuk kategori tahun rilis (jadul atau modern)
    print("Pilih kategori tahun rilis:")
    print("1. Jadul (<= 2000)")
    print("2. Modern (> 2000)")
    release_year_choice = int(input("Masukkan pilihan (1 atau 2): "))
    
    if release_year_choice == 1:
        release_year = "jadul"
    elif release_year_choice == 2:
        release_year = "modern"
    
    # Meminta input untuk kategori rating
    print("Pilih rating film:")
    print("1. Memuaskan (R)")
    print("2. Biasa aja (PG)")
    print("3. Buruk (PG-13)")
    rating_choice = int(input("Masukkan pilihan (1, 2, atau 3): "))
    
    if rating_choice == 1:
        rating_category = "memuaskan"
    elif rating_choice == 2:
        rating_category = "biasa aja"
    elif rating_choice == 3:
        rating_category = "buruk"
    
    # Meminta input untuk durasi
    print("Pilih durasi film:")
    print("1. Pendek (<= 90 menit)")
    print("2. Sedang (> 90 dan <= 120 menit)")
    print("3. Panjang (> 120 menit)")
    duration_choice = int(input("Masukkan pilihan (1, 2, atau 3): "))
    
    if duration_choice == 1:
        duration = "pendek"
    elif duration_choice == 2:
        duration = "sedang"
    elif duration_choice == 3:
        duration = "panjang"
    
    return release_year, rating_category, duration

# Membaca data dari CSV
data = pd.read_csv('data.csv')

# Mengonversi kolom 'duration' menjadi numerik agar mudah diproses
data['duration'] = data['duration'].astype(int)

# Mendapatkan input dari pengguna
release_year, rating_category, duration = get_user_input()

# Memfilter data berdasarkan input pengguna
filtered_data = filter_data_by_user_input(data, release_year, rating_category, duration)

# Menampilkan hasil
if not filtered_data.empty:
    print("\nFilm yang sesuai dengan kriteria pencarian Anda:")
    print(filtered_data[['title', 'release_year', 'rating', 'duration', 'genre']])
else:
    print("\nTidak ada film yang sesuai dengan kriteria pencarian Anda.")