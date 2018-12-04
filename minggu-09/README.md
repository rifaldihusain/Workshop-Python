# minggu-09

# Tutorial Modul pada [Bab - 12](https://docs.python.org/3/tutorial/venv.html)

1. python -m venv tutorial-env => membuat virtual environment yg akan ditempatkan di direktori lokal.

2. tutorial-env\Scripts\activate.bat => membuat direktori tutorial-env jika belom ada, yg didalamnya
   berisi salinan interpreter python, pustaka standar, dan berbagai file pendukung. ini perintah yg berjalan di windows.

3. python => mengaktifkan python dan mengetahui versi python yg terinstall
   >>> import sys
   >>> sys.path => mengimpor sys.path

4. https://bootstrap.pypa.io/get-pip.py => download get-pip python

5. python get-pip.py => install get-pip python

6. (tutorial-env) $ pip search astronomy => paket-paket yg ada didalam pip

7. (tutorial-env) $ pip install novas => menginstall salah satu paket pip yg bernama novas

8. (tutorial-env) $ pip install requests==2.6.0 => dapat juga menginstal versi spesifik paket 
   dengan memberikan nama paket diikuti dengan == dan nomor versi

9. (tutorial-env) $ pip install --upgrade requests => Jika Anda menjalankan ulang perintah ini, 
   pip akan melihat bahwa versi yang diminta sudah diinstal dan tidak melakukan apa-apa. 
   Anda dapat memberikan nomor versi yang berbeda untuk mendapatkan versi itu, 
   atau Anda dapat menjalankan instalasi pip --upgrade untuk meningkatkan paket ke versi terbaru

10. (tutorial-env) $ pip show requests => pip akan menampilkan informasi tentang paket tertentu
    atau menampilkan informasi dari pip itu sendiri.

11. (tutorial-env) $ pip list => menampilkan semua paket yg terdapat di virtual environment

12. (tutorial-env) $ pip freeze > requirements.txt
	(tutorial-env) $ cat requirements.txt
	=> pip freeze akan menghasilkan daftar serupa dari paket-paket yang terinstal, 
	tetapi output menggunakan format yang diharapkan oleh instalasi pip. Konvensi umum adalah menempatkan daftar ini dalam file requirements.txt

13. (tutorial-env) $ pip install -r requirements.txt => Requirements.txt kemudian dapat berkomitmen untuk kontrol versi dan dikirim sebagai bagian dari aplikasi. 
    Pengguna kemudian dapat menginstal semua paket yang diperlukan dengan menginstal -r