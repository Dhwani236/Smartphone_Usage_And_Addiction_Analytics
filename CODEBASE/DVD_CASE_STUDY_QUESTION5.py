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

# Plot
plt.figure(figsize=(8,5))

sns.boxplot(x=df["Age Group"], y=df["daily_screen_time_hours"], palette='coolwarm',showfliers=True)   

plt.title("Distribution of Smartphone Usage Across Age Groups")
plt.xlabel("Age Group")
plt.ylabel("Daily Screen Time (in hours)")

plt.show()