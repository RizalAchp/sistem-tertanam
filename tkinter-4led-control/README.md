
---
## Nyoba Python-Tk pertama

---
### Desclaimer
untuk kalian yang masih bingung bagaimana caranya, tidak perlu kawatir. disini saya akan menjelaskan secara singkat
1. pertama2, tkinter mmerupakan library  gui yang dapat digunakan di beberapa bahasa pemrograman, tidak hanya python
2. tkinter itu *multi platform* atau dapat di katakan, tersedia dan dapat berjalan di windows,mac, maupun linux.
3. penggunaan library ini dalam segi kesulitan dalam memrogram bisa dikatakan tidak terlalu mudah dan tidak terlalu susah :v **avarage**

### first take
1. pertama, **SUDAH PASTI HARUS DOWNLOAD PYTHON** misal mungkin kalian belum menginstallnya. bisa [sini](https://www.python.org/downloads/)
2. kedua, setelah yakin **python** sudah terinstall, coba buka terminal (cmd / powershell) *saya sarankan powershell aja* terus ketik

```fish
python -m tkinter
```

atau 

```fish
python -m Tkinter
```

jika output seperti gif dibawah maka tkinter sudah tersedia di dalam python kalian, karena kebanyakan python di windows sudah ada tkinter

<p align="center">
  <img src="https://github.com/RizalAchp/sistem-tertanam/blob/main/contoh.gif">
</p>

beres dah, tinggal ngoding

### untuk kodinganku
jika kalian ingin mencoba punyaku, pertama2 yang harus kamu lakukan adalah install requirements yang berada pada [requirements.txt](https://github.com/RizalAchp/sistem-tertanam/blob/main/tkinter-4led-control/requirements.txt)
dengan cara :

clone project

```fish
git clone https://github.com/RizalAchp/sistem-tertanam.git
```

install requirements : 

```fish
pip install -r requirements.txt
```

dan jalankan programnya :

```fish
python ./button-led.py
```

beres!
**oh iya, port board arduinonya di ganti bagi kalian yang memakai windows, karena saya pake port /dev/ttyACM0**
