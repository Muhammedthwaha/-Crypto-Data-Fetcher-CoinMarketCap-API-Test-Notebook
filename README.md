# 💹 Crypto Data Fetcher — CoinMarketCap API Test Notebook

This project demonstrates how to connect to the **CoinMarketCap API** to fetch real-time cryptocurrency data and display it in a clean, organized format using **Python**.  
It’s a practical example of API usage, data transformation, and Pandas integration for analysis-ready datasets.

---

## 📘 Description
The notebook shows how to:
- Send authenticated API requests to CoinMarketCap’s `/cryptocurrency/listings/latest` endpoint.
- Retrieve details of the top cryptocurrencies (price, symbol, rank, etc.).
- Normalize the JSON response into a Pandas DataFrame.
- Automatically add timestamps for each data fetch.
- Create a reusable function (`api_runner`) to refresh data dynamically.

---

## 🚀 Features
✅ Connects securely to the CoinMarketCap REST API  
✅ Fetches top cryptocurrency listings in USD  
✅ Converts complex JSON into a structured DataFrame  
✅ Includes a function to automate data retrieval  
✅ Ready for expansion — ideal for dashboards or time-series tracking  

---

## 🧩 Technologies Used
- **Python 3**
- **Requests**
- **Pandas**
- **JSON**

---

## ⚙️ How to Use
1. Clone or download this notebook.
2. Open `How to use an Api + Api Test Notebook.ipynb` in **Jupyter Notebook** or **VS Code**.
3. Replace the sample API key in the code:
   ```python
   headers = {
       'Accepts': 'application/json',
       'X-CMC_PRO_API_KEY': 'YOUR_API_KEY_HERE'
   }
   ```
4. Run all cells — the notebook will:
   - Fetch real-time crypto data.
   - Display it in a readable DataFrame format.

---

## 🧮 Example Output
| name      | symbol | quote.USD.price | timestamp           |
|------------|---------|-----------------|---------------------|
| Bitcoin    | BTC     | 67,000.12       | 2025-10-30 19:10:00 |
| Ethereum   | ETH     | 3,200.45        | 2025-10-30 19:10:00 |

---

## 📫 Author
**Muhammed Thaha Uwais**  
📧 [muhammedthahauwais@gmail.com](mailto:muhammedthahauwais@gmail.com)  
🔗 [LinkedIn][https://www.linkedin.com/in/muhammed-thaha-uwais-5b5444279](https://www.linkedin.com/in/muhammed-thaha-uwais-5b5444279)

---

## 🪪 License
This project is free to use for educational and personal learning purposes.
