import pandas as pd

# create a dataframe from a dictonary 

data = {
    "Product":["Laptop","Phone","Tablet","Headphones"],
    "Price":[1200,800,300,150],
    "Quantity":[5,10,8,15]
}

df  = pd.DataFrame(data)

# Display the DataFrame

print("DataFrame:")
print(df)

#calculate total sales for each product 

df["Total Sales"]= df["Price"] * df["Quantity"]

print("\nDataframe with Total sales")

print(df)

#get summary statistics 

print("\n SUmmary Statistics ")
print(df.describe())

#filter products with sales greater than 3000

high_sales = df[df["Total Sales"]>3000]
print("\n Products with the high sales ")
print(high_sales)


