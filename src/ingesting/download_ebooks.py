import os
import requests

BASE_DIR = "ebooks"
ids = [1342, 11, 54374, 1952, 84, 76, 1661, 54376, 98, 2542, 2591, 1232, 844, 158, 74, 54371, 54370, 345, 1400, 5200, 2701, 1184, 4300, 30254, 54372, 54360, 27827, 174, 2814, 2600, 1260, 16328, 23, 5740, 1497, 2500, 219, 135, 308, 24384, 160, 54375, 120, 54378, 1080, 16, 244, 30360,
       1322, 100, 1404, 54367, 54369, 140, 35, 2554, 8800, 768, 236, 1399, 521, 42, 779, 786, 730, 28054, 829, 161, 41, 45, 10, 375, 12, 2147, 3207, 55, 3296, 996, 36, 147, 19942, 1112, 10625, 34901, 33283, 1251, 14264, 3600, 3090, 2148, 31284, 54364, 46, 2097, 1727, 103, 20203, 805, 4363, 766]

def download_ebook(ebook_id):
    url = "https://www.gutenberg.org/files/%s/%s.txt" % (ebook_id, ebook_id)
    response = requests.get(url)
    file_name = os.path.join(BASE_DIR, ebook_id)
    if not os.path.exists(file_name):
        file_to_save = open(file_name, "w")
        file_to_save.write(response.text.encode("utf-8"))
        print "Downloaded:%s" % ebook_id

if __name__ == "__main__":
    if not os.path.exists(BASE_DIR):
        os.mkdir(BASE_DIR)

    info = { "pg30360.txt": { "title": "MY SECRET LIFE", "author": "Anonymous" } }

    for current_id in ids:
        if current_id in info:
            data = info[current_id]
            title = data['title']
            author = data['author']
        else:
            title, author = download_ebook(str(current_id))

        print title
        print author
