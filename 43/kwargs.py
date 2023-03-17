def get_profile(**kwargs):
    if len(set(kwargs.keys() - {"name", "profession"})):
        raise TypeError()
    name = kwargs.get("name", "julian")
    profession = kwargs.get("profession", "programmer")
    return f"{name} is a {profession}"
