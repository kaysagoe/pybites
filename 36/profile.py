from typing import Dict


def get_profile(name: str, age: int, *sports, **awards) -> Dict:
    if type(age) is not int or len(sports) > 5:
        raise ValueError()
    result = {
        "name": name,
        "age": age,
    }
    if sports:
        result["sports"] = sorted(sports)
    if awards:
        result["awards"] = {key: awards[key] for key in sorted(awards)}
    return result
