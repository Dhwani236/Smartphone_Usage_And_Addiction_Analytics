import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/dhwan/OneDrive/Documents/college/SEM 4/DVD/Smartphone_Usage_And_Addiction_Analysis_7500_Rows-2.csv")

stack_data = df.groupby("age")[["social_media_hours", 'gaming_hours', 'work_study_hours']].mean().reset_index()

x = stack_data["age"]

y1 = stack_data["social_media_hours"]
y2 = stack_data["gaming_hours"]
y3 = stack_data["work_study_hours"]

plt.figure(figsize=(10,5))

plt.stackplot(x, y1, y2, y3, labels=['Social Media', 'Gaming', 'Work/Study'], alpha=0.8)

plt.title("Contribution of Activities to Total Smartphone Usage by Age")
plt.xlabel("Age")
plt.ylabel("Average Hours")

plt.legend(loc='upper left')

plt.show()