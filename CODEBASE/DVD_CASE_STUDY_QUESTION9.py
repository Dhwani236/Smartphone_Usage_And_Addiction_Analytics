import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/dhwan/OneDrive/Documents/college/SEM 4/DVD/Smartphone_Usage_And_Addiction_Analysis_7500_Rows-2.csv")

counts = df["addiction_level"].value_counts()
plt.pie(x=counts.values,labels=["Mild","Moderate","Severe"], autopct='%.0f%%', shadow=True, startangle=90, colors=sns.color_palette('pastel'))  

plt.title("Addiction Level Proportions")

plt.show()