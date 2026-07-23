import matplotlib.pyplot as plt


gases = ['Nitrogen', 'Oxygen', 'Argon', 'Carbon Dioxide & Others']
percentages = [78.08, 20.95, 0.93, 0.04]


plt.figure(figsize=(6, 6))
plt.pie(
    percentages, 
    labels=gases, 
    autopct='%1.2f%%', 
    startangle=140, 
    explode=[0, 0.05, 0.1, 0.2]
)

plt.title("Composition of Air")
plt.show()