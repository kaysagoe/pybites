import os
import re
import urllib.request
from collections import Counter

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, "stopwords")
harry_text = os.path.join(tmp, "harry")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt", stopwords_file
)
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/harry.txt", harry_text
)


def get_harry_most_common_word():
    with open(harry_text) as harry_file, open(stopwords_file) as stopwords_f:
        harry = harry_file.read().splitlines()
        stopwords = set(stopwords_f.read().splitlines())

    words = list()

    for line in harry:
        words.extend(
            [
                word_trans
                for word in line.split(" ")
                if (word_trans := re.sub(r"[^\w]", "", word.lower())) not in stopwords
                and word_trans
            ]
        )
    return Counter(words).most_common(1)[0]
    pass
