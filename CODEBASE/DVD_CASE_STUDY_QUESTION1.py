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

df['Age Group'] = df['age'].apply(categorize_age)

avg_usage = df.groupby('Age Group')['daily_screen_time_hours'].mean()

plt.figure(figsize=(8,5))
sns.barplot(x=avg_usage.index, y=avg_usage.values, palette="viridis", edgecolor="black", alpha=0.8)

plt.title("Average Smartphone Usage by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Average Usage (in hours)")

plt.xticks(rotation=360)
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.show()