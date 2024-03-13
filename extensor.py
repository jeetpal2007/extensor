import os
import re
import sys

def check_extension(file_path, extension):
    with open(file_path, 'r') as file:
        urls = file.readlines()

    urls_with_extension = []
    for url in urls:
        url = url.strip()
        if url.endswith(f".{extension}"):
            urls_with_extension.append(url)

    return urls_with_extension

def save_to_file(urls, file_name):
    with open(file_name, 'w') as file:
        for url in urls:
            file.write(f"{url}\n")

if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    extension = input("Enter the file extension (e.g., .js, .css): ")
    file_name = input("Enter the file name to save the URLs: ")

    urls_with_extension = check_extension(file_path, extension)
    save_to_file(urls_with_extension, file_name)

    print(f"{len(urls_with_extension)} URLs with {extension} extension have been saved to {file_name}.")
                                                                                                                  
