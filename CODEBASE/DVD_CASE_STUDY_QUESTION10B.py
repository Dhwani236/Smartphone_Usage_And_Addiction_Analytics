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

addiction_level_values = {"Mild":1, "Moderate":2, "Severe":3}
df["addiction_level"] = df["addiction_level"].map(addiction_level_values)

cols = ["daily_screen_time_hours", "social_media_hours", "gaming_hours", "work_study_hours", "sleep_hours"]

#subplot1
plt.subplot(2,3,1)
sns.pairplot(df[cols + ["addiction_level"]], hue='addiction_level', palette='Set2', diag_kind='kde')       

plt.suptitle("Pair Plot of Smartphone Usage Variables", y=1.02)


#subplot2
stack_data = df.groupby("age")[["social_media_hours", 'gaming_hours', 'work_study_hours']].mean().reset_index()

x = stack_data["age"]

y1 = stack_data["social_media_hours"]
y2 = stack_data["gaming_hours"]
y3 = stack_data["work_study_hours"]

plt.subplot(2,3,2)
plt.stackplot(x, y1, y2, y3, labels=['Social Media', 'Gaming', 'Work/Study'], alpha=0.8)

plt.title("Contribution of Activities to Total Smartphone Usage by Age")
plt.xlabel("Age")
plt.ylabel("Average Hours")

plt.legend(loc='upper left')


#subplot3
counts = df["addiction_level"].value_counts()
plt.subplot(2,3,3)
plt.pie(x=counts.values,labels=["Mild","Moderate","Severe"], autopct='%.0f%%', shadow=True, startangle=90, colors=sns.color_palette('pastel'))  

plt.title("Addiction Level Proportions")

plt.show()