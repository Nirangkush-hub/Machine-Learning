import matplotlib.pyplot as plt
import seaborn as sns

planets = sns.load_dataset("planets")

yearly_discoveries = (
    planets.groupby("year")["number"].sum().reset_index()
)

plt.figure(figsize=(9, 5))

sns.lineplot(data=yearly_discoveries,x="year",y="number",marker="o",linestyle="-",color="teal")

plt.title("Total Exoplanets Discovered Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Planets Discovered")
plt.savefig("Linegraph")
plt.show()