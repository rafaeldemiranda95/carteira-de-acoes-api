from fastapi import FastAPI, HTTPException
import yfinance as yf

app = FastAPI()

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
        
        # Informações detalhadas
        data = {
            "Nome Completo": info.get("longName", "Não disponível"),
            "Setor": info.get("sector", "Não disponível"),
            "Indústria": info.get("industry", "Não disponível"),
            "Site Oficial": info.get("website", "Não disponível"),
            "Endereço": f"{info.get('address1', 'Não disponível')}, {info.get('city', '')}, {info.get('country', '')}",
            "Telefone": info.get("phone", "Não disponível"),
            "Logo da Empresa": info.get("logo_url", "Não disponível"),
            "Preço Atual": info.get("regularMarketPrice", "Não disponível"),
            "Preço de Abertura": info.get("regularMarketOpen", "Não disponível"),
            "Fechamento Anterior": info.get("regularMarketPreviousClose", "Não disponível"),
            "Volume Negociado": info.get("regularMarketVolume", "Não disponível"),
            "Valor de Mercado": info.get("marketCap", "Não disponível"),
            "P/L Trailing": info.get("trailingPE", "Não disponível"),
            "P/L Forward": info.get("forwardPE", "Não disponível"),
            "Taxa de Dividendos (%)": info.get("dividendYield", "Não disponível"),
            "Beta": info.get("beta", "Não disponível"),
            "Número de Funcionários": info.get("fullTimeEmployees", "Não disponível"),
            "Crescimento Trimestral dos Lucros (%)": info.get("earningsQuarterlyGrowth", "Não disponível"),
            "Próxima Data de Dividendos": info.get("dividendDate", "Não disponível"),
            "Data Ex-Dividendo": info.get("exDividendDate", "Não disponível"),
            "Moeda": info.get("currency", "Não disponível"),
            "País": info.get("country", "Não disponível"),
            "Código da Ação": info.get("symbol", "Não disponível"),
            "Dividendos Históricos": dividends.to_dict() if not dividends.empty else "Sem dividendos registrados"
        }

        return data

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar informações para {ticker_symbol}: {e}")

@app.get("/stock/{ticker_symbol}")
async def get_stock_data(ticker_symbol: str):
    """
    Endpoint para buscar informações detalhadas de uma ação.
    """
    stock_data = fetch_stock_info(ticker_symbol)
    if not stock_data:
        raise HTTPException(status_code=404, detail="Informações da ação não encontradas.")
    return stock_data
