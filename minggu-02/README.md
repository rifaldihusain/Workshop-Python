# minggu-02

# Tutorial Modul pada [bab - 4](https://docs.python.org/3/tutorial/controlflow.html)


**4. More Control Flow Tools**
		 - Selain pernyataan sementara yang baru saja diperkenalkan, Python mengetahui 		 pernyataan aliran kontrol yang biasa dikenal dari bahasa lain, dengan 					 beberapa twists
	
**4.1 if Statements**
			- Pengambilan keputusan (kondisi if else) tidak hanya digunakan untuk 			 		menentukan tindakan apa yang akan diambil sesuai dengan kondisi, tetapi 			juga digunakan untuk menentukan tindakan apa yang akan diambil/dijalankan 		jika kondisi tidak sesuai.
	  		Pada python ada beberapa statement/kondisi diantaranya adalah if, else dan elif Kondisi if digunakan untuk mengeksekusi kode jika kondisi bernilai benar.
	  		Kondisi if else adalah kondisi dimana jika pernyataan benar True maka kode dalam if akan dieksekusi, tetapi jika bernilai salah False maka akan mengeksekusi kode di dalam else.
	   
**4.2 for Statements**
			- For adalah perulangan yang dapat digunakan untuk menentukan batas awal, 			batas akhir, selisih dari loop
	
**4.3. The range() Function**
			 - Fungsi range() merupakan fungsi yang menghasilkan list. Fungsi ini akan 			 menciptakan sebuah list baru dengan rentang nilai tertentu.
	     	 Range dengan satu parameter akan menghasilkan list dengan rentang parameter itu. Sedangkan range dengan dua parameter akan menghasilkan list 
		 		 dengan rentang dari parameter pertama sampai parameter kedua. Kemudian, range yang menggunakan tiga parameter akan menghasilkan list dengan rentang 
		 		 dari parameter pertama sampai parameter kedua dengan jarak interval parameter ketiga.
	
**4.4. break and continue Statements, and else Clauses on Loops**
			 - BREAK adalah sebuah pernyataan yang akan membuat sebuah program berhenti 		 atau keluar dari suatu blok pengulangan. Dan semua kode setelah pernyataan 	 break akan diabaikan. 
	     	 Pernyataan break ini dapat kita gunakan pada pengulangan while dan for.
		 		 Berbeda dengan pernyataan break, pernyataan continue akan melakukan pengulangan mulai dari awal lagi. 
		 		 Dan akan mengabaikan semua kode yang tersisa pada loop untuk menuju awal loop lagi
	
**4.5. pass Statements**
			 - digunakan ketika pernyataan diperlukan secara sintaksis, tetapi Anda tidak 	 ingin ada perintah atau kode untuk dieksekusi.
	     	 Ini dapat digunakan ketika pernyataan diperlukan secara sintaksis tetapi program tidak memerlukan tindakan.
		 		 tidak ada yang terjadi saat operan dijalankan. Hasilnya tidak ada operasi (NOP).
	
**4.6. Defining Functions**
			 - Definisi fungsi memperkenalkan nama fungsi dalam tabel simbol saat ini. 			 Nilai dari nama fungsi memiliki tipe yang dikenali 
	   		 oleh interpreter sebagai fungsi yang ditentukan pengguna. Nilai ini dapat ditetapkan ke nama lain yang kemudian dapat juga 
	   		 digunakan sebagai fungsi. Ini berfungsi sebagai mekanisme penggantian nama umum

**4.7. More on Defining Functions**
			 - Juga dimungkinkan untuk mendefinisikan fungsi dengan sejumlah argumen 			  variabel. Ada tiga bentuk, yang bisa digabungkan.

	4.7.1. Default Argument Values
		     - Formulir yang paling berguna adalah menentukan nilai default untuk satu 		 atau lebih argumen. Ini menciptakan fungsi yang dapat dipanggil dengan 		 argumen yang lebih sedikit daripada yang ditentukan untuk diizinkan.
	
	4.7.2. Keyword Arguments
		     - Fungsi juga bisa disebut menggunakan argumen kata kunci dari bentuk 		  	 kwarg = nilai.Dalam panggilan fungsi, argumen kata kunci harus mengikuti 	 argumen posisional. Semua argumen kata kunci yang dilewatkan harus 		    sesuai 
			   	 dengan salah satu argumen yang diterima oleh fungsi (misalnya aktor bukanlah argumen yang valid untuk fungsi burung beo), dan urutannya tidak penting. Ini juga termasuk argumen non-opsional (misalnya parrot (tegangan = 1000) juga valid). 
			   	 Tidak ada argumen yang dapat menerima nilai lebih dari satu kali.
	
	4.7.3. Arbitrary Argument Lists
			 - Opsi yang paling jarang digunakan adalah untuk menentukan bahwa suatu 			  fungsi dapat dipanggil dengan sejumlah argumen acak. Argumen-argumen ini 		 akan dibungkus dalam tuple (lihat Tuples dan Urutan). 
			   Sebelum jumlah variabel argumen, nol atau lebih banyak argumen normal dapat terjadi. Biasanya, argumen-argumen variadic ini akan menjadi yang terakhir dalam daftar parameter formal, 
			   karena mereka mengumpulkan semua argumen input yang tersisa yang diteruskan ke fungsi. Setiap parameter formal yang terjadi setelah parameter * args adalah argumen 'kata kunci saja', 
			   yang berarti bahwa mereka hanya dapat digunakan sebagai kata kunci daripada argumen posisi.
	
	4.7.4. Unpacking Argument Lists
		     - Situasi sebaliknya terjadi ketika argumen sudah ada dalam daftar atau 			 tupel tetapi perlu dibongkar untuk panggilan fungsi yang membutuhkan 			 argumen posisi terpisah. Misalnya, 
			   	 fungsi rentang () built-in mengharapkan mulai terpisah dan menghentikan argumen. Jika tidak tersedia secara terpisah, tulis panggilan fungsi dengan * -operator untuk membongkar argumen dari daftar atau tupel
	
	4.7.5. Lambda Expressions
			 - Fungsi anonim kecil dapat dibuat dengan kata kunci lambda. Fungsi ini 				 mengembalikan jumlah dari dua argumennya: lambda a, b: a + b. Fungsi 				 Lambda dapat digunakan di mana pun objek fungsi diperlukan. 
			   Mereka secara sintaksis terbatas pada satu ekspresi. Secara semantis, mereka hanyalah gula sintaksis untuk definisi fungsi normal. Seperti definisi fungsi bertingkat, fungsi lambda dapat merujuk variabel dari ruang lingkup
	
	4.7.6. Documentation Strings
			 - Berikut adalah beberapa konvensi tentang konten dan format string 						 dokumentasi. Baris pertama harus selalu berupa ringkasan singkat dan 				 ringkas dari tujuan objek. Untuk keringkasan, 
			   itu tidak boleh secara eksplisit menyatakan nama atau jenis objek, karena ini tersedia dengan cara lain (kecuali jika nama yang terjadi adalah kata kerja yang menggambarkan operasi fungsi). Baris ini harus dimulai dengan huruf kapital dan diakhiri dengan titik. 
			   Jika ada lebih banyak baris dalam string dokumentasi, baris kedua harus kosong, secara visual memisahkan ringkasan dari sisa deskripsi. Baris berikut harus berupa satu paragraf atau lebih yang menggambarkan konvensi pemanggilan objek, efek sampingnya.

	
	4.7.7. Function Annotations
			 - Anotasi disimpan dalam atribut __annotations__ dari fungsi sebagai kamus 		 dan tidak berpengaruh pada bagian lain dari fungsi. Anotasi parameter 				 ditentukan oleh titik dua setelah nama parameter, diikuti oleh ekspresi 			 yang mengevaluasi ke nilai anotasi. 
			   Anotasi pengembalian ditentukan oleh literal ->, diikuti oleh ekspresi, di antara daftar parameter dan tanda titik dua yang menunjukkan akhir pernyataan def. Contoh berikut memiliki argumen posisi, argumen kata kunci dan nilai kembalian yang dianotasikan
