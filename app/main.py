from fastapi import FastAPI, HTTPException
import yfinance as yf

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "OK"}

def format_ticker(ticker_symbol: str) -> str:
    """
    Adiciona '.SA' ao final do ticker, caso ele não tenha.
    """
    if not ticker_symbol.endswith(".SA"):
        ticker_symbol += ".SA"
    return ticker_symbol

def fetch_stock_info(ticker_symbol: str):
    try:
        # Adiciona '.SA' se necessário
        ticker_symbol = format_ticker(ticker_symbol)

        # Inicializa o objeto Ticker
        stock = yf.Ticker(ticker_symbol)
        
        # Informações gerais sobre a empresa
        info = stock.info
        
        # Dividendos históricos
        dividends = stock.dividends
        
        # Informações detalhadas sobre a ação
        data = {
            "full_name": info.get("longName", "Unavailable"),
            "sector": info.get("sector", "Unavailable"),
            "industry": info.get("industry", "Unavailable"),
            "official_website": info.get("website", "Unavailable"),
            "address": f"{info.get('address1', 'Unavailable')}, {info.get('city', '')}, {info.get('country', '')}",
            "phone": info.get("phone", "Unavailable"),
            "logo_url": info.get("logo_url", "Unavailable"),
            "current_price": info.get("regularMarketPrice", "Unavailable"),
            "opening_price": info.get("regularMarketOpen", "Unavailable"),
            "previous_close": info.get("regularMarketPreviousClose", "Unavailable"),
            "traded_volume": info.get("regularMarketVolume", "Unavailable"),
            "market_cap": info.get("marketCap", "Unavailable"),
            "pe_trailing": info.get("trailingPE", "Unavailable"),
            "pe_forward": info.get("forwardPE", "Unavailable"),
            "dividend_yield_percentage": info.get("dividendYield", "Unavailable"),
            "beta": info.get("beta", "Unavailable"),
            "number_of_employees": info.get("fullTimeEmployees", "Unavailable"),
            "quarterly_earnings_growth_percentage": info.get("earningsQuarterlyGrowth", "Unavailable"),
            "next_dividend_date": info.get("dividendDate", "Unavailable"),
            "ex_dividend_date": info.get("exDividendDate", "Unavailable"),
            "currency": info.get("currency", "Unavailable"),
            "country": info.get("country", "Unavailable"),
            "stock_symbol": info.get("symbol", "Unavailable"),
            "historical_dividends": dividends.to_dict() if not dividends.empty else []
        }

        return data

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching information for {ticker_symbol}: {str(e)}")

@app.get("/stock/{ticker_symbol}")
async def get_stock_data(ticker_symbol: str):
    """
    Endpoint para buscar informações detalhadas de uma ação.
    """
    stock_data = fetch_stock_info(ticker_symbol)
    if not stock_data:
        raise HTTPException(status_code=404, detail="Stock information not found.")
    return stock_data
