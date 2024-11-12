import tkinter as tk  # Mengimpor pustaka tkinter untuk membuat GUI

# Fungsi untuk menampilkan hasil prediksi
def hasil_prediksi():
    # Mengatur teks pada label_hasil menjadi "Prodi Pilihan: Teknologi Informasi"
    label_hasil.config(text="Prodi Pilihan: Teknologi Informasi")

# Membuat jendela utama
root = tk.Tk()  # Membuat jendela utama aplikasi
root.title("Aplikasi Prediksi Prodi Pilihan")  # Memberikan judul pada jendela

# Label judul
label_judul = tk.Label(
    root,  # Menempatkan label di jendela utama
    text="Aplikasi Prediksi Prodi Pilihan",  # Teks yang ditampilkan
    font=("Arial", 16),  # Mengatur jenis dan ukuran huruf
    pady=10  # Memberikan jarak vertikal di sekitar teks
)
label_judul.grid(
    row=0, column=0, columnspan=2, pady=10  # Menempatkan label di baris 0, mencakup 2 kolom
)

# Input nilai mata pelajaran
entry_fields = []  # List untuk menyimpan input (entry) nilai
for i in range(10):  # Loop untuk membuat 10 input nilai
    label = tk.Label(
        root,  # Menempatkan label di jendela utama
        text=f"Nilai Mata Pelajaran {i+1}:",  # Teks dinamis untuk setiap mata pelajaran
        font=("Arial", 12)  # Mengatur jenis dan ukuran huruf
    )
    label.grid(
        row=i+1, column=0, padx=10, pady=5, sticky="e"  # Menempatkan label di kolom 0, baris sesuai iterasi
    )
    entry = tk.Entry(
        root,  # Menempatkan entry di jendela utama
        font=("Arial", 12)  # Mengatur jenis dan ukuran huruf
    )
    entry.grid(
        row=i+1, column=1, padx=10, pady=5  # Menempatkan entry di kolom 1, baris sesuai iterasi
    )
    entry_fields.append(entry)  # Menambahkan entry ke dalam list entry_fields

# Tombol hasil prediksi
button_prediksi = tk.Button(
    root,  # Menempatkan tombol di jendela utama
    text="Hasil Prediksi",  # Teks pada tombol
    font=("Arial", 12),  # Mengatur jenis dan ukuran huruf
    command=hasil_prediksi  # Fungsi yang dipanggil saat tombol ditekan
)
button_prediksi.grid(
    row=11, column=0, columnspan=2, pady=10  # Menempatkan tombol di baris 11, mencakup 2 kolom
)

# Label untuk hasil prediksi
label_hasil = tk.Label(
    root,  # Menempatkan label di jendela utama
    text="",  # Teks awal kosong
    font=("Arial", 14),  # Mengatur jenis dan ukuran huruf
    fg="blue"  # Mengatur warna teks menjadi biru
)
label_hasil.grid(
    row=12, column=0, columnspan=2, pady=10  # Menempatkan label di baris 12, mencakup 2 kolom
)

# Menjalankan aplikasi
root.mainloop()  # Memulai loop utama aplikasi GUI
