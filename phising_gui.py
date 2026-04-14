import tkinter as tk
import re
import joblib

model = joblib.load('phishing_model.pkl')

def extract_features(url):
    url_length = len(url)
    has_https = 1 if url.startswith("https") else 0
    has_ip = 1 if re.search(r"\d+\.\d+\.\d+\.\d+", url) else 0
    dot_count = url.count('.')
    has_at = 1 if '@' in url else 0
    has_hyphen = 1 if '-' in url else 0
    has_double_slash = 1 if url.count('//') > 1 else 0
    has_suspicious_word = 1 if any(word in url.lower() for word in ["login","verify","bank","secure","update"]) else 0
    return [
        url_length,
        has_https,
        has_ip,
        dot_count,
        has_at,
        has_hyphen,
        has_double_slash,
        has_suspicious_word
    ]
def predict_url():
    url = entry.get()
    features = extract_features(url)
    
    prediction = model.predict([features])[0]
    probability = model.predict_proba([features])[0][1] * 100

    if prediction == 0:
        result_label.config(
            text=f"Legitimate Website ✅\nRisk Score: {probability:.2f}%",
            fg="green"
        )
        root.configure(bg="#d4edda")
    else:
        result_label.config(
            text=f"Phishing Website ❌\nRisk Score: {probability:.2f}%",
            fg="red"
        )
        root.configure(bg="#f8d7da")

root = tk.Tk()
root.title("AI Phishing Website Detector")
root.geometry("500x250")

tk.Label(root, text="Enter Website URL:", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack()

tk.Button(root, text="Check Website", command=predict_url).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

root.mainloop()