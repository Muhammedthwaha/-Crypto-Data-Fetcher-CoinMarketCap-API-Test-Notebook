# Crypto Data Fetcher - CoinMarketCap API Test Notebook

This project demonstrates how to connect to the **CoinMarketCap API** to fetch real-time cryptocurrency data and display it in a clean, organized format using **Python**. It's a practical example of API usage, data transformation, and Pandas integration for analysis-ready datasets.

## Features

- 🔍 Fetch real-time cryptocurrency data from CoinMarketCap API
- 📊 Clean data transformation using Pandas
- 💰 Format prices, market caps, and volumes for readability
- 📈 Display percentage changes (1h, 24h, 7d)
- 📓 Interactive Jupyter notebook for exploration
- 🎯 Easy-to-use Python class with methods for data fetching

## Prerequisites

- Python 3.7 or higher
- CoinMarketCap API key (get your free key at [https://coinmarketcap.com/api/](https://coinmarketcap.com/api/))

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Muhammedthwaha/-Crypto-Data-Fetcher-CoinMarketCap-API-Test-Notebook.git
   cd -Crypto-Data-Fetcher-CoinMarketCap-API-Test-Notebook
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your API key:
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and add your CoinMarketCap API key:
     ```
     COINMARKETCAP_API_KEY=your-api-key-here
     ```

## Usage

### Using the Python Script

Run the script directly to fetch and display the top 10 cryptocurrencies:

```bash
python crypto_fetcher.py
```

### Using the Jupyter Notebook

1. Start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

2. Open `crypto_api_test.ipynb` in your browser

3. Follow the notebook cells to:
   - Fetch cryptocurrency data
   - Display formatted results
   - Perform data analysis
   - Visualize trends

### Using the CryptoDataFetcher Class

```python
from crypto_fetcher import CryptoDataFetcher

# Initialize the fetcher
fetcher = CryptoDataFetcher()

# Fetch top 10 cryptocurrencies
df = fetcher.get_latest_listings(limit=10)

# Display the data
fetcher.display_data(df)

# Fetch more cryptocurrencies
df_20 = fetcher.get_latest_listings(limit=20)
```

## Example Output

```
====================================================================================================
CRYPTOCURRENCY DATA - POWERED BY COINMARKETCAP
====================================================================================================

Rank  Name          Symbol  Price        Market Cap    Volume (24h)  Change (1h)  Change (24h)  Change (7d)  Circulating Supply
   1  Bitcoin       BTC     $45,123.45   $850.23B      $25.45B       +0.50%       +2.34%        +5.67%       18,900,000
   2  Ethereum      ETH     $3,456.78    $415.67B      $15.23B       +0.35%       +1.89%        +4.23%       120,500,000
...
====================================================================================================
```

## Project Structure

```
.
├── crypto_fetcher.py         # Main Python script with CryptoDataFetcher class
├── crypto_api_test.ipynb     # Jupyter notebook for interactive exploration
├── requirements.txt          # Python dependencies
├── .env.example             # Example environment variables file
├── .gitignore               # Git ignore file
└── README.md                # This file
```

## API Reference

### CryptoDataFetcher Class

#### Methods

- `__init__(api_key=None)`: Initialize the fetcher with an API key
- `get_latest_listings(limit=10, convert='USD')`: Fetch latest cryptocurrency listings
- `display_data(df)`: Display DataFrame in a formatted view

## Data Fields

The fetched data includes:

- **Rank**: Market cap ranking
- **Name**: Cryptocurrency name
- **Symbol**: Cryptocurrency symbol/ticker
- **Price**: Current price in USD
- **Market Cap**: Total market capitalization
- **Volume (24h)**: 24-hour trading volume
- **Change (1h)**: Percentage change in last 1 hour
- **Change (24h)**: Percentage change in last 24 hours
- **Change (7d)**: Percentage change in last 7 days
- **Circulating Supply**: Amount of cryptocurrency in circulation

## Dependencies

- `requests`: HTTP library for API calls
- `pandas`: Data manipulation and analysis
- `python-dotenv`: Environment variable management
- `jupyter`: Interactive notebook environment

## Notes

- The free CoinMarketCap API tier has usage limits
- Data is fetched in real-time and reflects current market conditions
- Prices and market data are subject to rapid changes

## License

This project is open source and available for educational purposes.

## Contributing

Contributions, issues, and feature requests are welcome!

## Author

Muhammed Thaha Uwais

## Acknowledgments

- Data provided by [CoinMarketCap](https://coinmarketcap.com/)
- Built with Python, Pandas, and Jupyter
