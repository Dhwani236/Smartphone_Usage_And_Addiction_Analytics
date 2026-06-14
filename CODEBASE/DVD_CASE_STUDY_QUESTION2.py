import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/dhwan/OneDrive/Documents/college/SEM 4/DVD/Smartphone_Usage_And_Addiction_Analysis_7500_Rows-2.csv")

def categorize_age(age):
    if 15 <= age <= 25:
        return "Youth"
    elif 26 <= age <= 35:
        return "Young Adults"
    elif 36 <= age <= 50:
        return "Adults"
    else:
        return "Senior Citizens"

df["Age Group"] = df["age"].apply(categorize_age)
addiction_level_values={"Mild":1,"Moderate":2,"Severe":3}
df["addiction_level"]=df["addiction_level"].map(addiction_level_values)

avg_usage = df.groupby("Age Group")["addiction_level"].mean().dropna()
avg_usage=avg_usage.sort_values()

plt.figure(figsize=(8,5))
plt.barh(avg_usage.index, avg_usage.values, edgecolor="black", alpha=0.8)

plt.title("Addiction Level Comparision by Age Group")
plt.ylabel("Age Group")
plt.xlabel("Addiction Level")

plt.xticks(rotation=360)

plt.show()