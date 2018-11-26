# minggu-08

# Tutorial Modul pada [Bab - 10](https://docs.python.org/3/tutorial/stdlib.html)

**10. Brief Tour of the Standard Library**
		
**10.1 Operating System Interface**
	   - Fungsi built-in dir () dan help () berguna sebagai bantuan interaktif     		 untuk bekerja dengan modul besar seperti os:
	     Untuk tugas-tugas harian dan manajemen direktori, modul shutil menyediakan antarmuka tingkat yang lebih tinggi yang lebih mudah digunakan

**10.2 File Wildcards**
	   - Modul glob menyediakan fungsi untuk membuat daftar file dari pencarian 		 direktori wildcard

**10.3 Command Line Arguments**
	   - Modul getopt memproses sys.argv menggunakan konvensi fungsi getopt (). 		 Pemrosesan baris perintah yang lebih kuat dan fleksibel disediakan oleh 		 modul argparse.

**10.4 Error Output Redirection and Program Termination**
	   - Modul sys juga memiliki atribut untuk stdin, stdout, dan stderr. Yang 			 terakhir ini berguna 
	     untuk memancarkan peringatan dan pesan kesalahan untuk membuatnya terlihat bahkan ketika stdout telah dialihkan
		 Cara paling langsung untuk mengakhiri skrip adalah menggunakan sys.exit ().

**10.5 String Pattern Matching**
	   - Modul re menyediakan alat ekspresi reguler untuk pemrosesan string tingkat 	 lanjut. 
	     Untuk pencocokan dan manipulasi yang kompleks, ekspresi reguler menawarkan solusi yang ringkas dan dioptimalkan
	     Ketika hanya kemampuan sederhana yang diperlukan, metode string lebih disukai karena mereka lebih mudah dibaca dan di-debug

**10.6 Mathematics**
	   - Modul matematika memberikan akses ke fungsi pustaka C yang mendasari untuk 	 floating point math
	     Modul acak menyediakan alat untuk membuat pilihan acak
		 Modul statistik menghitung sifat statistik dasar (mean, median, varians, dll.) Dari data numerik
		 Proyek SciPy (https://scipy.org) memiliki banyak modul lain untuk perhitungan numerik.

**10.7 Internet Access**
	   - Ada sejumlah modul untuk mengakses internet dan memproses protokol 			 internet. Dua yang paling sederhana adalah urllib.
	     request untuk mengambil data dari URL dan smtplib untuk mengirim email

**10.8 Dates and Times**
	   - The datetime module supplies classes for manipulating dates and times in 		 both simple and complex ways. 
	     While date and time arithmetic is supported, the focus of the implementation is on efficient member extraction for output formatting and manipulation. 
		 The module also supports objects that are timezone aware.

**10.9 Data Compression**
	   - Pengarsipan data umum dan format kompresi secara langsung didukung oleh 		 modul termasuk: zlib, gzip, bz2, lzma, zipfile dan tarfile.

**10.10 Performance Measurement**
	    - Python menyediakan alat pengukuran untuk menggunakan pengemasan tuple dan   fitur unpacking dari pada 
		  pendekatan tradisional untuk bertukar argumen. Modul timeit dengan cepat menunjukkan keunggulan kinerja.

**10.11 Quality Control**
	    - Modul doctest menyediakan alat untuk memindai modul dan memvalidasi tes 	  yang disematkan di doktrin program. 
		  Uji konstruksi sederhana seperti memotong dan menyisipkan panggilan khas bersama dengan hasilnya ke dalam docstring. 
		  Ini meningkatkan dokumentasi dengan memberikan contoh kepada pengguna dan memungkinkan modul doctest memastikan kode tetap benar untuk dokumentasi
		  Modul unittest tidak semudah modul doctest, tetapi memungkinkan serangkaian tes yang lebih komprehensif dipertahankan dalam file terpisah

	  
	  
# Tutorial Modul pada [Bab - 11](https://docs.python.org/3/tutorial/stdlib2.html)

**11. Brief Tour of the Standard Library — Part II**
	  - Tur kedua ini mencakup modul yang lebih canggih yang mendukung kebutuhan 	  pemrograman profesional. 
	    Modul-modul ini jarang terjadi dalam skrip kecil.

**11.1 Output Formatting**
	   - Modul reprlib menyediakan versi repr () yang disesuaikan untuk disingkat 	  menampilkan wadah bersarang besar atau sangat bersarang
	     Modul pprint menawarkan kontrol yang lebih canggih atas pencetakan objek yang sudah ada dan yang ditentukan pengguna dengan cara 
		 yang dapat dibaca oleh juru bahasa. Ketika hasilnya lebih panjang dari satu baris, "printer cantik" menambahkan jeda baris dan indentasi untuk lebih jelas mengungkapkan struktur data
		 Modul textwrap memformat paragraf teks agar sesuai dengan lebar layar yang ditentukan
		 Modul lokal mengakses database format data budaya tertentu. Atribut pengelompokan fungsi format lokal menyediakan cara langsung untuk memformat angka dengan pemisah grup

**11.2 Templating**
	   - Modul string termasuk kelas Template serbaguna dengan sintaks yang 	  		 disederhanakan yang cocok untuk diedit oleh pengguna akhir. 
	     Ini memungkinkan pengguna untuk menyesuaikan aplikasi mereka tanpa harus mengubah aplikasi.
		 Format ini menggunakan nama placeholder yang dibentuk oleh $ dengan identifier Python yang valid
		 Metode substit () membangkitkan KeyError ketika placeholder tidak disediakan dalam kamus atau argumen kata kunci.
		 Subclass template dapat menetapkan pemisah khusus. Misalnya, utilitas penggantian nama batch untuk browser foto dapat memilih 
		 untuk menggunakan tanda persen untuk placeholder seperti tanggal saat ini, nomor urut gambar, atau format file

**11.3 Working with Binary Data Record Layouts**
	   - Modul struct menyediakan fungsi pack () dan unpack () untuk bekerja dengan   format record binary panjang variabel. 
	 	 Contoh berikut menunjukkan cara mengulang melalui informasi header dalam file ZIP tanpa menggunakan modul zipfile. 
	 	 Paket kode "H" dan "I" mewakili dua dan empat bilangan unsigned masing-masing. "<" Menunjukkan bahwa ukurannya standar dan dalam urutan byte kecil-endian

**11.4 Multi-threading**
	   - Threading adalah teknik untuk memisahkan tugas yang tidak tergantung    	  secara berurutan. Thread dapat digunakan untuk meningkatkan respon dari 	  aplikasi 
	     yang menerima input pengguna sementara tugas lain berjalan di latar belakang. Kasus penggunaan terkait menjalankan I / O secara paralel dengan perhitungan lain.
		 Tantangan utama aplikasi multi-threaded adalah mengoordinasikan utas yang berbagi data atau sumber daya lainnya. Untuk itu, modul threading menyediakan 
		 sejumlah primitif sinkronisasi termasuk kunci, peristiwa, variabel kondisi, dan semaphores.
	 
**11.5 Logging**
	   - Secara default, pesan informasi dan debug ditekan dan output dikirim ke 	  kesalahan standar. Pilihan output lainnya termasuk routing pesan melalui 	  email, 
	   	 datagrams, socket, atau ke HTTP Server. Filter baru dapat memilih perutean berbeda berdasarkan prioritas pesan: DEBUG, INFO, PERINGATAN, KESALAHAN, dan KRITIS.
	 	 Sistem pencatatan dapat dikonfigurasikan langsung dari Python atau dapat dimuat dari file konfigurasi yang dapat diedit pengguna untuk pencatatan kustom tanpa mengubah aplikasi.

**11.6 Weak References**
	   - Python melakukan manajemen memori otomatis (penghitungan referensi untuk 	  sebagian besar objek dan pengumpulan sampah untuk menghilangkan siklus). 		 Memori dibebaskan tak lama setelah referensi terakhir yang telah    	  		 dihapuskan.
	 	 Pendekatan ini berfungsi dengan baik untuk sebagian besar aplikasi, tetapi kadang-kadang ada kebutuhan untuk melacak objek hanya selama mereka digunakan oleh sesuatu yang lain

**11.7 Tools for Working with Lists**
	   - Modul array menyediakan objek array () yang seperti daftar yang hanya 	 	  menyimpan data homogen dan menyimpannya secara lebih kompak. 
	 	 Contoh berikut menunjukkan array angka yang disimpan sebagai dua bilangan biner unsigned digit (typecode "H") daripada biasanya 16 byte per entri untuk daftar reguler objek int Python
	 	 Modul koleksi menyediakan objek deque () yang seperti daftar dengan penambahan lebih cepat dan muncul dari sisi kiri tetapi pencarian lebih lambat di tengah. 
	 	 Objek-objek ini sangat cocok untuk mengimplementasikan antrian dan keluasan pencarian pohon pertama
	 	 Selain penerapan daftar alternatif, perpustakaan juga menawarkan alat lain seperti modul membagi dua dengan fungsi untuk memanipulasi daftar yang diurutkan
		 Modul heapq menyediakan fungsi untuk menerapkan tumpukan berdasarkan daftar reguler. 
		 Entri bernilai terendah selalu disimpan di posisi nol. Ini berguna untuk aplikasi yang berulang kali mengakses elemen terkecil tetapi tidak ingin menjalankan daftar daftar lengkap
	
**11.8 Decimal Floating Point Arithmetic**
	   - Modul desimal menawarkan datatype Desimal untuk aritmatika floating point 	  desimal. Dibandingkan dengan penerapan float floating point biner, kelas 	  sangat membantu
	   - aplikasi keuangan dan penggunaan lainnya yang memerlukan representasi 			 desimal yang tepat,
	   - kontrol atas presisi,
	   - kontrol atas pembulatan untuk memenuhi persyaratan hukum atau peraturan,
	   - pelacakan tempat desimal yang signifikan, atau
	   - aplikasi di mana pengguna mengharapkan hasil untuk mencocokkan perhitungan 	 yang dilakukan dengan tangan.

