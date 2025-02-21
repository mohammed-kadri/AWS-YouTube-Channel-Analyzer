import requests
from isodate import parse_duration
import pandas as pd

# Function to read video IDs from a file
def read_video_ids_from_file(file_path):
    video_ids = []
    with open(file_path, 'r') as file:
        for line in file:
            video_id = line.strip()  # Remove any leading/trailing whitespace
            if video_id:  # Skip empty lines
                video_ids.append(video_id)
    return video_ids

# Function to convert ISO 8601 duration to seconds
def iso8601_duration_to_seconds(duration_str):
    dur = parse_duration(duration_str)
    return dur.total_seconds()

# Read video IDs from the input file
input_file = 'video_ids.txt'  # Replace with your input file path
video_ids = read_video_ids_from_file(input_file)

# List to store video data
videos_data = []

# YouTube Data API key (replace with your own key)
API_KEY = "AIzaSyBNFkbZ3ax-n1e807OL5JCAYo_Ve1-0wf0"

# Fetch video details for each video ID
for video_id in video_ids:
    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics,status&id={video_id}&key={API_KEY}"
    response = requests.get(url)
    data = response.json()

    # Extract video details
    try:
        title = data['items'][0]['snippet']['title']
    except Exception as e:
        title = "No Title"
        continue

    description = data['items'][0]['snippet']['description']
    thumbnail_url = data['items'][0]['snippet']['thumbnails']['default']['url']
    duration = iso8601_duration_to_seconds(data['items'][0]['contentDetails']['duration'])

    try:
        tags = data['items'][0]['snippet']['tags']
    except Exception as e:
        tags = "No Tags"

    category_id = data['items'][0]['snippet']['categoryId']
    publishedAt = data['items'][0]['snippet']['publishedAt']
    privacy_status = data['items'][0]['status']['privacyStatus']
    licensed_content = data['items'][0]['status']['license']
    captions = data['items'][0]['contentDetails']['caption']
    public_stats_viewable = data['items'][0]['status']['publicStatsViewable']

    try:
        view_count = data['items'][0]['statistics']['viewCount']
    except Exception as e:
        view_count = 0

    try:
        like_count = data['items'][0]['statistics']['likeCount']
    except Exception as e:
        like_count = 0

    try:
        comment_count = data['items'][0]['statistics']['commentCount']
    except Exception as e:
        comment_count = 0

    # Print video details (optional)
    print(f"Title: {title}")
    print(f"Video ID: {video_id}")
    print(f"Description: {description}")
    print(f"Thumbnail URL: {thumbnail_url}")
    print(f"Tags: {tags}")
    print(f"Category ID: {category_id}")
    print(f"Privacy Status: {privacy_status}")
    print(f"Licensed Content: {licensed_content}")
    print(f"Captions: {captions}")
    print(f"Public Stats Viewable: {public_stats_viewable}")
    print(f"View Count: {view_count}")
    print(f"Like Count: {like_count}")
    print(f"Comment Count: {comment_count}")
    print(f"Duration: {duration} seconds")
    print(f"Published At: {publishedAt}")
    print("-" * 40)

    # Append video data to the list
    videos_data.append({
        'video_id': video_id,
        'title': title,
        'description': description,
        'duration': duration,
        'thumbnail_url': thumbnail_url,
        'tags': tags,
        'category_id': category_id,
        'privacy_status': privacy_status,
        'licensed_content': licensed_content,
        'captions': captions,
        'public_stats_viewable': public_stats_viewable,
        'view_count': view_count,
        'like_count': like_count,
        'comment_count': comment_count,
        'publishedAt': publishedAt
    })

# Save video data to an Excel file
df = pd.DataFrame(videos_data)
excel_file_name = 'video_data.xlsx'
df.to_excel(excel_file_name, index=False, engine='openpyxl')
print(f"Data has been saved to {excel_file_name}")