import pandas as pd
df = pd.read_csv('Sample - Superstore.csv', encoding='latin1')
# 1. Dimensiones
print(f"Filas: {df.shape[0]}, Columnas: {df.shape[1]}")

# 2. Primeras filas
df.head()

# 3. Tipos de datos y nulos
df.info()

# # 4. Nulos explícitos
print("Nulos por columna:")
print(df.isnull().sum())

# # 5. Duplicados
print(f"Duplicados: {df.duplicated().sum()}")

# 6. Estadísticas básicas
print("describe():")
print(df.describe())

# 7. Columnas categóricas: valores únicos
for col in df.select_dtypes(include='object').columns:
    print(f"\n{col}: {df[col].nunique()} únicos")
    print(df[col].unique()[:10])

# 8. Conversión de fechas
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')

# # 9. Verificación de fechas
print(df[['Order Date', 'Ship Date']].isnull().sum())
print(df.dtypes)

# # 10. Ship date debe ser mayor o igual a Order date
errores_fechas = df[df['Ship Date'] < df['Order Date']]
print(f"Errores de fechas: {len(errores_fechas)}")

# # 11. Cuantas filas tienen perdidas
perdidas = df[df['Profit'] < 0]
print(f"Filas con pérdidas: {len(perdidas)} ({len(perdidas)/len(df)*100:.2f}%)")
print(perdidas[['Category', 'Sub-Category', 'Discount', 'Sales', 'Profit']].head())

#12. Revisar el rango temporal
print(f"Rango temporal: {df['Order Date'].min()} a {df['Order Date'].max()}")


#13. Tiempo de envio
df['Dias_envio'] = (df['Ship Date'] - df['Order Date']).dt.days

#14. Dimensiones temporales
df['Anio'] = df['Order Date'].dt.year
df['Mes'] = df['Order Date'].dt.month
df['Nombre_mes'] = df['Order Date'].dt.strftime('%B')
df['Trimestre'] = df['Order Date'].dt.quarter
df['Anio_mes'] = df['Order Date'].dt.to_period('M').astype(str)

#15 Margen
df['Margen'] = df['Profit'] / df['Sales']

#16. Flag de perdidas
df['Es_perdida'] = df['Profit'] < 0

#17. Eliminar columnas innecesarias
df = df.drop(columns=['Row ID', 'Postal Code'])

#18. Guardar el dataframe limpio
df.to_csv('Superstore_clean.csv', index=False, encoding='latin1')

#----------Desde aca lee el csv limpio que se genero y realiza el analisis----------------
df = pd.read_csv('Superstore_clean.csv', encoding='latin1')

# Pregunta 1: ¿Cuánto vendemos y cuánto ganamos en total?
print(f"Ventas totales: {df['Sales'].sum():,.2f}")
print(f"Ganancias totales: {df['Profit'].sum():,.2f}")
print(f"Margen total: {df['Profit'].sum() / df['Sales'].sum() * 100:.2f}%")
print(f"Ticket promedio: {df['Sales'].mean():,.2f}")
print(f"Pedidos unicos: {df['Order ID'].nunique()}")

# Pregunta 2: ¿Cómo evolucionan las ventas por año y mes?

ventas_anio = df.groupby('Anio').agg(Ventas=('Sales', 'sum'), Ganancias=('Profit', 'sum'), Pedidos=('Order ID', 'nunique')).round(2).reset_index()
print("\nVentas por año:")
print(ventas_anio)

# Pregunta 3: ¿Qué categorías y subcategorías son rentables?

cat = df.groupby('Category').agg(Ventas=('Sales', 'sum'), Ganancias=('Profit', 'sum'), Margen=('Margen', 'mean')).round(2).reset_index()
print("\nRentabilidad por categoría:")
print(cat)
subcat = df.groupby('Sub-Category').agg(Ventas=('Sales', 'sum'), Ganancias=('Profit', 'sum'), Margen=('Margen', 'mean')).round(2).reset_index()
print("\nRentabilidad por subcategoría:")
print(subcat)

# Pregunta 4: ¿Qué regiones son más rentables?

region = df.groupby('Region').agg(Ventas=('Sales', 'sum'), Ganancias=('Profit', 'sum'), Margen=('Margen', 'mean')).round(2).sort_values(by='Ventas', ascending=False).reset_index()
print("\nRentabilidad por región:")
print(region)

# Pregunta 5: ¿El descuento mata la ganancia?

df['Rango de descuento'] = pd.cut(df['Discount'], bins=[-0.01, 0, 0.1, 0.2, 0.3, 1], labels=['Sin descuento', '0-10%', '10-20%', '20-30%', '30%+'])
descuento = df.groupby('Rango de descuento', observed=True).agg(Ventas=('Sales', 'sum'), Ganancias=('Profit', 'sum'), Margen=('Margen', 'mean'), Pedidos=('Order ID', 'nunique')).round(2).reset_index()
print("\nRentabilidad por rango de descuento:")
print(descuento)

# Pregunta 6: ¿Los envíos tardan mucho?

print(df['Dias_envio'].describe())
print("\nPor modo de envío:")
print(df.groupby('Ship Mode')['Dias_envio'].mean().round(2).sort_values().reset_index())