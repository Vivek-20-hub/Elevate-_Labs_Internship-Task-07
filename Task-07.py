import sqlite3 as sql
import pandas as pd
import matplotlib as mpl

conn = sql.connect("sales_data.db")

query = "SELECT product_name, SUM(quantity) as total_quantity, SUM(price * quantity) as revenue FROM cleaned_sales_data GROUP BY product_name ORDER BY revenue DESC LIMIT 10;"
df = pd.read_sql_query(query,conn)
print(df)
df.plot(kind="bar",x="product_name",y="revenue")
mpl.pyplot.savefig("sales_chart.png")


query = "SELECT product_name, SUM(quantity) as total_quantity, SUM(profit) as profit FROM cleaned_sales_data GROUP BY product_name ORDER BY profit DESC LIMIT 10;"
df = pd.read_sql_query(query,conn)
print(df)
df.plot(kind="bar",x="product_name",y="profit")
mpl.pyplot.savefig("profit_chart.png")
