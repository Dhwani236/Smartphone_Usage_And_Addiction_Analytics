# plots 1 - 6 because i want to keep the layout clean and dont want to display 9 subplots in the same plotspace
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/dhwan/OneDrive/Documents/college/SEM 4/DVD/Smartphone_Usage_And_Addiction_Analysis_7500_Rows-2.csv")

plt.subplots(2,3,figsize=(15,10))

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

#subplot1
plt.subplot(2,3,1)
sns.barplot(x=avg_usage.index, y=avg_usage.values, palette="viridis", edgecolor="black", alpha=0.8)

plt.title("Average Smartphone Usage by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Average Usage (in hours)")

plt.xticks(rotation=360)


addiction_level_values={"Mild":1,"Moderate":2,"Severe":3}
df["addiction_level"]=df["addiction_level"].map(addiction_level_values)

avg_usage = df.groupby("Age Group")["addiction_level"].mean().dropna()
avg_usage=avg_usage.sort_values()

#subplot2
plt.subplot(2,3,2)
plt.barh(avg_usage.index, avg_usage.values, edgecolor="black", alpha=0.8)

plt.title("Addiction Level Comparision by Age Group")
plt.ylabel("Age Group")
plt.xlabel("Addiction Level")

plt.xticks(rotation=360)

plt.subplot(2,3,3)
sns.lineplot(x=df["Age Group"], y=df["daily_screen_time_hours"], marker='D',linestyle='-',linewidth=0.5,color='blue',alpha=0.8)

plt.title("Smartphone Usage Trend")
plt.xlabel("Age Group")
plt.ylabel("Daily Smartphone Usage (in hours)")

plt.xticks(rotation=360)

plt.subplot(2,3,4)
sns.stripplot(x=df["addiction_level"],y=df["daily_screen_time_hours"], hue=df["addiction_level"], palette="viridis", alpha=0.7)

plt.title("Relationship between Usage and Addiction")
plt.xlabel("Addiction Levels")
plt.ylabel("Daily Screen Time (in hours)")

plt.xticks(rotation=360)

plt.subplot(2,3,5)
sns.boxplot(x=df["Age Group"], y=df["daily_screen_time_hours"], palette='coolwarm',showfliers=True)   

plt.title("Distribution of Smartphone Usage Across Age Groups")
plt.xlabel("Age Group")
plt.ylabel("Daily Screen Time (in hours)")

plt.subplot(2,3,6)
sns.violinplot(x=df["Age Group"], y=df["daily_screen_time_hours"], palette='Set2', inner='quartile')  

plt.title("Distribution of Smartphone Usage Across Age Groups")
plt.xlabel("Age Group")
plt.ylabel("Daily Screen Time (in hours)")

plt.show()