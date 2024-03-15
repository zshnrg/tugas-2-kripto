# Krip-Chip!

![alt text](/doc/header.png "Krip-Chip Icon")

  
<p align="center">
Repositori ini merupakan sebuah project aplikasi <b>Krip-Chip!</b>, program yang menyediakan algoritma enkripsi RC4 termodifikasi pada aplikasi mobile untuk memenuhi <b>Tugas 2 II4031 2024: Program Modifikasi RC4 dengan Konsep Extended Vigenere Cipher</b>
</p>

<br>

<p align="center">
18221121 Natasya Vercelly Harijadi - 18221121 Rozan Ghosani
</p>

<p align="center">
  <a href="#about">About</a> |
  <a href="#system-requirement">System Requirements</a> |
  <a href="#installation---android">Installation (Android)</a> |
  <a href="#installation---windows">Installation (Windows)</a> |
  <a href="#features">Features</a>
</p>

## About

Krip-Chip! merupakan multi-platform yang difokuskan pada aplikasi mobile yang dirancang untuk menyediakan fungsi enkripsi dan dekripsi yang aman dengan menggabungkan modifikasi RC4 dengan konsep Extended Vigenere Cipherdan Playfair Cipher. Dengan aplikasi ini, pengguna dapat dengan mudah mengamankan pesan teks atau berkas biner.

Aplikasi ini dapat melakukan enkripsi pada pesan teks dan mendekripsi cipherteks kembali menjadi pesan teks asli, memastikan komunikasi yang aman. Selain itu, untuk pesan teks, aplikasi dapat menampilkan pesan teks asli dan cipherteks dalam format layer, seperti format string atau dalam format base64. Pengguna juga dapat menyimpan cipherteks ke dalam berkas terenkripsi custom untuk keamanan tambahan. Fleksibilitas kunci juga diberikan, memungkinkan pengguna untuk memasukkan kunci sesuai keinginan mereka tanpa batasan panjang

Program ini ditulis dalam bahasa Python yang dibantu dengan library Flet (Flutter) untuk membuat program kompatibel dengan sistem operasi Android.

## System Requirement

- Python 3.8 atau lebih baru.
- Library Flet versi terbaru
- Flutter SDK 3.16 atau lebih baru (apabila ingin melakukan build)
- Developer mode pada Windows 11
- Visual Studio Code

Spesifikasi lebih lanjut dapat dilihat melalui [pranala ini](https://flet.dev/docs/guides/python/packaging-app-for-distribution).

## Installation - Android

1. Lihat rilis terbaru aplikasi ini di [GitHub](https://github.com/zshnrg/tugas-2-kripto/releases)
2. Unduh aplikasi dengan ekstensi `.apk`
3. Install aplikasi yang telah diunduh

Instalasi juga dapat dilakukan dengan menggunakan bantuan komputer melalui [adb](https://www.makeuseof.com/install-apps-via-adb-android/) (Android Debug Bridge) tool.

```sh
adb install <path-to-your.apk>
```

## Installation - Windows

### Cloning repository

1. Pada halaman utama repository [GitHub](https://github.com/zshnrg/tugas-2-kripto), buka menu **Clone** lalu salin URL dari repository
2. Buka Terminal
3. Pindah ke direktori yang diinginkan
4. Ketikan `git clone`, lalu tempelkan URL yang telah disalin tadi 
   ```sh
   git clone https://github.com/zshnrg/tugas-2-kripto.git
   ```
   
5. Tekan **Enter** untuk membuat *local clone*
   ```sh
   $ git clone https://github.com/zshnrg/tugas-2-kripto.git
    > Cloning into `tugas-2-kripto`...
    > remote: Counting objects: 10, done.
    > remote: Compressing objects: 100% (8/8), done.
    > remove: Total 10 (delta 1), reused 10 (delta 1)
    > Unpacking objects: 100% (10/10), done.
   ``` 

6. Install modul Flet dengan perintah
    ```sh
    pip install flet
    ```

### Running the app
1. Jalankan terminal pada repositori
2. Ketika perintah berikut ini sesuai dengan device yang diinginkan

    Aplikasi dijalankan di komputer secara langsung
    ```sh
        flet run
    ```

    Aplikasi dijalankan di device Android melalui aplikasi [Flet](https://play.google.com/store/apps/details?id=com.appveyor.flet)
    ```sh
        flet run --android
    ```

    Aplikasi dijalankan di device iOS melalui aplikasi [Flet](https://apps.apple.com/app/flet/id1624979699)
    ```sh
        flet run --ios
    ```
### Building the app

Saat ini aplikasi Krip-Chip! hanya dibuat kompatibel untuk dibuild di Android. Namun, aplikasi tetap bisa dijalankan di sistem operasi manapun dengan bantuan Flet. Untuk melakukan build pastikan requirements berikut ini sudah terinstall:

- Library Flet versi terbaru
- Flutter SDK 3.16 atau lebih baru (apabila ingin melakukan build)
- Developer mode pada Windows 11
- Visual Studio Code

Kemudian jalankan perintah berikut ini pada terminal di direktori `Krip-Chip/`

```sh
flet build apk
```

Tunggu 5-20 menit hingga aplikasi telah berhasil di-build

```
Creating Flutter bootstrap project...OK
Customizing app icons and splash images...OK    
Generating app icons...OK
Generating splash screens...OK
Packaging Python app...OK
Building .apk for Android...OK
Copying build to build\apk directory...OK
Success!
```

## Features
Program ini memiliki fitur:
- Enkripsi dan dekripsi dengan RC4 yang telah dimodifikasi
- Kustomisasi kunci atau randomize kunci
- Pengenkripsi dan dekripsian file dan text ketikkan