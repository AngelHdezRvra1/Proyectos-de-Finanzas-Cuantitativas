# Optimización de Portafolios con Teoría Moderna de Markowitz 📊

## Descripción del Proyecto

Este proyecto implementa un modelo de optimización de portafolios de inversión utilizando Python, análisis cuantitativo y la Teoría Moderna de Portafolios propuesta por Harry Markowitz.

El objetivo es encontrar una asignación eficiente de activos financieros que permita maximizar el rendimiento esperado considerando el nivel de riesgo asumido.

El proyecto combina conceptos de:

- Finanzas cuantitativas
- Estadística aplicada
- Optimización matemática
- Simulación Monte Carlo
- Análisis de riesgo financiero


---

# Objetivo

Construir un sistema capaz de analizar diferentes combinaciones de activos financieros y encontrar el portafolio óptimo mediante la maximización del Sharpe Ratio.

El modelo permite evaluar la relación riesgo-rendimiento y visualizar la frontera eficiente de inversión.


---

# Tecnologías utilizadas

- Python
- Pandas
- NumPy
- Yahoo Finance API (yfinance)
- Matplotlib
- Estadística Financiera
- Optimización Cuantitativa


---

# Obtención de Datos

Los precios históricos de los activos son obtenidos utilizando Yahoo Finance.

Para cada activo se analiza:

- Precio histórico ajustado
- Rendimientos diarios
- Volatilidad
- Relación entre activos


---

# Rendimientos Financieros

Los rendimientos diarios se calculan mediante:

$$
R_t=\frac{P_t-P_{t-1}}{P_{t-1}}
$$

donde:

- \(P_t\): precio actual
- \(P_{t-1}\): precio del periodo anterior


---

# Rendimiento Esperado del Portafolio

El rendimiento esperado se obtiene mediante:

$$
E(R_p)=w^T\mu
$$


donde:

- \(w\): vector de pesos del portafolio
- \(\mu\): vector de rendimientos esperados


---

# Riesgo del Portafolio

La volatilidad del portafolio se calcula usando la matriz de covarianza:

$$
\sigma_p=\sqrt{w^T\Sigma w}
$$


donde:

- \(\Sigma\): matriz de covarianza de los activos


---

# Simulación Monte Carlo

Se generan miles de combinaciones aleatorias de pesos del portafolio.

Cada simulación calcula:

- Rendimiento esperado
- Riesgo
- Sharpe Ratio


El objetivo es explorar diferentes combinaciones posibles de inversión.


---

# Optimización mediante Sharpe Ratio

El Sharpe Ratio mide la rentabilidad obtenida por unidad de riesgo:

$$
S=\frac{R_p-r_f}{\sigma_p}
$$


donde:

- \(R_p\): rendimiento del portafolio
- \(r_f\): tasa libre de riesgo
- \(\sigma_p\): volatilidad


El portafolio óptimo se obtiene resolviendo:

$$
\max S
$$


---

# Resultados obtenidos

El modelo permite identificar:

- Portafolio con máximo Sharpe Ratio
- Portafolio con menor volatilidad
- Pesos óptimos por activo
- Riesgo anual esperado
- Rendimiento anual esperado


---

# Visualizaciones

El proyecto genera:

- Evolución histórica de activos
- Matriz de correlación
- Frontera eficiente de Markowitz
- Distribución óptima del portafolio


---

# Estructura del Proyecto

```
02-Optimizacion-Portafolios-Markowitz/

│── Portfolio_Optimization_Markowitz.ipynb
│── README.md
```


---

# Aplicaciones

Este proyecto tiene aplicaciones en:

- Gestión de inversiones
- Asset Management
- Planeación financiera
- Administración de riesgos
- Finanzas cuantitativas
- Análisis financiero


---

# Autor

**Angel Hernández Rivera**

Licenciatura en Matemática Algorítmica  
Escuela Superior de Física y Matemáticas - IPN

Áreas de interés:

- Ciencia de Datos
- Finanzas Cuantitativas
- Machine Learning
- Modelos Predictivos
- Gestión de Riesgo
