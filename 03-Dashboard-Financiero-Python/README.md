# Dashboard Financiero Interactivo con Python 📊

## 🚀 Aplicación Web

Puedes probar el dashboard financiero interactivo en el siguiente enlace:

https://proyectos-de-finanzas-cuantitativas-gzxhkkom5zvj9c2vczfpty.streamlit.app/

---

## Descripción del Proyecto

Este proyecto desarrolla un dashboard financiero interactivo utilizando Python y Streamlit para analizar activos financieros mediante datos históricos obtenidos desde Yahoo Finance.

El objetivo es construir una herramienta que permita visualizar el comportamiento de diferentes acciones, evaluar métricas de rendimiento y analizar el riesgo financiero de los activos seleccionados.

El proyecto integra conceptos de:

- Ciencia de datos financiera
- Análisis de series temporales
- Finanzas cuantitativas
- Visualización de datos
- Indicadores de riesgo financiero

---

# Objetivo

Crear una aplicación interactiva capaz de analizar múltiples activos financieros y generar indicadores clave utilizados en análisis financiero e inversión.

El usuario puede seleccionar diferentes acciones, modificar periodos históricos y evaluar métricas financieras automáticamente.

---

# Tecnologías utilizadas

- Python
- Streamlit
- Yahoo Finance API (yfinance)
- Pandas
- NumPy
- Matplotlib

---

# Funcionalidades del Dashboard

El dashboard permite analizar:

- Precios históricos de acciones
- Evolución de activos financieros
- Rendimientos diarios
- Rendimiento acumulado
- Volatilidad móvil
- Drawdown histórico
- Correlación entre activos
- KPIs financieros

---

# Obtención de Datos

Los datos financieros son descargados automáticamente desde Yahoo Finance utilizando la librería:

```python
yfinance
```

Para cada activo seleccionado se obtiene:

- Precio histórico ajustado
- Fechas de cotización
- Series temporales financieras

---

# Rendimientos Financieros

El rendimiento diario se calcula mediante:

$$
R_t=\frac{P_t-P_{t-1}}{P_{t-1}}
$$

donde:

- $P_t$: precio actual del activo
- $P_{t-1}$: precio del periodo anterior

---

# Rendimiento Acumulado

La evolución acumulada del activo se calcula mediante:

$$
R_{acum}=
\prod_{t=1}^{n}(1+R_t)-1
$$

Esta métrica permite analizar cuánto habría aumentado o disminuido una inversión durante un periodo determinado.

---

# Volatilidad

La volatilidad mide la variabilidad de los rendimientos de un activo financiero:

$$
\sigma=
\sqrt{
\frac{1}{n}
\sum_{i=1}^{n}
(R_i-\bar{R})^2
}
$$

La volatilidad anualizada se calcula como:

$$
\sigma_{anual}=\sigma_{diaria}\sqrt{252}
$$

considerando aproximadamente 252 días hábiles bursátiles al año.

---

# Drawdown

El drawdown representa la caída porcentual de un activo respecto a su máximo histórico alcanzado:

$$
DD_t=
\frac{
P_t-\max(P)
}
{
\max(P)
}
$$

Permite evaluar la magnitud de las pérdidas durante periodos de caída del mercado.

---

# Sharpe Ratio

El Sharpe Ratio mide el rendimiento obtenido por unidad de riesgo asumido:

$$
S=\frac{R_p}{\sigma_p}
$$

donde:

- $R_p$: rendimiento esperado del activo
- $\sigma_p$: volatilidad del activo

Un mayor Sharpe Ratio representa una mejor relación entre rendimiento y riesgo.

---

# Correlación entre Activos

La correlación mide qué tan relacionados están los movimientos de dos activos financieros.

Se calcula mediante:

$$
\rho_{xy}=
\frac{
Cov(X,Y)
}
{
\sigma_X\sigma_Y
}
$$

donde:

- $\rho_{xy}$: coeficiente de correlación
- $Cov(X,Y)$: covarianza entre los activos
- $\sigma_X,\sigma_Y$: volatilidades individuales

---

# Indicadores Principales (KPIs)

El sistema calcula automáticamente:

| Indicador | Descripción |
|---|---|
| Rendimiento anual | Rentabilidad anualizada del activo |
| Volatilidad anual | Medida del riesgo histórico |
| Sharpe Ratio | Rendimiento ajustado por riesgo |
| Máximo Drawdown | Mayor caída desde máximos históricos |

---

# Visualizaciones del Dashboard

## Evolución de Precios

Comparación del crecimiento de diferentes activos utilizando precios normalizados.

---

## Rendimiento Acumulado

Visualización del crecimiento porcentual acumulado de una inversión.

---

## Volatilidad Móvil

Análisis del comportamiento del riesgo financiero a través del tiempo.

---

## Drawdown

Identificación de periodos de pérdidas y recuperación del activo.

---

## Matriz de Correlación

Comparación de la relación entre los movimientos de diferentes instrumentos financieros.

---

# Ejecución Local del Proyecto

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar la aplicación:

```bash
streamlit run app.py
```

La aplicación se abrirá localmente mediante Streamlit.

---

# Estructura del Proyecto

```
03-Dashboard-Financiero-Python/

│── app.py
│── requirements.txt
│── README.md
```

---

# Aplicaciones

Este proyecto tiene aplicaciones en áreas como:

- Análisis financiero
- Business Intelligence
- Asset Management
- Planeación financiera
- Evaluación de inversiones
- Ciencia de datos aplicada a mercados financieros
- Análisis cuantitativo

---

# Autor

**Angel Hernández Rivera**

Licenciatura en Matemática Algorítmica  
Escuela Superior de Física y Matemáticas - IPN

Áreas de interés:

- Ciencia de Datos
- Finanzas Cuantitativas
- Machine Learning
- Análisis Financiero
- Gestión de Riesgo
- Modelos Predictivos
