import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
plt.figure(figsize=(8, 5))
sns.regplot(data=tips, x="total_bill", y="tip", scatter_kws={"alpha":0.6}, line_kws={"color":"red"})

plt.title("Relationship Between Total Bill and Tip Amount")
plt.xlabel("Total Bill")
plt.ylabel("Tip")

plt.show()