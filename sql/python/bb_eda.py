
# BigBasket EDA in Python (VS Code)


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine


# 1. Load Data from MySQL


# Use URL-encoded password (Esha@2004 → Esha%402004)
engine = create_engine("mysql+pymysql://root:password@localhost/ecommerce_inventory")


query = "SELECT * FROM `bigbasket products_new`"
df = pd.read_sql(query, engine)

print("Dataset Loaded Successfully")
print(df.head())


# 2. Basic Structure + Info


print("\nDATASET INFO:")
print(df.info())

print("\nNULL VALUES:")
print(df.isnull().sum())

print("\nDESCRIPTIVE STATS:")
print(df.describe(include='all'))


# 3. Category Analysis


print("\nCATEGORY DISTRIBUTION:")
print(df['category'].value_counts())

plt.figure(figsize=(10,5))
sns.countplot(data=df, y='category', order=df['category'].value_counts().index)
plt.title("Category Distribution")
plt.tight_layout()
plt.show()


# 4. Sub-category Analysis


print("\nSUB-CATEGORY DISTRIBUTION:")
print(df['sub_category'].value_counts())

plt.figure(figsize=(10,6))
df['sub_category'].value_counts().head(15).plot(kind='bar')
plt.title("Top Sub-categories")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 5. Price Bucket Distribution


print("\nPRICE BUCKET DISTRIBUTION:")
print(df['price_bucket'].value_counts())

df['price_bucket'].value_counts().plot(kind='bar', figsize=(6,4))
plt.title("Price Bucket Distribution")
plt.xlabel("Bucket")
plt.ylabel("Count")
plt.tight_layout()
plt.show()


# 6. Demand Score Distribution


print("\nDEMAND SCORE DISTRIBUTION:")
print(df['demand_score'].value_counts())

df['demand_score'].value_counts().plot(kind='pie', autopct='%1.1f%%', figsize=(6,6))
plt.title("Demand Score Distribution")
plt.ylabel("")
plt.show()


# 7. Category vs Price Bucket (Heatmap)


cross1 = pd.crosstab(df['category'], df['price_bucket'])
print("\nCATEGORY vs PRICE BUCKET:\n", cross1)

plt.figure(figsize=(10,5))
sns.heatmap(cross1, annot=True, cmap='Blues')
plt.title("Category vs Price Bucket Heatmap")
plt.tight_layout()
plt.show()


# 8. Category vs Demand Score (Heatmap)


cross2 = pd.crosstab(df['category'], df['demand_score'])
print("\nCATEGORY vs DEMAND SCORE:\n", cross2)

plt.figure(figsize=(10,5))
sns.heatmap(cross2, annot=True, cmap='Greens')
plt.title("Category vs Demand Score Heatmap")
plt.tight_layout()
plt.show()


# 9. Rating Distribution


plt.figure(figsize=(8,4))
sns.histplot(df['rating'], kde=True)
plt.title("Rating Distribution")
plt.tight_layout()
plt.show()


# 10. Correlation Heatmap (Numerical)


plt.figure(figsize=(6,4))
sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

print("\nEDA Completed Successfully!")
