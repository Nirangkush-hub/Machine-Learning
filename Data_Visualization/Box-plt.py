import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
plt.figure(figsize=(8, 5))
sns.boxplot(data=tips, x="time", y="total_bill", palette="Set2")

plt.title("Distribution of Total Bills: Lunch vs. Dinner")
plt.xlabel("Time of Day")
plt.ylabel("Total Bill")
plt.savefig("boxplot.png")
plt.show()