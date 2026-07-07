# ==========================================
# PROYECTO 3: Dashboard Financiero en Python
# Streamlit + Yahoo Finance
# ==========================================

import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from datetime import datetime

st.set_page_config(
    page_title="Dashboard Financiero",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard Financiero con Python")
st.write(
    "Análisis de precios históricos, rendimientos, volatilidad, drawdown, "
    "correlaciones y KPIs financieros usando datos de Yahoo Finance."
)

# ==========================
# Sidebar
# ==========================

st.sidebar.header("Parámetros del análisis")

tickers_input = st.sidebar.text_input(
    "Tickers separados por coma",
    value="AAPL, MSFT, NVDA, GOOGL, AMZN"
)

fecha_inicio = st.sidebar.date_input(
    "Fecha de inicio",
    value=pd.to_datetime("2018-01-01")
)

fecha_fin = st.sidebar.date_input(
    "Fecha de fin",
    value=pd.to_datetime(datetime.today().strftime("%Y-%m-%d"))
)

ventana_volatilidad = st.sidebar.slider(
    "Ventana de volatilidad móvil",
    min_value=7,
    max_value=90,
    value=21
)

tickers = [ticker.strip().upper() for ticker in tickers_input.split(",")]

# ==========================
# Descargar datos
# ==========================

@st.cache_data
def descargar_datos(tickers, fecha_inicio, fecha_fin):
    datos = yf.download(
        tickers,
        start=fecha_inicio,
        end=fecha_fin,
        auto_adjust=True
    )

    if len(tickers) == 1:
        precios = datos[["Close"]].copy()
        precios.columns = tickers
    else:
        precios = datos["Close"].copy()

    return precios.dropna()

try:
    precios = descargar_datos(tickers, fecha_inicio, fecha_fin)

    if precios.empty:
        st.error("No se encontraron datos. Revisa los tickers o las fechas.")
        st.stop()

except Exception as e:
    st.error("Ocurrió un error al descargar los datos.")
    st.write(e)
    st.stop()

# ==========================
# Cálculos financieros
# ==========================

rendimientos = precios.pct_change().dropna()
rendimiento_acumulado = (1 + rendimientos).cumprod() - 1
volatilidad_movil = rendimientos.rolling(window=ventana_volatilidad).std() * np.sqrt(252)

precios_normalizados = precios / precios.iloc[0]

max_acumulado = precios.cummax()
drawdown = (precios - max_acumulado) / max_acumulado

rendimiento_anual = rendimientos.mean() * 252
volatilidad_anual = rendimientos.std() * np.sqrt(252)
sharpe_ratio = rendimiento_anual / volatilidad_anual
max_drawdown = drawdown.min()

kpis = pd.DataFrame({
    "Rendimiento Anual": rendimiento_anual,
    "Volatilidad Anual": volatilidad_anual,
    "Sharpe Ratio": sharpe_ratio,
    "Máximo Drawdown": max_drawdown
})

# ==========================
# KPIs principales
# ==========================

st.subheader("Indicadores principales")

cols = st.columns(len(tickers))

for i, ticker in enumerate(tickers):
    with cols[i]:
        st.metric(
            label=ticker,
            value=f"{rendimiento_anual[ticker]:.2%}",
            delta=f"Volatilidad: {volatilidad_anual[ticker]:.2%}"
        )

st.dataframe(kpis.style.format({
    "Rendimiento Anual": "{:.2%}",
    "Volatilidad Anual": "{:.2%}",
    "Sharpe Ratio": "{:.2f}",
    "Máximo Drawdown": "{:.2%}"
}))

# ==========================
# Gráfica de precios
# ==========================

st.subheader("Precios históricos normalizados")

fig1, ax1 = plt.subplots(figsize=(12, 5))
for ticker in tickers:
    ax1.plot(precios_normalizados.index, precios_normalizados[ticker], label=ticker)

ax1.set_title("Evolución de precios normalizados")
ax1.set_xlabel("Fecha")
ax1.set_ylabel("Precio normalizado")
ax1.legend()
ax1.grid(True)

st.pyplot(fig1)

# ==========================
# Rendimiento acumulado
# ==========================

st.subheader("Rendimiento acumulado")

fig2, ax2 = plt.subplots(figsize=(12, 5))
for ticker in tickers:
    ax2.plot(rendimiento_acumulado.index, rendimiento_acumulado[ticker], label=ticker)

ax2.set_title("Rendimiento acumulado")
ax2.set_xlabel("Fecha")
ax2.set_ylabel("Rendimiento acumulado")
ax2.legend()
ax2.grid(True)

st.pyplot(fig2)

# ==========================
# Volatilidad móvil
# ==========================

st.subheader("Volatilidad móvil anualizada")

fig3, ax3 = plt.subplots(figsize=(12, 5))
for ticker in tickers:
    ax3.plot(volatilidad_movil.index, volatilidad_movil[ticker], label=ticker)

ax3.set_title(f"Volatilidad móvil anualizada - Ventana {ventana_volatilidad} días")
ax3.set_xlabel("Fecha")
ax3.set_ylabel("Volatilidad")
ax3.legend()
ax3.grid(True)

st.pyplot(fig3)

# ==========================
# Drawdown
# ==========================

st.subheader("Drawdown")

fig4, ax4 = plt.subplots(figsize=(12, 5))
for ticker in tickers:
    ax4.plot(drawdown.index, drawdown[ticker], label=ticker)

ax4.set_title("Caídas desde máximos históricos")
ax4.set_xlabel("Fecha")
ax4.set_ylabel("Drawdown")
ax4.legend()
ax4.grid(True)

st.pyplot(fig4)

# ==========================
# Matriz de correlación
# ==========================

st.subheader("Matriz de correlación")

correlacion = rendimientos.corr()

fig5, ax5 = plt.subplots(figsize=(8, 6))
im = ax5.imshow(correlacion, interpolation="nearest")
fig5.colorbar(im)

ax5.set_xticks(range(len(correlacion.columns)))
ax5.set_yticks(range(len(correlacion.columns)))
ax5.set_xticklabels(correlacion.columns, rotation=45)
ax5.set_yticklabels(correlacion.columns)

ax5.set_title("Correlación entre rendimientos diarios")

for i in range(len(correlacion.columns)):
    for j in range(len(correlacion.columns)):
        ax5.text(
            j,
            i,
            f"{correlacion.iloc[i, j]:.2f}",
            ha="center",
            va="center"
        )

st.pyplot(fig5)

# ==========================
# Datos descargados
# ==========================

st.subheader("Datos históricos descargados")
st.dataframe(precios.tail(20))

st.download_button(
    label="Descargar precios en CSV",
    data=precios.to_csv().encode("utf-8"),
    file_name="precios_historicos.csv",
    mime="text/csv"
)
