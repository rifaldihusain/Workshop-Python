# minggu-03

# Tutorial Modul pada [Bab - 5](https://docs.python.org/3/tutorial/datastructures.html)

**5.1 More on Lists**
	  - Bab ini menjelaskan beberapa hal yang sudah Anda pelajari dengan lebih 			detail,dan menambahkan beberapa hal baru. yang terdapat list.append, list 		extend, list insert, list remove, list pop, list clear, list index, list 		count, list sort, list reverse, list copy.

	5.1.1 Using Lists as Stacks
		  - Metode daftar membuatnya sangat mudah untuk menggunakan daftar sebagai 		tumpukan, di mana elemen terakhir yang ditambahkan adalah elemen 			pertama yang diambil ("terakhir-masuk, pertama-keluar"). Untuk 				menambahkan item ke bagian atas tumpukan, gunakan tambahkan (). Untuk 		mengambil item dari bagian atas tumpukan, gunakan pop () tanpa indeks 		eksplisit.

	5.1.2 Using Lists as Queues
		  - menggunakan daftar sebagai antrian, di mana 		elemen pertama yang 	ditambahkan adalah elemen pertama yang diambil 			("masuk pertama, 	pertama keluar"); Namun, daftar tidak efisien untuk 		tujuan ini. 	Sementara menambahkan dan muncul dari akhir daftar cepat, 					melakukan sisipan atau muncul dari awal daftar lambat (karena semua 		elemen lain harus digeser).
		  	Untuk menerapkan antrean, gunakan collections.deque yang dirancang agar memiliki penambahan cepat dan muncul dari kedua ujungnya.

	5.1.3 List Comprehensions
		  - Daftar pemahaman menyediakan cara yang ringkas untuk membuat daftar. 		Aplikasi umum adalah membuat daftar baru di mana setiap elemen adalah 		hasil dari beberapa operasi yang diterapkan pada setiap anggota urutan 		lain atau dapat dilakukan, atau untuk menciptakan kelanjutan dari 			elemen-elemen yang memenuhi suatu kondisi tertentu.

	5.1.4 Nested List Comprehensions
		  - Ekspresi awal dalam pemahaman daftar dapat berupa ekspresi sembarang, 		termasuk pemahaman daftar lainnya.
	
**5.2 The del Statement**
	  - Ada cara untuk menghapus item dari daftar yang diberikan indeks, bukan 			nilainya: pernyataan del. Ini berbeda dari metode pop () yang mengembalikan 	nilai. Pernyataan del juga dapat digunakan untuk menghapus irisan dari 			daftar atau menghapus seluruh daftar (yang kita lakukan sebelumnya dengan 		penugasan daftar kosong ke irisan)

**5.3 Tuples and Sequence**
	  - Kami melihat bahwa daftar dan string memiliki banyak properti umum, seperti 	pengindeksan dan operasi pengirisan. Mereka adalah dua contoh tipe data 		urutan (lihat Jenis Urutan - daftar, tupel, rentang). Karena Python adalah 		bahasa yang sedang berkembang, tipe data urutan lainnya dapat ditambahkan. 		Ada juga tipe data urutan standar lainnyaSebuah tuple terdiri dari sejumlah 	nilai yang dipisahkan oleh koma.

**5.4 Sets**
	  - Python juga termasuk tipe data untuk set. Satu set adalah koleksi tak 			berurutan tanpa elemen duplikat. Penggunaan dasar termasuk pengujian 			keanggotaan dan menghilangkan entri duplikat. Mengatur objek juga mendukung 	operasi matematika seperti penyatuan, persimpangan, perbedaan, dan 				perbedaan simetris.
	  	Curly braces atau fungsi set () dapat digunakan untuk membuat set. Catatan: untuk membuat set kosong Anda harus menggunakan set (), bukan {}; yang terakhir menciptakan kamus kosong

**5.5 Dictionaries**
	  - Tipe data lain yang berguna dibangun ke dalam Python adalah kamus (lihat 		Jenis Pemetaan - dict). Kamus kadang-kadang ditemukan dalam bahasa lain 		sebagai "kenangan asosiatif" atau "array asosiatif". Tidak seperti urutan, 		yang diindeks oleh berbagai angka, kamus diindeks oleh kunci, yang bisa 		menjadi jenis yang tidak berubah; string dan angka selalu bisa menjadi 			kunci. Tuples dapat digunakan sebagai kunci jika hanya berisi string, angka, 	atau tupel; jika tuple berisi objek yang dapat berubah baik secara langsung 	atau tidak langsung, itu tidak dapat digunakan sebagai kunci. Anda tidak 		dapat menggunakan daftar sebagai kunci, karena daftar dapat dimodifikasi di 	tempat menggunakan tugas indeks, tugas slice, atau metode seperti tambahkan 	() dan perpanjang ().
	  	Yang terbaik adalah memikirkan kamus sebagai satu set kunci: pasangan nilai, dengan persyaratan bahwa kunci itu unik (dalam satu kamus).membuat kamus kosong: {}. Menempatkan daftar kunci yang dipisahkan koma: pasangan nilai dalam tanda kurung menambahkan kunci awal: pasangan nilai ke kamus; ini juga cara kamus ditulis pada output.
	  	Operasi utama pada kamus menyimpan nilai dengan beberapa kunci dan mengekstraksi nilai yang diberikan kunci. Anda juga dapat menghapus kunci: pasangan nilai dengan del. Jika Anda menyimpan menggunakan kunci yang sudah digunakan, nilai lama yang terkait dengan kunci itu terlupakan. Ini adalah kesalahan untuk mengekstrak nilai menggunakan kunci yang tidak ada.
	  	Melakukan daftar (d) pada kamus mengembalikan daftar semua kunci yang digunakan dalam kamus, dalam urutan penyisipan (jika Anda menginginkannya diurutkan, gunakan saja diurutkan (d) sebagai gantinya). Untuk memeriksa apakah kunci tunggal ada di kamus, gunakan kata kunci.

**5.6 Looping Techniques**
	  - Ketika mengulang melalui kamus, kunci dan nilai yang terkait dapat diambil 		pada saat yang sama menggunakan metode item ().
	  	Ketika perulangan melalui urutan, indeks posisi dan nilai yang sesuai dapat diambil pada saat yang sama menggunakan fungsi enumerasi ().
		Untuk mengulang lebih dari dua atau lebih urutan pada saat yang sama, entri dapat dipasangkan dengan fungsi zip ().
		Untuk mengulang urutan secara terbalik, pertama-tama tentukan urutan dalam arah maju dan kemudian panggil fungsi terbalik ().
		Untuk mengulang urutan dalam urutan yang diurutkan, gunakan fungsi yang diurutkan () yang mengembalikan daftar yang diurutkan baru saat meninggalkan sumber tidak berubah.
		Terkadang menggoda untuk mengubah daftar saat Anda mengulanginya; namun, seringkali lebih sederhana dan lebih aman untuk membuat daftar baru.

**5.7 More on Conditions**
	  - Kondisi yang digunakan dalam waktu dan jika pernyataan dapat mengandung 		operator, bukan hanya perbandingan.
	  	Operator pembanding memeriksa apakah suatu nilai terjadi (tidak terjadi) secara berurutan. Operator membandingkan apakah dua objek benar-benar objek yang sama; ini hanya penting untuk objek yang bisa berubah seperti daftar. Semua operator pembanding memiliki prioritas yang sama, yang lebih rendah daripada semua operator numerik.
		Perbandingan bisa dirantai. Sebagai contoh, a <b == c menguji apakah a kurang dari b dan selain itu b sama dengan c.
		Perbandingan dapat digabungkan menggunakan operator Boolean, dan hasil perbandingan (atau ekspresi Boolean lainnya) dapat dinegasikan dengan tidak. Ini memiliki prioritas yang lebih rendah daripada operator pembanding; di antara mereka, tidak memiliki prioritas tertinggi dan atau terendah, sehingga A dan bukan B atau C setara dengan (A dan (bukan B)) atau C. Seperti biasa, tanda kurung dapat digunakan untuk mengekspresikan komposisi yang diinginkan.
		Operator Boolean dan dan atau yang disebut operator hubungan singkat: argumen mereka dievaluasi dari kiri ke kanan, dan evaluasi berhenti segera setelah hasilnya ditentukan. Sebagai contoh, jika A dan C adalah benar tetapi B salah, A dan B dan C tidak mengevaluasi ekspresi C. Ketika digunakan sebagai nilai umum dan bukan sebagai Boolean, nilai kembali dari operator sirkuit pendek adalah yang terakhir argumen yang dievaluasi.

**5.8 Comparing Sequences and Other Types**
	  - Objek urutan dapat dibandingkan dengan objek lain dengan jenis urutan yang 		sama. Perbandingan ini menggunakan urutan leksikografis: pertama dua item 		pertama dibandingkan, dan jika mereka berbeda, ini menentukan hasil 			perbandingan; jika keduanya sama, dua item berikutnya akan dibandingkan, 		dan seterusnya, hingga urutannya habis. Jika dua item untuk dibandingkan 		adalah urutan dari jenis yang sama, perbandingan leksikografis dilakukan 		secara rekursif. Jika semua item dari dua urutan membandingkan sama, urutan 	dianggap sama. Jika satu urutan adalah sub-urutan awal yang lain, urutan 		yang lebih pendek adalah yang lebih kecil (lebih kecil). Pemesanan 				Lexicographical untuk string menggunakan nomor poin kode Unicode untuk 			memesan karakter individu. 