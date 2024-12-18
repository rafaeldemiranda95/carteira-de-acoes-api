# Carteira de Ações - API de Ações
---

## Recursos Principais

- **Integração com yfinance**:
  - Obtenha informações detalhadas de ações, incluindo:
    - Nome completo da empresa.
    - Preço atual.
    - Histórico de dividendos.

- **Documentação Automática**:
  - Documentação interativa com Swagger e Redoc gerada automaticamente.

- **Integração com Laravel**:
  - Envia os dados obtidos para uma rota Laravel via requisições HTTP POST.

---

## Tecnologias Utilizadas

- **Backend**: FastAPI
- **Bibliotecas Python**:
  - `yfinance`: Para acessar dados financeiros.
  - `requests`: Para integração com Laravel.
- **Servidor**: Uvicorn

---

## Pré-requisitos

Antes de iniciar, certifique-se de ter instalado:

- **Python 3.8 ou superior**.
- **pip** para gerenciar pacotes Python.
- Um servidor Laravel configurado para receber as requisições.

