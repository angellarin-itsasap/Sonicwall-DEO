import requests

# Step 1: Download the large text file from the website
url = 'https://cpdbl.net/lists/etknown.list'  # Replace with the actual URL
response = requests.get(url)

if response.status_code != 200:
    print("Error downloading the file.")
    exit(1)

large_text = response.text

# Step 2: Split the large text into chunks of 100 lines
lines = large_text.splitlines()
chunk_size = 100
chunks = [lines[i:i + chunk_size] for i in range(0, len(lines), chunk_size)]

# Step 3: Save each chunk as a new text file
for i, chunk in enumerate(chunks):
    filename = f'chunk_{i + 1}.txt'
    with open(filename, 'w') as f:
        f.write('\n'.join(chunk))

    print(f"Created file: {filename}")
