import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('complaints_jan_feb_2020.csv')
top_complaint_1 = df1.groupby('complaint_type')['count'].sum().idxmax()
# Plot occurrences over Jan-Feb
top_complaint_df1 = df1[df1['complaint_type'] == top_complaint_1]
top_complaint_df1 = top_complaint_df1.groupby('borough')['count'].sum().reset_index()
top_complaint_df1 = top_complaint_df1.sort_values(by='count', ascending=False)

# Plot occurrences over Jan-Feb
plt.figure(figsize=(8, 4))
plt.bar(top_complaint_df1['borough'], top_complaint_df1['count'])
plt.xlabel('Borough')
plt.ylabel('Number of Complaints')
plt.title(f'Number of "{top_complaint_1}" Complaints in Jan-Feb 2020')
plt.tight_layout()
plt.show()
