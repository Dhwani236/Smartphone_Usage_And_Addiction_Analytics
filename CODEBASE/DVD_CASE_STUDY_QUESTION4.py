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

# addiction_level_values = {"Mild":1,"Moderate":2,"Severe":3}
# df["addiction_level"]=df["addiction_level"].map(addiction_level_values)

plt.figure(figsize=(8,5))
sns.stripplot(x=df["addiction_level"],y=df["daily_screen_time_hours"], hue=df["addiction_level"], palette="viridis", alpha=0.7)

plt.title("Relationship between Usage and Addiction")
plt.xlabel("Addiction Levels")
plt.ylabel("Daily Screen Time (in hours)")

plt.xticks(rotation=360)

plt.show()