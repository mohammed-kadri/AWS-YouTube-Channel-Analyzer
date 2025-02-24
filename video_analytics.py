import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file
excel_file = 'video_data.xlsx'  # Replace with your file path
df = pd.read_excel(excel_file, engine='openpyxl')

# Display basic information about the data
print("Data Overview:")
print(df.info())
print("\nFirst 5 rows:")
print(df.head())

# Convert relevant columns to numeric (if needed)
df['view_count'] = pd.to_numeric(df['view_count'], errors='coerce')
df['like_count'] = pd.to_numeric(df['like_count'], errors='coerce')
df['comment_count'] = pd.to_numeric(df['comment_count'], errors='coerce')

# Basic Analytics
print("\nBasic Analytics:")
print(f"Total Videos: {len(df)}")
print(f"Average Views: {df['view_count'].mean():.2f}")
print(f"Average Likes: {df['like_count'].mean():.2f}")
print(f"Average Comments: {df['comment_count'].mean():.2f}")

# Top 10 Most Viewed Videos
top_10_views = df.nlargest(10, 'view_count')[['title', 'view_count']]
print("\nTop 10 Most Viewed Videos:")
print(top_10_views)

# Top 10 Most Liked Videos
top_10_likes = df.nlargest(10, 'like_count')[['title', 'like_count']]
print("\nTop 10 Most Liked Videos:")
print(top_10_likes)

# Top 10 Most Commented Videos
top_10_comments = df.nlargest(10, 'comment_count')[['title', 'comment_count']]
print("\nTop 10 Most Commented Videos:")
print(top_10_comments)

# Visualization 1: Views Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['view_count'], bins=30, kde=True, color='blue')
plt.title('Distribution of Video Views')
plt.xlabel('Views')
plt.ylabel('Frequency')
plt.show()

# Visualization 2: Likes vs Views
plt.figure(figsize=(10, 6))
sns.scatterplot(x='view_count', y='like_count', data=df, color='green')
plt.title('Likes vs Views')
plt.xlabel('Views')
plt.ylabel('Likes')
plt.show()

# Visualization 3: Comments vs Views
plt.figure(figsize=(10, 6))
sns.scatterplot(x='view_count', y='comment_count', data=df, color='red')
plt.title('Comments vs Views')
plt.xlabel('Views')
plt.ylabel('Comments')
plt.show()

# Visualization 4: Top 10 Most Viewed Videos
plt.figure(figsize=(10, 6))
sns.barplot(x='view_count', y='title', data=top_10_views, palette='viridis')
plt.title('Top 10 Most Viewed Videos')
plt.xlabel('Views')
plt.ylabel('Video Title')
plt.show()

# Visualization 5: Top 10 Most Liked Videos
plt.figure(figsize=(10, 6))
sns.barplot(x='like_count', y='title', data=top_10_likes, palette='magma')
plt.title('Top 10 Most Liked Videos')
plt.xlabel('Likes')
plt.ylabel('Video Title')
plt.show()

# Visualization 6: Top 10 Most Commented Videos
plt.figure(figsize=(10, 6))
sns.barplot(x='comment_count', y='title', data=top_10_comments, palette='plasma')
plt.title('Top 10 Most Commented Videos')
plt.xlabel('Comments')
plt.ylabel('Video Title')
plt.show()

# Visualization 7: Correlation Heatmap
plt.figure(figsize=(8, 6))
corr = df[['view_count', 'like_count', 'comment_count']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()