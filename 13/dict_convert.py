from collections import namedtuple
from datetime import datetime
import json


blog = dict(
    name="PyBites",
    founders=("Julian", "Bob"),
    started=datetime(year=2016, month=12, day=19),
    tags=["Python", "Code Challenges", "Learn by Doing"],
    location="Spain/Australia",
    site="https://pybit.es",
)

# define namedtuple here
Blog = namedtuple("Blog", ["name", "founders", "tags", "location", "site", "started"])


def dict2nt(dict_):
    return Blog(
        name=dict_["name"],
        founders=list(dict_["founders"]),
        tags=dict_["tags"],
        location=dict_["location"],
        site=dict_["site"],
        started=dict_["started"],
    )


def nt2json(nt):
    nt_dict = nt._asdict()
    nt_dict["started"] = nt_dict["started"].strftime("%Y-%m_%d")
    return json.dumps(nt_dict)
