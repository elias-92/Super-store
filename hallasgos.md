# Análisis de Ventas — Superstore (2014-2017)

## Contexto del negocio

Análisis exploratorio de 4 años de ventas de una cadena retail con operación
en 4 regiones de Estados Unidos. El objetivo fue identificar oportunidades
de mejora en rentabilidad y detectar las causas del bajo margen global.

**Alcance del análisis:**

- Periodo: enero 2014 — diciembre 2017
- Filas analizadas: 9,994 líneas de pedido
- Pedidos únicos: 5,009
- Regiones: West, East, Central, South
- Categorías: Furniture, Office Supplies, Technology

---

## KPIs principales

| Métrica                | Valor         |
| ---------------------- | ------------- |
| Ventas totales         | $2,297,200.86 |
| Ganancia total         | $286,397.02   |
| Margen global          | 12.47%        |
| Ticket promedio        | $229.86       |
| Pedidos únicos         | 5,009         |
| Días de envío promedio | 3.96          |

**Observación:** el margen del 12.47% es bajo para retail (el estándar
suele estar entre 20% y 40%). Esto indica un problema estructural de
pricing o mix de producto.

---

## Hallazgo 1 — Crecimiento sostenido con 2015 en rojo

| Año  | Ventas | Crecimiento | Ganancia | Margen |
| ---- | ------ | ----------- | -------- | ------ |
| 2014 | $484K  | —           | $49.5K   | 10.2%  |
| 2015 | $471K  | -2.8%       | $61.6K   | 13.1%  |
| 2016 | $609K  | +29.5%      | $81.8K   | 13.4%  |
| 2017 | $733K  | +20.4%      | $93.4K   | 12.7%  |

**Interpretación:** el negocio crece a doble dígito en 2016-2017, y la
ganancia crece más rápido que las ventas (buena eficiencia). Sin embargo,
2015 tuvo una caída del -2.8% en ventas que merece investigación
adicional.

**Acción sugerida:** revisar qué pasó en 2015 (¿estacionalidad, competencia,
cambio de estrategia comercial?).

---

## Hallazgo 2 — Furniture vende mucho pero gana poco

| Categoría       | Ventas | Ganancia | Margen |
| --------------- | ------ | -------- | ------ |
| Technology      | $836K  | $145K    | 16%    |
| Furniture       | $742K  | $18K     | 4%     |
| Office Supplies | $719K  | $122K    | 14%    |

**Interpretación:** Furniture factura casi lo mismo que Technology pero
genera 8 veces menos ganancia. No es un problema de volumen, es un
problema de márgenes.

**Acción sugerida:** revisar pricing y costos de Furniture, o revisar
si vale la pena seguir compitiendo en esa categoría con el modelo actual.

---

## Hallazgo 3 — Tres subcategorías pierden dinero

| Subcategoría | Ventas | Ganancia | Margen |
| ------------ | ------ | -------- | ------ |
| Tables       | $207K  | -$17,725 | -9%    |
| Bookcases    | $115K  | -$3,473  | -3%    |
| Supplies     | $47K   | -$1,189  | -3%    |

Juntas venden $369K y pierden $22K.

**Top subcategorías rentables (para compensar):**

| Subcategoría | Margen |
| ------------ | ------ |
| Labels       | 43%    |
| Paper        | 43%    |
| Envelopes    | 42%    |
| Copiers      | 32%    |

**Interpretación:** el negocio subsidia las subcategorías perdedoras con
las rentables. Copiers es la joya oculta: $149K en ventas con 32% de margen.

**Acción sugerida:**

- Revisar precios de Tables y Bookcases (probablemente están por debajo de costo)
- Impulsar Copiers, Labels, Paper y Envelopes en campañas
- Evaluar descontinuar Supplies si no aporta estratégicamente

---

## Hallazgo 4 — Central es la región problema

| Región  | Ventas | Ganancia | Margen |
| ------- | ------ | -------- | ------ |
| West    | $725K  | $108K    | 22%    |
| East    | $679K  | $92K     | 17%    |
| South   | $392K  | $47K     | 16%    |
| Central | $501K  | $40K     | -10%   |

**Interpretación:** Central vende más que South pero gana menos, y tiene
margen NEGATIVO. El problema es estructural, no de volumen.

**Hipótesis:** exceso de descuentos, mala mezcla de producto (mucho
Furniture) o costos logísticos elevados.

**Acción sugerida:** auditar la estrategia comercial de Central, revisar
descuentos aplicados y mezcla de producto vendido.

---

## Hallazgo 5 — El descuento destruye la ganancia (HALLAZGO PRINCIPAL)

| Rango de descuento | Ventas  | Ganancia | Margen |
| ------------------ | ------- | -------- | ------ |
| Sin descuento      | $1,088K | $321K    | 34%    |
| 0-10%              | $54K    | $9K      | 16%    |
| 10-20%             | $792K   | $92K     | 17%    |
| 20-30%             | $103K   | -$10K    | -12%   |
| 30%+               | $260K   | -$125K   | -91%   |

**Interpretación:** a partir del 20% de descuento, las ventas se vuelven
no rentables. Los pedidos con descuento superior al 30% pierden 91
centavos por cada dólar vendido.

**Impacto cuantificado:**

- Los descuentos >20% generaron $363K en ventas pero **-$135K en ganancia**
- Eliminar esos descuentos recuperaría $135K de margen

**Acción sugerida:**

- Limitar descuentos al 20% máximo
- Exigir aprobación gerencial para descuentos superiores
- Analizar caso por caso los 888 pedidos con +30% de descuento (¿son clientes estratégicos o fuga de margen?)

---

## Hallazgo 6 — Operación logística sin problemas

| Modo de envío  | Días promedio |
| -------------- | ------------- |
| Same Day       | 0.04          |
| First Class    | 2.18          |
| Second Class   | 3.24          |
| Standard Class | 5.01          |

**Interpretación:** los tiempos de envío son coherentes con el modo
contratado. No hay señales de ineficiencia operativa.

---

## Conclusiones y recomendaciones

### Problema central

El margen global del 12.47% es bajo para retail. Las causas son
identificables y cuantificables.

### Recomendaciones priorizadas

1. **Urgente — Política de descuentos:** limitar al 20% máximo.
   Impacto estimado: +$135K de ganancia anual.

2. **Alta prioridad — Subcategorías perdedoras:** revisar pricing de
   Tables, Bookcases y Supplies. Impacto estimado: +$22K.

3. **Alta prioridad — Región Central:** auditar estrategia comercial.
   Si Central alcanzara el margen de South (16%), generaría $80K
   adicionales.

4. **Media prioridad — Impulsar productos rentables:** Copiers, Labels,
   Paper, Envelopes como foco comercial.

5. **Investigación — Caída 2015:** entender la causa para prevenir
   futuras caídas.

### Impacto potencial total

Si se ejecutan las recomendaciones 1, 2 y 3:
**+$237K de ganancia anual** (83% de incremento sobre el actual $286K).

---

## Metodología

- **Herramientas:** Python (pandas, numpy) para limpieza y análisis;
  [Power BI] para visualización
- **Limpieza:** conversión de fechas, creación de features temporales,
  cálculo de margen, flag de pérdida
- **Supuestos:** no se eliminaron outliers de ventas ni profit porque
  representan comportamiento real del negocio
- **Limitaciones:** no se cuenta con datos de costos desagregados ni
  información de competencia

---

## Próximos pasos

- Análisis de cohortes de clientes
- Análisis de canasta de productos (market basket)
- Modelo predictivo de propensión a descuento
- Segmentación RFM de clientes
