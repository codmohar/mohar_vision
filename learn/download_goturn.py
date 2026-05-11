import os
import urllib.request
import zipfile

def download_goturn():
    # Download prototxt
    if not os.path.isfile("goturn.prototxt"):
        print("Downloading goturn.prototxt...")
        urllib.request.urlretrieve("https://raw.githubusercontent.com/Mogball/goturn-files/master/goturn.prototxt", "goturn.prototxt")
        
    if not os.path.isfile("goturn.caffemodel"):
        print("Downloading goturn.caffemodel zip parts...")
        parts = []
        for i in range(1, 5):
            part_name = f"goturn.caffemodel.zip.00{i}"
            part_url = f"https://github.com/Mogball/goturn-files/raw/master/{part_name}"
            parts.append(part_name)
            if not os.path.isfile(part_name):
                print(f"Downloading {part_name}...")
                urllib.request.urlretrieve(part_url, part_name)
        
        print("Combining zip parts...")
        with open("goturn.caffemodel.zip", "wb") as outfile:
            for part in parts:
                with open(part, "rb") as infile:
                    outfile.write(infile.read())
                    
        print("Extracting zip...")
        with zipfile.ZipFile("goturn.caffemodel.zip", 'r') as zip_ref:
            zip_ref.extractall(".")
            
        print("Cleaning up zip files...")
        os.remove("goturn.caffemodel.zip")
        for part in parts:
            os.remove(part)
            
        print("Download and extraction complete!")
    else:
        print("goturn.caffemodel already exists.")

if __name__ == "__main__":
    download_goturn()
