# Predicción del Tipo de Cambio USD/MXN con Machine Learning 📈

## Descripción del Proyecto

Este proyecto desarrolla un modelo predictivo para analizar y estimar el comportamiento futuro del tipo de cambio USD/MXN utilizando técnicas de Ciencia de Datos, Machine Learning y Deep Learning aplicadas a series temporales financieras.

El objetivo es construir un sistema capaz de procesar información histórica del mercado cambiario, generar variables financieras relevantes y comparar diferentes modelos predictivos para estimar movimientos futuros del tipo de cambio.

El proyecto integra conceptos de:

- Series de tiempo financieras
- Finanzas cuantitativas
- Ingeniería de características
- Machine Learning
- Deep Learning
- Redes neuronales recurrentes


---

# Objetivo

Construir un modelo de predicción del tipo de cambio USD/MXN utilizando datos históricos y técnicas cuantitativas que permitan analizar tendencias y proyectar valores futuros.

El sistema permite seleccionar un horizonte de predicción en días hábiles y estimar el posible comportamiento futuro del tipo de cambio.


---

# Tecnologías utilizadas

- Python
- Yahoo Finance API (yfinance)
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn
- XGBoost
- TensorFlow
- Keras


---

# Obtención de Datos

Los datos son descargados automáticamente desde Yahoo Finance utilizando:

```python
yfinance
```

El activo utilizado corresponde al ticker:

```text
MXN=X
```

La información representa el tipo de cambio:

```text
USD/MXN
```

y contiene:

- Precio histórico del tipo de cambio
- Fechas de cotización
- Serie temporal financiera


---

# Ingeniería de Características

Para mejorar la capacidad predictiva de los modelos se generan nuevas variables financieras a partir de la serie original.


---

# Rendimientos Financieros

Los rendimientos diarios se calculan mediante:

$$
R_t=
\frac{
S_t-S_{t-1}
}
{
S_{t-1}
}
$$

donde:

- $S_t$: tipo de cambio actual
- $S_{t-1}$: tipo de cambio del periodo anterior


---

# Medias Móviles

Se calculan medias móviles para identificar tendencias de corto y mediano plazo:

$$
MA_n=
\frac{1}{n}
\sum_{i=0}^{n-1}
S_{t-i}
$$

Variables utilizadas:

- Media móvil de 7 días
- Media móvil de 30 días
- Media móvil de 90 días


---

# Volatilidad Histórica

La volatilidad mide la variabilidad de los movimientos del tipo de cambio:

$$
\sigma=
\sqrt{
\frac{1}{n}
\sum_{i=1}^{n}
(R_i-\bar R)^2
}
$$


Permite representar el nivel de incertidumbre y riesgo del mercado cambiario.


---

# Variables Rezagadas (Lag Features)

Se incorporan valores históricos del tipo de cambio:

- Lag 1 día
- Lag 7 días
- Lag 30 días


Estas variables permiten que los modelos aprendan patrones temporales del comportamiento pasado.


---

# Modelos Implementados

El proyecto compara diferentes algoritmos predictivos.


---

## Regresión Lineal

Modelo base que aproxima una relación lineal entre las variables financieras y el tipo de cambio futuro.

La estructura general es:

$$
Y=
\beta_0+
\beta_1X_1+
\beta_2X_2+
...
+
\beta_nX_n
$$


---

## Random Forest Regressor

Modelo basado en múltiples árboles de decisión.

Permite capturar relaciones no lineales entre:

- Tendencias
- Volatilidad
- Movimientos históricos


El resultado final se obtiene mediante el promedio de múltiples árboles.


---

## XGBoost Regressor

Modelo basado en Gradient Boosting.

Construye árboles de manera secuencial donde cada nuevo modelo busca corregir los errores del anterior.

Se caracteriza por:

- Alta capacidad predictiva
- Manejo de relaciones complejas
- Regularización para reducir sobreajuste


---

## LSTM (Long Short-Term Memory)

Se implementa una red neuronal recurrente especializada en series temporales.

Las redes LSTM permiten conservar información histórica mediante mecanismos de memoria interna.

Son utilizadas frecuentemente en:

- Series financieras
- Señales temporales
- Predicción secuencial


---

# Evaluación de Modelos

Los modelos son evaluados utilizando diferentes métricas.


---

## MAE (Mean Absolute Error)

Error absoluto promedio:

$$
MAE=
\frac{1}{n}
\sum_{i=1}^{n}
|y_i-\hat y_i|
$$


---

## RMSE (Root Mean Squared Error)

Penaliza errores grandes:

$$
RMSE=
\sqrt{
\frac{1}{n}
\sum_{i=1}^{n}
(y_i-\hat y_i)^2
}
$$


---

## R² Score

Mide qué porcentaje de la variabilidad logra explicar el modelo:

$$
R^2=
1-
\frac{
SS_{res}
}
{
SS_{tot}
}
$$


---

# Selección del Mejor Modelo

Después de entrenar los modelos:

- Regresión Lineal
- Random Forest
- XGBoost

se selecciona automáticamente el modelo con menor RMSE para realizar las predicciones futuras.


---

# Predicción Futura

El sistema permite proyectar el tipo de cambio para un número definido de días hábiles.

El procedimiento consiste en:

1. Predecir el siguiente valor del USD/MXN.
2. Incorporar la predicción como nuevo dato.
3. Recalcular indicadores financieros.
4. Repetir el proceso hasta completar el horizonte definido.


---

# Visualizaciones

El proyecto genera:

- Evolución histórica del USD/MXN
- Comparación entre valores reales y predichos
- Evaluación de modelos
- Proyección futura del tipo de cambio


---

# Estructura del Proyecto

```
04-Prediccion-Tipo-Cambio-USDMXN/

│── USD_MXN_Forecasting_Machine_Learning.ipynb
│── README.md
```


---

# Aplicaciones

Este proyecto tiene aplicaciones en:

- Análisis financiero
- Mercados cambiarios
- Planeación financiera
- Gestión de riesgo cambiario
- Finanzas cuantitativas
- Ciencia de datos aplicada a economía
- Modelado de series temporales


---

# Autor

**Angel Hernández Rivera**

Licenciatura en Matemática Algorítmica  
Escuela Superior de Física y Matemáticas - IPN


Áreas de interés:

- Ciencia de Datos
- Finanzas Cuantitativas
- Machine Learning
- Series Temporales
- Análisis Financiero
- Gestión de Riesgo
