# minggu-07

# Tutorial Modul pada [Bab - 9](https://docs.python.org/3/tutorial/classes.html)

9. Classes
	Kelas menyediakan sarana untuk menggabungkan data dan fungsi bersama. 
	Membuat kelas baru menciptakan jenis objek baru, yang memungkinkan instance baru dari jenis itu dibuat. 
	Setiap instance kelas dapat memiliki atribut yang melekat padanya untuk mempertahankan statusnya. 
	Instance kelas juga dapat memiliki metode (ditentukan oleh kelasnya) untuk memodifikasi statusnya.
	
9.1 A Word About Names and Objects
	Objek memiliki individualitas, dan beberapa nama (dalam berbagai cakupan) dapat terikat ke objek yang sama. 
	Ini dikenal sebagai aliasing dalam bahasa lain. Ini biasanya tidak dihargai pada pandangan pertama Python, 
	dan dapat dengan aman diabaikan ketika berhadapan dengan jenis dasar yang tidak dapat diubah (angka, string, tupel). 
	Namun, aliasing memiliki efek yang mungkin mengejutkan pada semantik kode Python yang melibatkan objek yang dapat berubah 
	seperti daftar, kamus, dan sebagian besar jenis lainnya. Ini biasanya digunakan untuk kepentingan program, karena alias 
	bertindak seperti pointer dalam beberapa hal. Sebagai contoh, melewati suatu objek adalah murah karena hanya pointer yang 
	dilewatkan oleh implementasi; dan jika fungsi memodifikasi objek yang dilewatkan sebagai argumen, pemanggil akan melihat 
	perubahan - ini menghilangkan kebutuhan untuk dua mekanisme pengalihan argumen yang berbeda seperti dalam Pascal.

9.2 Python Scopes and Namespaces
	Namespace adalah pemetaan dari nama ke objek. Kebanyakan ruang nama saat ini diterapkan sebagai kamus Python, tetapi itu 
	biasanya tidak terlihat dengan cara apa pun (kecuali untuk kinerja), dan mungkin akan berubah di masa mendatang. 
	Contoh ruang nama adalah: kumpulan nama bawaan (berisi fungsi seperti abs (), dan nama pengecualian bawaan); nama-nama global 
	dalam sebuah modul; dan nama-nama lokal dalam doa fungsi. Dalam arti set atribut suatu objek juga membentuk namespace. 
	Yang penting untuk diketahui tentang ruang nama adalah bahwa sama sekali tidak ada hubungan antara nama di ruang nama 
	yang berbeda; misalnya, dua modul yang berbeda dapat mendefinisikan fungsi yang dimaksimalkan tanpa kebingungan - pengguna 
	modul harus menambahkannya dengan nama modul.

	9.2.1 Scopes and Namespaces Example
		  Perhatikan bagaimana penugasan lokal (yang default) tidak mengubah scope_test's binding of spam. 
		  Penugasan nonlokal mengubah scope_test's binding of spam, dan penugasan global mengubah pengikatan level modul.
		  Anda juga dapat melihat bahwa tidak ada pengikatan sebelumnya untuk spam sebelum penugasan global.
	
9.3 A First Look at Classes
	memperkenalkan sedikit sintaks baru, tiga jenis objek baru, dan beberapa semantik baru.

	9.3.1 Class Definition Syntax
		  Definisi kelas, seperti definisi fungsi (pernyataan def) harus dijalankan sebelum mereka memiliki efek apa pun. 
		  (Anda mungkin bisa menempatkan definisi kelas dalam cabang pernyataan if, atau di dalam fungsi.)
		  Dalam praktiknya, pernyataan di dalam definisi kelas biasanya akan menjadi definisi fungsi, 
		  tetapi pernyataan lain diizinkan, dan terkadang berguna - kami akan kembali ke ini nanti. 
		  Definisi fungsi di dalam kelas biasanya memiliki bentuk aneh daftar argumen, didikte oleh konvensi 
		  pemanggilan untuk metode - lagi, ini dijelaskan nanti.
		  
	9.3.2 Class Objects
		  Objek kelas mendukung dua jenis operasi: referensi atribut dan instantiasi.
		  Referensi atribut menggunakan sintaks standar yang digunakan untuk semua referensi 
		  atribut dengan Python: obj.name. Nama atribut yang valid adalah semua nama yang ada 
		  di namespace kelas ketika objek kelas dibuat.
		  
	9.3.3 Instance Objects
		  Metode adalah fungsi yang "milik" suatu objek. (Dalam Python, metode jangka tidak unik untuk instance kelas: jenis objek lain dapat memiliki metode juga. 
		  Misalnya, objek daftar memiliki metode yang disebut append, insert, remove, sort, dan sebagainya. Namun, 
		  dalam diskusi berikut, kami akan menggunakan metode istilah secara eksklusif untuk mengartikan metode objek instance kelas, kecuali secara eksplisit dinyatakan sebaliknya.)
		  Nama metode yang valid dari objek instance bergantung pada kelasnya. Menurut definisi, semua atribut kelas 
		  yang merupakan objek fungsi menentukan metode yang sesuai dari instance-nya. Jadi dalam contoh kita, x.f adalah referensi metode yang valid, 
		  karena MyClass.f adalah fungsi, tetapi x.i tidak, karena MyClass.i tidak. Tapi x.f tidak sama dengan MyClass.f - itu adalah objek metode, bukan objek fungsi.
	
	9.3.4 Method Objects
		  Jika Anda masih belum memahami cara kerja metode, melihat penerapannya mungkin dapat memperjelas masalah. 
		  Ketika atribut non-data dari suatu instance direferensikan, kelas instance tersebut dicari. Jika nama menunjukkan 
		  atribut kelas yang valid yang merupakan objek fungsi, objek metode dibuat dengan mengepak (menunjuk ke) objek contoh 
		  dan objek fungsi hanya ditemukan bersama-sama dalam objek abstrak: ini adalah objek metode. Ketika objek metode dipanggil 
		  dengan daftar argumen, daftar argumen baru dibangun dari objek contoh dan daftar argumen, dan objek fungsi dipanggil dengan daftar argumen baru ini.
	
	9.3.5 Class and Instance Variables
		  Sebagaimana dibahas dalam A Word About Names and Objects, data yang dibagikan dapat memiliki efek 
		  yang mengejutkan dengan melibatkan objek yang dapat berubah seperti daftar dan kamus. Misalnya, 
		  daftar trik dalam kode berikut tidak boleh digunakan sebagai variabel kelas karena hanya satu daftar yang akan dibagikan oleh semua instance

9.4 Random Remarks
	Metode dapat merujuk nama global dengan cara yang sama seperti fungsi biasa. Ruang lingkup global yang terkait 
	dengan suatu metode adalah modul yang berisi definisinya. (Sebuah kelas tidak pernah digunakan sebagai ruang lingkup global.) 
	Sementara seseorang jarang menemukan alasan yang baik untuk menggunakan data global dalam suatu metode, ada banyak penggunaan 
	yang sah dari lingkup global: untuk satu hal, fungsi dan modul yang diimpor ke dalam lingkup global dapat digunakan oleh metode, 
	serta fungsi dan kelas yang ditentukan di dalamnya. Biasanya, kelas yang berisi metode itu sendiri didefinisikan dalam lingkup global ini, 
	dan di bagian berikutnya kita akan menemukan beberapa alasan bagus mengapa suatu metode ingin merujuk kelasnya sendiri.
	Setiap nilai adalah objek, dan oleh karena itu memiliki kelas (juga disebut jenisnya). Itu disimpan sebagai objek .__ class__.

9.5 Inheritance
	Eksekusi definisi kelas turunan berlangsung sama dengan kelas dasar. Ketika objek kelas dibangun, kelas dasar dikenang. 
	Ini digunakan untuk menyelesaikan referensi atribut: jika atribut yang diminta tidak ditemukan di kelas, pencarian dilanjutkan ke kelas dasar. 
	Aturan ini diterapkan secara rekursif jika kelas dasar itu sendiri berasal dari beberapa kelas lain.
	Tidak ada yang istimewa tentang Instansiasi kelas turunan: DerivedClassName () membuat instance baru dari kelas. 
	Referensi metode diselesaikan sebagai berikut: atribut kelas yang sesuai dicari, menuruni rantai kelas dasar jika 
	diperlukan, dan referensi metode valid jika ini menghasilkan objek fungsi.

	
	9.5.1 Multiple Inheritance
		  Urutan dinamis diperlukan karena semua kasus pewarisan berganda menunjukkan satu atau lebih hubungan berlian 
		  (di mana setidaknya satu dari kelas induk dapat diakses melalui beberapa jalur dari kelas paling bawah). Sebagai contoh, 
		  semua kelas mewarisi dari objek, jadi setiap kasus multiple inheritance menyediakan lebih dari satu jalur untuk mencapai objek. 
		  Agar kelas dasar tidak dapat diakses lebih dari satu kali, algoritme dinamis akan membuat garis keturunan urutan pencarian dengan 
		  cara mempertahankan urutan kiri-ke-kanan yang ditentukan di setiap kelas, yang memanggil setiap orang tua hanya sekali, dan itu monotonik 
		  (artinya kelas dapat digolongkan tanpa mempengaruhi urutan prioritas dari orang tuanya). Secara bersama-sama, properti ini memungkinkan untuk
		  mendesain kelas yang dapat diandalkan dan diperluas dengan multiple inheritance. 

9.6 Private Variables
	Private "variabel instan yang tidak dapat diakses kecuali dari dalam objek tidak ada di Python. Namun, ada konvensi yang diikuti
	oleh sebagian besar kode Python: sebuah nama yang diawali dengan underscore (misalnya _spam) harus diperlakukan sebagai bagian 
	non-publik dari API (apakah itu fungsi, metode atau anggota data) . Ini harus dianggap sebagai detail implementasi dan dapat berubah tanpa pemberitahuan.

9.7 Odds and Ends
	Sepotong kode Python yang mengharapkan tipe data abstrak tertentu sering dapat dilewatkan kelas yang mengemulasi metode dari tipe data itu sebagai gantinya. 
	Misalnya, jika Anda memiliki fungsi yang memformat beberapa data dari objek file, Anda dapat menentukan kelas dengan metode baca () dan readline () yang 
	mendapatkan data dari buffer string sebagai gantinya, dan menyebarkannya sebagai argumen.

9.8 Iterators
	Gaya akses ini jelas, ringkas, dan nyaman. Penggunaan iterator meliputi dan menyatukan Python. Di belakang layar, untuk pernyataan memanggil 
	iter () pada objek kontainer. Fungsi mengembalikan objek iterator yang mendefinisikan metode __next __ () yang mengakses elemen dalam 
	wadah satu per satu. Ketika tidak ada lagi elemen, __next __ () memunculkan pengecualian StopIteration yang memberitahu loop untuk mengakhiri.
	Anda dapat memanggil metode __next __ () dengan menggunakan fungsi next () built-in;

9.9 Generators
	Apa pun yang dapat dilakukan dengan generator juga dapat dilakukan dengan iterator berbasis kelas seperti yang dijelaskan di bagian sebelumnya. 
	Apa yang membuat generator begitu kompak adalah bahwa metode __iter __ () dan __next __ () dibuat secara otomatis.Fitur kunci lainnya adalah 
	bahwa variabel lokal dan status eksekusi secara otomatis disimpan di antara panggilan. Ini membuat fungsi lebih mudah ditulis dan lebih jelas 
	daripada pendekatan menggunakan variabel instan seperti self.index dan self.data.

9.10 Generator Expressions
	 Beberapa generator sederhana dapat dikodekan secara ringkas sebagai ekspresi menggunakan sintaks yang mirip dengan daftar pemahaman tetapi 
	 dengan tanda kurung bukan tanda kurung siku. Ekspresi ini dirancang untuk situasi di mana generator digunakan langsung oleh fungsi melampirkan. 
	 Ekspresi generator lebih ringkas tetapi kurang serbaguna daripada definisi generator penuh dan cenderung lebih ramah memori daripada pemahaman daftar ekuivalen
	
