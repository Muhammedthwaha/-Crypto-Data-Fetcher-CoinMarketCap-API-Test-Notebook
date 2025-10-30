"""
Crypto Data Fetcher - CoinMarketCap API
This script fetches real-time cryptocurrency data from CoinMarketCap API
and displays it in a clean, organized format using Pandas.
"""

import os
import requests
import pandas as pd
from typing import Optional, Dict, List
from dotenv import load_dotenv


class CryptoDataFetcher:
    """
    A class to fetch and process cryptocurrency data from CoinMarketCap API.
    """
    
    BASE_URL = "https://pro-api.coinmarketcap.com/v1"
    PRICE_DECIMAL_THRESHOLD = 1.0
    BILLION = 1_000_000_000
    MILLION = 1_000_000
    THOUSAND = 1_000
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the CryptoDataFetcher.
        
        Args:
            api_key: CoinMarketCap API key. If not provided, will try to read from environment.
        """
        # Load environment variables from .env file if it exists
        load_dotenv()
        
        self.api_key = api_key or os.getenv('COINMARKETCAP_API_KEY')
        if not self.api_key:
            raise ValueError("API key is required. Set COINMARKETCAP_API_KEY environment variable or pass it as parameter.")
        
        self.headers = {
            'X-CMC_PRO_API_KEY': self.api_key,
            'Accept': 'application/json'
        }
    
    def get_latest_listings(self, limit: int = 10, convert: str = 'USD') -> pd.DataFrame:
        """
        Fetch the latest cryptocurrency listings.
        
        Args:
            limit: Number of cryptocurrencies to fetch (default: 10)
            convert: Currency to convert prices to (default: 'USD')
            
        Returns:
            DataFrame containing cryptocurrency data
        """
        url = f"{self.BASE_URL}/cryptocurrency/listings/latest"
        parameters = {
            'limit': limit,
            'convert': convert
        }
        
        try:
            response = requests.get(url, headers=self.headers, params=parameters)
            response.raise_for_status()
            data = response.json()
            
            if data['status']['error_code'] != 0:
                raise Exception(f"API Error: {data['status']['error_message']}")
            
            return self._process_listings_data(data['data'], convert)
        
        except requests.exceptions.RequestException as e:
            raise Exception(f"Request failed: {str(e)}")
    
    def _process_listings_data(self, data: List[Dict], convert: str) -> pd.DataFrame:
        """
        Process raw API data into a clean Pandas DataFrame.
        
        Args:
            data: Raw data from API response
            convert: Currency used for conversion
            
        Returns:
            Processed DataFrame
        """
        processed_data = []
        
        for crypto in data:
            quote = crypto['quote'][convert]
            processed_data.append({
                'Rank': crypto['cmc_rank'],
                'Name': crypto['name'],
                'Symbol': crypto['symbol'],
                'Price': quote['price'],
                'Market Cap': quote['market_cap'],
                'Volume (24h)': quote['volume_24h'],
                'Change (1h)': quote['percent_change_1h'],
                'Change (24h)': quote['percent_change_24h'],
                'Change (7d)': quote['percent_change_7d'],
                'Circulating Supply': crypto['circulating_supply']
            })
        
        df = pd.DataFrame(processed_data)
        
        # Format the DataFrame for better readability
        df = self._format_dataframe(df)
        
        return df
    
    def _format_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Format DataFrame columns for better display.
        
        Args:
            df: Input DataFrame
            
        Returns:
            Formatted DataFrame
        """
        # Format price with 2 decimal places for values > threshold, more for smaller values
        df['Price'] = df['Price'].apply(
            lambda x: f"${x:,.2f}" if x >= self.PRICE_DECIMAL_THRESHOLD else f"${x:,.6f}"
        )
        
        # Format large numbers with K, M, B suffixes
        df['Market Cap'] = df['Market Cap'].apply(self._format_large_number)
        df['Volume (24h)'] = df['Volume (24h)'].apply(self._format_large_number)
        df['Circulating Supply'] = df['Circulating Supply'].apply(lambda x: f"{x:,.0f}" if pd.notna(x) else 'N/A')
        
        # Format percentage changes
        for col in ['Change (1h)', 'Change (24h)', 'Change (7d)']:
            df[col] = df[col].apply(lambda x: f"{x:+.2f}%" if pd.notna(x) else 'N/A')
        
        return df
    
    def _format_large_number(self, num: float) -> str:
        """
        Format large numbers with K, M, B suffixes.
        
        Args:
            num: Number to format
            
        Returns:
            Formatted string
        """
        if pd.isna(num):
            return 'N/A'
        
        if num >= self.BILLION:
            return f"${num / self.BILLION:,.2f}B"
        elif num >= self.MILLION:
            return f"${num / self.MILLION:,.2f}M"
        elif num >= self.THOUSAND:
            return f"${num / self.THOUSAND:,.2f}K"
        else:
            return f"${num:,.2f}"
    
    def display_data(self, df: pd.DataFrame):
        """
        Display the DataFrame in a clean format.
        
        Args:
            df: DataFrame to display
        """
        print("\n" + "="*100)
        print("CRYPTOCURRENCY DATA - POWERED BY COINMARKETCAP")
        print("="*100 + "\n")
        print(df.to_string(index=False))
        print("\n" + "="*100 + "\n")


def main():
    """
    Main function to demonstrate the CryptoDataFetcher usage.
    """
    try:
        # Initialize the fetcher
        fetcher = CryptoDataFetcher()
        
        # Fetch top 10 cryptocurrencies
        print("Fetching top 10 cryptocurrencies...")
        df = fetcher.get_latest_listings(limit=10)
        
        # Display the data
        fetcher.display_data(df)
        
        # You can also work with the DataFrame for further analysis
        print("Summary Statistics:")
        print(f"Total cryptocurrencies fetched: {len(df)}")
        
    except ValueError as e:
        print(f"Configuration Error: {e}")
        print("\nTo use this script, you need a CoinMarketCap API key.")
        print("1. Get your free API key from: https://coinmarketcap.com/api/")
        print("2. Set it as an environment variable: export COINMARKETCAP_API_KEY='your-api-key'")
        print("3. Or create a .env file with: COINMARKETCAP_API_KEY=your-api-key")
    
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
