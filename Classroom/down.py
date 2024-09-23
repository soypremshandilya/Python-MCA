import requests

def download_file(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"File '{file_name}' downloaded successfully.")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

if __name__ == "__main__":
    url = 'https://pagalnew.com.se/files/download/id/918.mp3'
    file_name = 'lollipop_lagelu.mp3' 
    download_file(url, file_name)