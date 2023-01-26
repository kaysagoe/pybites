from typing import List, Tuple, cast
from itertools import combinations, permutations


def friends_teams(
    people: List[str], team_size: int = 2, order_does_matter: bool = False
) -> List[Tuple[str, str]]:
    if order_does_matter:
        # Permutation
        return cast(List[Tuple[str, str]], permutations(people, team_size))
    else:
        # Combination
        return cast(List[Tuple[str, str]], combinations(people, team_size))
