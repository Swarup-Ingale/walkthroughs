from typing import List

class Solution:
    def generateSchedule(self, n: int) -> List[List[int]]:
        if n <= 4:
            return []

        total_matches = n * (n - 1)
        rem_games = [2 * (n - 1)] * n
        unused = {(u, v) for u in range(n) for v in range(n) if u != v}

        schedule = []
        last_teams = set()

        for _ in range(total_matches):
            best_match = None
            best_score = (-1, -1)

            for u, v in unused:
                if u not in last_teams and v not in last_teams:
                    score = (rem_games[u] + rem_games[v], max(rem_games[u], rem_games[v]))
                    if score > best_score:
                        best_score = score
                        best_match = (u, v)

            u, v = best_match
            schedule.append([u, v])
            unused.remove((u, v))
            rem_games[u] -= 1
            rem_games[v] -= 1
            last_teams = {u, v}

        return schedule