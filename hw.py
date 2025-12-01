import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

tips = sb.load_dataset("tips")
print(tips.head())

print(tips[["size", "tip", "total_bill"]].describe())

plt.figure()
sb.histplot(tips["total_bill"], kde=True)
plt.title("Total Bill Distribution")
plt.show()

plt.figure()
sb.scatterplot(data=tips, x="total_bill", y="tip", hue="time")
plt.title("Total Bill vs Tip (Time as Hue)")
plt.show()

sb.pairplot(tips, hue="sex")
plt.show()