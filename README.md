# 🏋️ Smart Workout Tracker [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python-based application that automatically tracks workouts using natural language input, calculates exercise metrics via the Nutritionix API, and logs results to a Google Sheet using Sheety.

![Workflow Demo](https://img.shields.io/badge/Demo-Available-green) [![GitHub Stars](https://img.shields.io/github/stars/masood2004/workout-tracking-using-google-sheets?style=social)](https://github.com/masood2004/workout-tracking-using-google-sheets)

## ✨ Features
- **Natural Language Processing**: Input exercises in plain English (e.g., "ran 5km and cycled 20 minutes")
- **Real-Time Metrics**: Fetches calories burned, duration, and exercise type via Nutritionix API
- **Google Sheets Integration**: Automatically logs workouts with timestamps using Sheety
- **Environment Security**: Uses `.env` for secure API key management
- **Error Handling**: Robust error checking for API failures and invalid inputs

## 🛠️ Prerequisites
- Python 3.8+
- [Nutritionix API](https://www.nutritionix.com/business/api) account
- [Sheety](https://sheety.co/) account (for Google Sheets integration)
- Google Sheet setup with [template columns](#-google-sheets-setup)

## ⚙️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/masood2004/workout-tracking-using-google-sheets.git
   cd workout-tracking-using-google-sheets
   ```
2. Install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Create `.env` file:
   ```env
   APP_ID="your_nutritionix_app_id"
   API_KEY="your_nutritionix_api_key"
   ```

## 🔑 API Configuration
### Nutritionix Setup
1. Get API credentials from [Nutritionix Dashboard](https://developer.nutritionix.com/)
2. Add credentials to `.env`

### Sheety/Google Sheets Setup
1. Create a new project in [Sheety](https://sheety.co/)
2. Connect to Google Sheets with these columns:
   ```
   Date | Time | Exercise | Duration | Calories
   ```
3. Replace `SHEETY_API_URL` in `main.py` with your Sheety endpoint.

## 🚀 Usage
Run the program:
```bash
python main.py
```
**Example Input:**
```
Tell me what exercise you did today: ran 3km and did 30 minutes of weight training
Gender: male
Weight (kg): 75
Height (cm): 180
Age: 25
```

**Output in Google Sheets:**
| Date       | Time         | Exercise          | Duration | Calories |
|------------|--------------|-------------------|----------|----------|
| 15/Sep/2023 | 03:45:30 PM  | Running           | 27       | 298      |
| 15/Sep/2023 | 03:45:30 PM  | Weight Training   | 30       | 177      |


## 🤝 Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License
Distributed under the MIT License. See [LICENSE](./LICENSE) for details.

## 🙏 Acknowledgments
- Nutritionix for the exercise data API
- Sheety for seamless Google Sheets integration
- Python community for awesome open-source tools

---

**Happy Tracking!** 🔥 Let's crush those fitness goals! 💪
