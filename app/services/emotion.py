from app.models.ml_model import model, label_encoder
from app.utils.audio import extract_features
import tempfile

def predict_from_audio(upload_file):
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(upload_file.file.read())
        tmp_path = tmp.name

    features = extract_features(tmp_path)
    prediction = model.predict(features)
    emotion = label_encoder.inverse_transform(prediction)[0]

    return emotion
