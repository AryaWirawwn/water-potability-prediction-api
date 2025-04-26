from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

# Inisialisasi FastAPI
app = FastAPI(title="Water Potability Prediction API")

# Load model dan scaler
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Skema input
class Water(BaseModel):
    ph:float
    Hardness:float
    Solids:float
    Chloramines:float
    Sulfate:float
    Organic_carbon:float
    Trihalomethanes:float

# Fungsi kategori ph
def categorize_ph(ph):
    if pd.isna(ph):
        return 'Unknown'
    elif ph < 6.5:
        return 'Acidic'
    elif ph <= 8.5:
        return 'Neutral'
    else:
        return 'Alkaline'

def preprocess_input(data: Water):
    # Buat DataFrame dari input
    df = pd.DataFrame([{
        "ph":data.ph,
        "Hardness":data.Hardness,
        "Solids":data.Solids,
        "Chloramines":data.Chloramines,
        "Sulfate": data.Sulfate,
        "Organic_carbon": data.Organic_carbon,
        "Trihalomethanes": data.Trihalomethanes,
    }])

    df['ph_category'] = df['ph'].apply(categorize_ph)
    df['ph_category'] = df['ph_category'].map({'Acidic':0,'Neutral':1, 'Alkaline':2})

    df['ph_hardness_ratio'] = df['ph'] / (df['Hardness'] + 1e-6)
    df['solids_chloramines_sum'] = df['Solids'] + df['Chloramines']
    df['organic_trihalo'] = df['Organic_carbon'] * df['Trihalomethanes']

    # One-hot encoding untuk 'ph_category'
    df = pd.get_dummies(df, columns=['ph_category'], prefix='ph')

    # Pastikan semua kolom dummy tersedia
    for col in ["ph_0", "ph_1", "ph_2"]:
        if col not in df.columns:
            df[col] = 0

    # Urutkan kolom agar sesuai dengan model
    df = df[[ 
        "ph", "Hardness", "Solids", "Chloramines", "Sulfate", "Organic_carbon",
        "ph_hardness_ratio", "solids_chloramines_sum", "organic_trihalo", "ph_0", "ph_1", "ph_2"
    ]]


    # Normalisasi
    df_scaled = scaler.transform(df)
    return df_scaled

@app.get("/")
def read_root():
    return {"message": "Water Potability Prediction API is running"}

# Endpoint prediksi
@app.post("/predict")
def predict_water(data: Water):
    processed = preprocess_input(data)
    prediction = model.predict(processed)[0]
    result = "Safe to Drink" if prediction == 1 else "Unsafe to Drink"
    return {
        "ph": data.ph,
        "prediction": int(prediction),
        "result": result
    }