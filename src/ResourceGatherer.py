import urllib.request
from bs4 import BeautifulSoup

__author__ = 'Moriya Shrine'


def get_image_urls_from_page(page_url):
    response = urllib.request.urlopen(page_url)
    html = response.read()
    soup = BeautifulSoup(html)
    output = []
    all_images = soup.find_all('img')
    for img in all_images:
        img_url = img["src"]
        if img_url.endswith('.bmp'):
            output.append(img_url)
    return output


def download_images(image_urls):
    image_name = 'image'
    extension = '.bmp'
    counter = 0
    image_paths = []
    for image_url in image_urls:
        image_path = image_name + str(counter) + extension
        urllib.request.urlretrieve(image_url, image_path)
        image_paths.append(image_path)
        counter += 1
    return image_paths