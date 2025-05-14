import pandas as pd

# Try different encodings
data=pd.read_csv('sales_data_sample.csv', encoding='latin1')
#print(data)
#print(data.head())
#print(data.isnull().sum())
#df.drop(columns=['ADDRESSLINE2','TERRITORY'],inplace=True)
#df['POSTALCODE'].df.fillna(method='bfill',inplace=True)
#df.fillna(0).isnull().sum()
          
# Convert the ORDERDATE column to datetime
data['ORDERDATE'] = pd.to_datetime(data['ORDERDATE'], errors='coerce')

data['Sales_Amount']=data['QUANTITYORDERED']*data['PRICEEACH']
print(data['Sales_Amount'])

data['Month'] = data['ORDERDATE'].dt.to_period('M')
print(data['Month'])

monthly_sales = data.groupby('Month')['Sales_Amount'].sum()

monthly_sales.plot(kind='bar', title='Monthly Sales', ylabel='Sales Amount', xlabel='Month', color='skyblue')
#plt.show()

top_products = data.groupby('PRODUCTCODE')['QUANTITYORDERED'].sum().nlargest(5)
print(top_products)

top_products.plot(kind='bar', title='Top 5 Best-Selling Products', ylabel='Quantity Sold', xlabel='Product', color='orange')
#plt.show()

avg_sale_amount = data['SALES'].mean()
print(f"The average sale amount per transaction is: ${avg_sale_amount:.2f}")

data['Month_Name'] = data['ORDERDATE'].dt.strftime('%B')
print(data['Month_Name'])

monthly_sales_trends = data.groupby('Month_Name')['Sales_Amount'].sum()
print(monthly_sales_trends)
monthly_sales_trends.plot(kind='line', title='Sales Trends by Month', ylabel='Sales Amount', xlabel='Month', color='green')
print(data)