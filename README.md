## 📈 Real-Time Stock Market Dashboard

A modern, interactive dashboard built with Python and Streamlit for real-time stock analysis. This application allows users to fetch intraday data for any specified stock symbol, visualize price movements with interactive candlestick charts, and analyze key financial indicators.

<img width="1895" height="947" alt="Screenshot 2025-10-13 180818" src="https://github.com/user-attachments/assets/881604d5-9602-49ee-9cc3-5564e7aa85a5" />

<img width="1907" height="942" alt="Screenshot 2025-10-13 145954" src="https://github.com/user-attachments/assets/f607f022-4dbf-4ceb-903d-188d5c2fb73a" />


## ✨ Key Features


● Real-Time Data Fetching : Fetches up-to-the-minute intraday stock data (from 1-min to
60-min intervals) using the Alpha Vantage API.

● Interactive Candlestick Charts : Utilizes Plotly to visualize price action (Open, High,
Low, Close) in a dynamic chart.

● Technical Analysis : Automatically calculates and overlays:

  ○ 20-Period Moving Average (MA) for trend smoothing.

  ○ 14-Period Relative Strength Index (RSI) for momentum analysis.

● User-Friendly Interface : Features a simple sidebar for symbol and interval selection,
making it easy to analyze different assets on demand.

## ⚙ Tech Stack

This project is built primarily on the Python data science ecosystem and is fully containerized
using Docker.

| **Category** | **Component** | **Description** | 
| :--- | :--- | :--- | 
| **Language** | Python | Main programming language (`3.11-slim` base image). | 
| **Web App** | **Streamlit** | Framework used for creating and serving the interactive dashboard. | 
| **Data Handling** | **Pandas** | Essential library for data structure (DataFrame) and time-series analysis. | 
| **Visualization** | **Plotly** | Used to render high-quality, interactive candlestick and line charts. | 
| **API Client** | Requests | Standard library for making external HTTP calls to the data API. | 
| **Data Source** | **Alpha Vantage** | External API providing intraday stock market data. | 
| **Deployment** | **Docker & Docker Compose** | Used to ensure a consistent, portable, and easily deployable application environment. |


## 🚀 Quick Start (Docker)

The recommended way to run this application is using Docker Compose, which handles the
environment setup automatically.

### 1. Prerequisites

You must have Docker and Docker Compose installed on your machine.

### 2. Set Up Environment

1. **Obtain API Key** : Get a free API key from Alpha Vantage.
2. **Configure .env** : Create a file named .env in the root directory and populate it with your
    key and settings:
    API_KEY=YOUR_ALPHA_VANTAGE_API_KEY
    API_BASE=[https://www.alphavantage.co/query](https://www.alphavantage.co/query)
    REFRESH_INTERVAL=
    _(Note: The REFRESH_INTERVAL is the data cache duration in seconds)_

### 3. Build and Run the Container

Run the following command from the project root:
docker compose up --build

### 4. Access the Dashboard

Once the service is running, open your web browser and navigate to:
🌐 **[http://localhost:](http://localhost:)**


## 💻 Local Development


If you prefer to run the application directly on your local machine:

1. **Clone the Repository.**
2. **Install Dependencies** : Install all required Python packages listed in requirements.txt:
    pip install -r requirements.txt
3. **Set Environment** : Ensure your .env file with the API_KEY is configured in the root
    directory.
4. **Run the App** : Execute the main Streamlit application:
    streamlit run app.py















