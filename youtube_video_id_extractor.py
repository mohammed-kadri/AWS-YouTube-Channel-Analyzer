import re
import argparse

# Function to extract YouTube video ID from a URL
def extract_video_id(url):
    # Regex pattern to match YouTube video IDs
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

# Main function
def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Extract YouTube video IDs from a file containing video links.')
    parser.add_argument('-i', '--input-file', required=True, help='Input file containing YouTube video links (one per line).')
    parser.add_argument('-o', '--output-file', required=True, help='Output file to save the extracted video IDs.')
    args = parser.parse_args()

    # Read input file and extract video IDs
    video_ids = []
    with open(args.input_file, 'r') as infile:
        for line in infile:
            url = line.strip()
            if url:  # Skip empty lines
                video_id = extract_video_id(url)
                if video_id:
                    video_ids.append(video_id)
                else:
                    print(f"Warning: Could not extract video ID from URL: {url}")

    # Write video IDs to output file
    with open(args.output_file, 'w') as outfile:
        for video_id in video_ids:
            outfile.write(video_id + '\n')

    print(f"Successfully extracted {len(video_ids)} video IDs and saved them to {args.output_file}.")

if __name__ == '__main__':
    main()