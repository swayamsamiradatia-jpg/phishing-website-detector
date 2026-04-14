# AI Phishing Website Detector

This project is a machine learning based phishing website detection system.  
The system analyzes a given URL and predicts whether the website is legitimate or a phishing website.

## Technologies Used
- Python
- Tkinter (GUI)
- Scikit-learn
- Machine Learning
- Random Forest Algorithm

## Features
- Detect phishing websites
- Analyze URL security features
- Display prediction with risk score
- Simple graphical user interface

## How It Works

1. User enters a website URL.
2. The system extracts features from the URL such as:
   - HTTPS usage
   - URL length
   - Presence of IP address
   - Suspicious keywords
3. The machine learning model analyzes these features.
4. The system predicts whether the website is **legitimate** or **phishing**.

## Project Interface

![Phishing Detector Interface](screenshot/interface.png)

## Example Output

The program displays:

- **Legitimate Website ✅**
- **Phishing Website ❌**
- Risk score percentage

## Author
Swayam Adatia
