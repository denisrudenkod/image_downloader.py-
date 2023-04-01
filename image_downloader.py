import urllib.request

def download_image(url, file_path):
    try:
        urllib.request.urlretrieve(url, file_path)
        print("Image downloaded successfully.")
    except Exception as e:
        print("Error while downloading image:", str(e))

def main():
    url = input("Enter the image URL: ")
    file_path = input("Enter the file path to save the image: ")
    download_image(url, file_path)

if __name__ == "__main__":
    main()
