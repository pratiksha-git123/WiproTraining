import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

sns.displot(
    data=tips,
    x='total_bill',
    kde=True,
    color='darkblue'
)
plt.title("Distribution of Total Bill")
plt.show()

sns.jointplot(
    data=tips,
    x='total_bill',
    y='tip',
    kind='reg'
)
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(
    data=tips,
    x='day',
    y='total_bill',
    hue='smoker'
)
plt.title("Total bill across different days")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()