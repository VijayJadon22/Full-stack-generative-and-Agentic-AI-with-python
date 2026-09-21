import threading
import requests
import time


def download(url):
    print(f"Starting download from {url}")
    response = requests.get(url)
    print(f"Fineshed downloading from {url}, size {len(response.content)} bytes")


urls = [
    "https://wallup.net/wp-content/uploads/2016/02/18/286966-nature-photography.jpg",
    "https://tse3.mm.bing.net/th/id/OIP.FTOqIxe6Pu146Hl-KY_YTwHaHa?r=0&w=1440&h=1440&rs=1&pid=ImgDetMain&o=7&rm=3",
    "https://tse2.mm.bing.net/th/id/OIP.10wo2WRMlIcz8XiclZZUagHaFj?r=0&w=900&h=675&rs=1&pid=ImgDetMain&o=7&rm=3",
]

start = time.time()
threads = []

for url in urls:
    t = threading.Thread(target=download, args=(url,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()

print(f"Total time taken : {end - start:.2f} seconds")
