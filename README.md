# 💧 Water Potability Prediction API

Sebuah mini-proyek berbasis **FastAPI** yang dapat memprediksi **kelayakan air minum**, berdasarkan beberapa faktor kualitas air.

## 📁 Struktur File
```
├── main.py             # Endpoint API utama
├── model.pkl           # File model Machine Learning yang telah dilatih
├── scaler.pkl          # File scaler untuk normalisasi fitur input
├── requirements.txt    # Daftar dependency yang dibutuhkan
```

## 🚀 Fitur API
```
- Prediksi kelayakan air minum
- Menerima input melalui metode POST
- Hasil prediksi: '0 untuk Unsafe to Drink', '1 untuk Safe to Drink'
```

## ⚙️ Cara Menjalankan

### 1. Clone Repositori

```cmd
git clone https://github.com/AryaWirawwn/water-potability-prediction-api.git
cd water-potability-prediction-api
```

### 2. Buat Virtual Environment

```cmd
python -m venv .env
.env\Scripts\activate
```

### 3. Install Dependensi

```cmd
pip install -r requirements.txt
```

### 4. Jalankan API

```cmd
fastapi dev main.py
```

### 5. Akses Swagger UI

Buka browser ke:  
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 🧪 Contoh JSON Input

```json
{
  "ph": 7,
  "Hardness": 256,
  "Solids": 11245,
  "Chloramines": 7,
  "Sulfate": 329,
  "Organic_carbon": 15,
  "Trihalomethanes": 51
}
```

## ✅ Contoh Output

```json
{
  "ph": 7,
  "prediction": 0,
  "result": "Unsafe to Drink"
}
```


> Dibuat sebagai bagian dari praktik tahap **Deployment** dalam metode **CRISP-DM**.  
> Proyek ini dapat dijadikan dasar pengembangan API prediksi sederhana lainnya.
