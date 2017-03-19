import os
import re
import sys

from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

def extract_title_author(file_name):
    contents = open(file_name).read()
    title_re = re.compile(r"Title\:.+")
    author_re = re.compile(r"Author\:.+")

    title_match = title_re.search(contents)
    author_match = author_re.search(contents)

    title = ""
    author = ""

    if title_match:
        title = title_match.group()
        title = title.strip().replace("Title: ", "")

    if author_match:
        author = author_match.group()
        author = author.strip().replace("Author: ", "")

    return (title, author)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        dir_to_process = sys.argv[1]
    else:
        print "Please specify input directory"
        sys.exit(-1)

    file_to_save = open("authors.txt", "w")
    info = {"pg30360.txt": {"title": "MY SECRET LIFE", "author": "Anonymous"}}

    for current_doc_id, current_file in enumerate(os.listdir(dir_to_process)):
        # Skip Hidden Files
        if current_file[0] == ".":
            continue

        if current_file in info:
            data = info[current_file]
            title = data["title"]
            author = data["author"]
        else:
            title, author = extract_title_author(
                os.path.join(dir_to_process, current_file))

        doc = {
            'author': author,
            'title': title,
            'text': open(os.path.join(dir_to_process, current_file)).read(),
            'timestamp': datetime.now(),
        }

        rec = "%s\n" % author
        file_to_save.write(rec)

        try:
            res = es.index(
                index="top100", doc_type='ebook', id=current_doc_id, body=doc)
            print res['created']
        except:
            print "Cannot index:%s" % current_file
