# 📊 Superstore Sales & Profitability Analysis

Este repositorio contiene un análisis exploratorio de datos (EDA) y procesamiento ETL sobre el dataset **Sample - Superstore**. El objetivo principal es identificar patrones de ventas, analizar la rentabilidad por categoría, región y política de descuentos, y evaluar los tiempos de envío.

---

## 🛠️ Tecnologías y Librerías

- **Lenguaje:** Python 3.x
- **Librerías:** 
  - `pandas` (Limpieza, transformación y análisis de datos)

---

## 📁 Estructura del Proyecto

```text
superStore/
├── .gitignore             # Exclusión de entornos, settings y archivos pesados
├── analisis.py            # Script principal de ETL y Análisis Exploratorio (EDA)
└── hallasgos.md           # Reporte detallado con conclusiones y recomendaciones
```

---

## ⚙️ Proceso de ETL y Limpieza de Datos

El script `analisis.py` realiza automáticamente las siguientes etapas:

1. **Inspección de Calidad:** Verificación de dimensiones, nulos y duplicados.
2. **Transformación de Fechas:** Conversión de `Order Date` y `Ship Date` a formato `datetime` y validación de inconsistencias (envíos antes de la orden).
3. **Ingeniería de Características (Feature Engineering):**
   - `Dias_envio`: Tiempo transcurrido entre la orden y el envío.
   - `Margen`: Porcentaje de ganancia (`Profit / Sales`).
   - `Es_perdida`: Flag para transacciones con margen negativo.
   - Aperturas temporales: Año, Mes, Nombre de Mes, Trimestre y Periodo (Año-Mes).
   - Categorización de descuentos en rangos (`Sin descuento`, `0-10%`, `10-20%`, `20-30%`, `30%+`).
4. **Exportación:** Generación de `Superstore_clean.csv` optimizado para análisis posterior o consumo en herramientas de BI.

---

## 💡 Preguntas de Negocio Respondidas

El análisis aborda directamente las siguientes interrogantes clave:

1. **Desempeño Global:** Ventas totales, ganancias, margen global y ticket promedio.
2. **Evolución Temporal:** Crecimiento anual y tendencia de ventas/ganancias por mes.
3. **Rentabilidad por Producto:** Identificación de categorías y subcategorías de alto/bajo rendimiento.
4. **Análisis Geográfico:** Desempeño y margen por regiones.
5. **Impacto de Descuentos:** Relación entre el nivel de descuento aplicado y el margen neto.
6. **Logística:** Tiempos promedio de despacho según el método de envío (`Ship Mode`).

---

## 📄 Conclusiones y Reporte

Para consultar los hallazgos clave, insights de negocio y recomendaciones estratégicas detalladas, revisa el archivo [`hallasgos.md`](./hallasgos.md).
