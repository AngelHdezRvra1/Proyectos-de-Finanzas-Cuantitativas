# Dashboard Financiero Interactivo con Python 📊

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

- Precios históricos
- Evolución de activos financieros
- Rendimientos diarios
- Rendimiento acumulado
- Volatilidad
- Drawdown
- Correlación entre activos
- KPIs financieros


---

# Obtención de Datos

Los datos son descargados automáticamente desde Yahoo Finance utilizando:

```python
yfinance
```

Para cada activo se obtiene:

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

- \(P_t\): precio actual del activo
- \(P_{t-1}\): precio del periodo anterior


---

# Rendimiento Acumulado

La evolución acumulada del activo se calcula como:

$$
R_{acum}=\prod_{t=1}^{n}(1+R_t)-1
$$


Permite observar cuánto habría aumentado o disminuido una inversión durante el periodo analizado.


---

# Volatilidad

La volatilidad mide la variabilidad de los rendimientos:

$$
\sigma=
\sqrt{
\frac{1}{n}
\sum_{i=1}^{n}
(R_i-\bar{R})^2
}
$$


La volatilidad anualizada se obtiene mediante:

$$
\sigma_{anual}
=
\sigma_{diaria}\sqrt{252}
$$


considerando aproximadamente 252 días hábiles bursátiles.


---

# Drawdown

El drawdown mide la caída de un activo desde su máximo histórico:

$$
DD_t=
\frac{P_t-\max(P)}
{\max(P)}
$$


Permite analizar pérdidas máximas durante un periodo determinado.


---

# Sharpe Ratio

El dashboard calcula el rendimiento ajustado por riesgo:

$$
S=
\frac{R_p}{\sigma_p}
$$


donde:

- \(R_p\): rendimiento esperado
- \(\sigma_p\): volatilidad del activo


Un valor mayor indica una mejor relación entre rendimiento y riesgo.


---

# Correlación entre Activos

Se calcula la matriz de correlación de rendimientos:

$$
\rho_{xy}
=
\frac{
Cov(X,Y)
}
{
\sigma_X\sigma_Y
}
$$


La correlación permite analizar qué tan relacionados están los movimientos entre diferentes activos.


---

# Indicadores principales (KPIs)

El sistema calcula automáticamente:

| Indicador | Descripción |
|---|---|
| Rendimiento anual | Ganancia esperada anualizada |
| Volatilidad anual | Riesgo del activo |
| Sharpe Ratio | Rendimiento ajustado por riesgo |
| Máximo Drawdown | Mayor caída histórica |


---

# Visualizaciones

La aplicación genera:

## Evolución de precios

Comparación de precios normalizados para distintos activos.


## Rendimiento acumulado

Crecimiento porcentual de una inversión inicial.


## Volatilidad móvil

Cambio del riesgo a través del tiempo.


## Drawdown

Periodos de pérdida respecto a máximos históricos.


## Matriz de correlación

Relación entre activos financieros.


---

# Ejecución del Proyecto

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar aplicación:

```bash
streamlit run app.py
```


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

Este proyecto tiene aplicaciones en:

- Análisis financiero
- Business Intelligence
- Asset Management
- Planeación financiera
- Evaluación de inversiones
- Ciencia de datos aplicada a mercados financieros


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
