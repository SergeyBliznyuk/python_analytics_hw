import pandas as pd
# Lviv amnt corrected
data = {"city": ["Kyiv", "Lviv", "Odesa"], "sales": [1200, 950, 500]}
df = pd.DataFrame(data)

print("Продажі по містах:")
print(df)

average_sales = df["sales"].mean()
print("Середнє значення:", average_sales)
print("Це середній рівень продажів по трьох містах")

# one more merged
# and one more merged

# this is a feature before revert