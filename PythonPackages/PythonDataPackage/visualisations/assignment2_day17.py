import matplotlib.pyplot as plt

cities = ['Chennai', 'Mumbai', 'Delhi', 'Banglore', 'Hyderabad']
sales_values = [450, 600, 520, 780, 410]

categories = ['Electronics', 'Fashion', 'Groceries', 'Home Decor']
market_share = [35, 25, 30, 10]

fig, axes = plt.subplots(1,2, figsize=(12, 5))
axes[0].bar(cities, sales_values, color='teal')
axes[0].set_title("City-wise Sales")
axes[0].set_xlabel("Cities")
axes[0].set_ylabel("Sales Values")
axes[0].grid(axis='y')

explode = (0.1, 0, 0, 0)
axes[1].pie(
    market_share,
    labels=categories,
    autopct='%1.1f%%',
    explode=explode
)
axes[1].set_title("Market share by Category")
fig.suptitle("Regional Sales & Category Analysis", fontsize=16)
plt.tight_layout()
plt.show()