from collections import Counter, namedtuple
import os
import urllib.request
import pandas as pd

# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.join(tmp, "dirnames")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/dirnames.txt", tempfile
)

IGNORE = ["static", "templates", "data", "pybites", "bbelderbos", "hobojoe1848"]

Stats = namedtuple("Stats", "user challenge")


# code


def gen_files(tempfile=tempfile):
    """
    Parse the tempfile passed in, filtering out directory names
    (first column) using the last "is_dir" column.

    Lowercase these directory names and return them as a generator.

    "tempfile" has the following format:
    challenge<int>/file_or_dir<str>,is_dir<bool>

    For example:
    03/rss.xml,False
    03/tags.html,False
    03/Mridubhatnagar,True
    03/aleksandarknezevic,True

    => Here you would return 03/mridubhatnagar (lowercased!)
       followed by 03/aleksandarknezevic
    """
    return iter(
        pd.read_csv(tempfile, names=["path", "is_dir"], header=0)
        .loc[lambda df_: df_["is_dir"]]
        .assign(path=lambda df_: df_["path"].str.lower())["path"]
    )


def diehard_pybites(files=None):
    """
    Return a Stats namedtuple (defined above) that contains:
    1. the user that made the most pull requests (ignoring the users in IGNORE), and
    2. a tuple of:
        ("most popular challenge id", "amount of pull requests for that challenge")

    Calling this function on the default dirnames.txt should return:

    Stats(user='clamytoe', challenge=('01', 7))
    """
    if files is None:
        files = gen_files()

    users = list()
    challenges = list()
    for f in files:
        challenge, user = f.split("/")

        if user in IGNORE:
            continue

        users.append(user)
        challenges.append(challenge)

    most_active_user = Counter(users).most_common(1)[0][0]
    most_popular_challenge = Counter(challenges).most_common(1)[0]

    return Stats(most_active_user, most_popular_challenge)
