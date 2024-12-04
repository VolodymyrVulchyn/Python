import pandas as pd
import requests

# Отримання даних з API
response = requests.get('http://localhost:8000/api/report/')
data = response.json()

# Перетворення в DataFrame
df_avg_price = pd.DataFrame(data['avg_price_by_category'])
df_sales_by_month = pd.DataFrame(data['sold_items_by_month'])

# Обчислення статистичних показників
print(df_avg_price.describe())
print(df_sales_by_month.describe())