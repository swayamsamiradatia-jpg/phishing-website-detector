import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Sample dataset (You can expand later)
data = {
    'url_length': [54, 120, 30, 200, 80, 150],
    'has_https': [1, 0, 1, 0, 1, 0],
    'has_ip': [0, 1, 0, 1, 0, 1],
    'dot_count': [2, 6, 1, 8, 3, 7],
    'has_at': [0, 1, 0, 1, 0, 1],
    'has_hyphen': [0, 1, 0, 1, 0, 1],
    'has_double_slash': [0, 1, 0, 1, 0, 1],
    'has_suspicious_word': [0, 1, 0, 1, 0, 1],
    'label': [0, 1, 0, 1, 0, 1]
}


df = pd.DataFrame(data)

X = df.drop('label', axis=1)
y = df['label']

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, 'phishing_model.pkl')

print("Model Trained Successfully!")