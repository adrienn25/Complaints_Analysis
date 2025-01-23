df2 = pd.read_csv('complaints_jun_jul_2020.csv')
top_complaint_2 = df2.groupby('complaint_type')['count'].sum().idxmax()
# Plot occurrences over Jun-Jul
top_complaint_df2 = df2[df2['complaint_type'] == top_complaint_1]
top_complaint_df2 = top_complaint_df2.groupby('borough')['count'].sum().reset_index()
top_complaint_df2 = top_complaint_df2.sort_values(by='count', ascending=False)


plt.figure(figsize=(8, 4))
plt.bar(top_complaint_df2['borough'], top_complaint_df2['count'])
plt.xlabel('Borough')
plt.ylabel('Number of Complaints')
plt.title(f'Number of "{top_complaint_1}" Complaints in Jun-Jul 2020')
plt.tight_layout()
plt.show()
