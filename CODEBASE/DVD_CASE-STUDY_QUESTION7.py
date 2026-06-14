import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/dhwan/OneDrive/Documents/college/SEM 4/DVD/Smartphone_Usage_And_Addiction_Analysis_7500_Rows-2.csv")

addiction_level_values = {"Mild":1, "Moderate":2, "Severe":3}
df["addiction_level"] = df["addiction_level"].map(addiction_level_values)

cols = ["daily_screen_time_hours", "social_media_hours", "gaming_hours", "work_study_hours", "sleep_hours"]

sns.pairplot(df[cols + ["addiction_level"]], hue='addiction_level', palette='Set2', diag_kind='kde')       

plt.suptitle("Pair Plot of Smartphone Usage Variables", y=1.02)

plt.show()