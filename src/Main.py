import urllib
from src.MessageDecoder import get_secret_message
from src.MessageEncoder import encode_message_into_bitmap
from src.ResourceGatherer import get_image_urls_from_page, download_images


message = 'Muda da! MUDA MUDA MUDA! ZA WARUDO! TOKI WO TOMARE! .....Soshite, toki ga ugoki desu... '
message += 'MUDA DA! WRYYYYYYYYYYYYYYYYYYYYYY'
image_path = 'cave.bmp'

encode_message_into_bitmap(message, image_path)

page_url = 'http://localhost/BitmapHtml/'
image_urls = get_image_urls_from_page(page_url)
image_paths = download_images(image_urls)

secret_messages = []
for path in image_paths:
    secret_messages.append(get_secret_message(path))

print(secret_messages)