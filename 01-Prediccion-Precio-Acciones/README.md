# Predicción de Precios de Acciones con Machine Learning 📈

## Descripción del Proyecto

Este proyecto desarrolla un sistema de predicción de precios de acciones utilizando técnicas de Ciencia de Datos, Machine Learning y análisis financiero cuantitativo.

El objetivo es analizar información histórica del mercado bursátil obtenida mediante Yahoo Finance, generar indicadores financieros relevantes y comparar distintos modelos predictivos para estimar el comportamiento futuro del precio de una acción.

El proyecto combina conceptos de:

- Series de tiempo financieras
- Ingeniería de características
- Indicadores técnicos
- Aprendizaje automático
- Evaluación de modelos predictivos


---

# Objetivo

Construir un modelo capaz de estimar el precio futuro de cierre de una acción a partir de información histórica y variables financieras generadas mediante análisis cuantitativo.

El sistema permite seleccionar una acción y proyectar su precio para un número determinado de días hábiles del mercado.


---

# Tecnologías utilizadas

- Python
- Pandas
- NumPy
- Yahoo Finance API (yfinance)
- Matplotlib
- Scikit-Learn
- XGBoost
- Machine Learning


---

# Obtención de Datos

Los datos financieros son obtenidos directamente desde Yahoo Finance utilizando la librería:

```python
yfinance
```

La información utilizada incluye:

- Precio de apertura (Open)
- Precio máximo diario (High)
- Precio mínimo diario (Low)
- Precio de cierre (Close)
- Volumen negociado (Volume)


---

# Ingeniería de Características

Para mejorar el aprendizaje de los modelos se construyeron nuevas variables financieras.


## Rendimientos diarios

Se calcula el cambio porcentual diario del precio:

$$
R_t=\frac{P_t-P_{t-1}}{P_{t-1}}
$$


## Medias móviles

Se generan tendencias de corto y mediano plazo:

- Media móvil de 7 días
- Media móvil de 21 días
- Media móvil de 50 días


## Volatilidad histórica

Se estima mediante la desviación estándar móvil de los rendimientos:

$$
\sigma=\sqrt{\frac{1}{n}\sum(R_i-\bar R)^2}
$$


## Variables rezagadas (Lag Features)

Se incorporan precios anteriores:

- Precio del día anterior
- Precio de los últimos días
- Tendencia histórica reciente


## RSI (Relative Strength Index)

Indicador de momentum utilizado para identificar condiciones de sobrecompra o sobreventa del mercado.


## MACD

Indicador basado en medias móviles exponenciales para detectar cambios en la tendencia del precio.


---

# Modelos Implementados

Se comparan diferentes algoritmos de Machine Learning:


## Regresión Lineal

Modelo base utilizado para identificar relaciones lineales entre las variables financieras y el precio futuro.


## Random Forest Regressor

Modelo basado en múltiples árboles de decisión capaz de detectar relaciones no lineales entre los indicadores financieros.


## XGBoost Regressor

Algoritmo avanzado basado en Gradient Boosting que construye modelos secuenciales corrigiendo errores anteriores para mejorar la precisión.


---

# Evaluación de Modelos

Los modelos son evaluados mediante:

## MAE (Mean Absolute Error)

Error absoluto promedio:

$$
MAE=\frac{1}{n}\sum |y_i-\hat{y_i}|
$$


## RMSE (Root Mean Squared Error)

Penaliza errores grandes:

$$
RMSE=\sqrt{\frac{1}{n}\sum(y_i-\hat{y_i})^2}
$$


## R² Score

Mide la capacidad explicativa del modelo:

$$
R^2=1-\frac{SS_{res}}{SS_{tot}}
$$


---

# Predicción Futura

Después del entrenamiento, el modelo permite proyectar el precio de la acción para un número definido de días hábiles.

La predicción se realiza de manera iterativa:

1. Se predice el siguiente precio.
2. Ese nuevo valor se incorpora nuevamente al conjunto de datos.
3. Se recalculan indicadores financieros.
4. Se genera la siguiente predicción.

Este proceso continúa hasta alcanzar el horizonte definido.


---

# Visualizaciones

El proyecto genera:

- Comparación precio real vs precio estimado
- Evaluación de modelos
- Importancia de variables financieras
- Proyección futura del precio


---

# Estructura del Proyecto

```
01-Prediccion-Precio-Acciones/

│── Stock_Price_Forecasting.ipynb
│── README.md
```

---

# Aplicaciones

Este proyecto tiene aplicaciones en:

- Análisis financiero
- Ciencia de datos aplicada a mercados
- Modelado cuantitativo
- Gestión de inversiones
- Investigación de series temporales financieras


---

# Autor

**Angel Hernández Rivera**

Licenciatura en Matemática Algorítmica  
Escuela Superior de Física y Matemáticas - IPN

Intereses:
- Ciencia de Datos
- Finanzas Cuantitativas
- Machine Learning
- Análisis de Riesgo
