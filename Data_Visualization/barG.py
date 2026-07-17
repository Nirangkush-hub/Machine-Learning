"""This perticular program is to demonstrate how we can visualize data in a bar graph diagram.
We are using a built-in dataset(csv file) called "tips.csv" to visualize the data in it
"""
import matplotlib.pyplot as plt
import seaborn as sns


tips = sns.load_dataset("tips")

plt.figure(figsize=(8, 5))
sns.barplot(data=tips, x="day", y="total_bill", hue="sex")


# Customize with Matplotlib
plt.title("Average Total Bill by Day and Gender")

plt.xlabel("Day of the Week")
plt.ylabel("Average Bill")

plt.show()