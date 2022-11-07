#chart from Amazon_order.csv file
import pandas as pd
df= pd.read_csv('Amazon_orders.csv')
pd.set_option('display.max_columns', None)
print(df.to_string())

#minimum price of purchases
import pandas as pd
df= pd.read_csv('Amazon_orders.csv')
pd.set_option('display.max_columns', None)
x=df['price'].min()
print(x)

#maximum price of purchases
import pandas as pd
df= pd.read_csv('Amazon_orders.csv')
pd.set_option('display.max_columns', None)
x=df['price'].max()
print(x)

#mean price of purchases
import pandas as pd
df= pd.read_csv('Amazon_orders.csv')
pd.set_option('display.max_columns', None)
x=df['price'].mean()
print(x)

#median price of purchases
import pandas as pd
df= pd.read_csv('Amazon_orders.csv')
pd.set_option('display.max_columns', None)
x=df['price'].median()
print(x)

#standard deviation of purchases
import pandas as pd
df= pd.read_csv('Amazon_orders.csv')
pd.set_option('display.max_columns', None)
x=df['price'].std()
print(x)

#average monthly spending 
import pandas as pd
df= pd.read_csv('Amazon_orders.csv')
y=df.groupby(pd.PeriodIndex(df['order date'], freq='M'))['price'].mean()
print(y)