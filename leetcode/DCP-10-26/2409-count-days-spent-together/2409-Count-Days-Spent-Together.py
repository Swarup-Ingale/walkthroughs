class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def to_day_of_year(date: str) -> int:
            m = int(date[:2])
            d = int(date[3:])

            return sum(days_in_month[:m - 1]) + d
            
        alice_arrive = to_day_of_year(arriveAlice)
        alice_leave = to_day_of_year(leaveAlice)
        bob_arrive = to_day_of_year(arriveBob)
        bob_leave = to_day_of_year(leaveBob)

        overlap_start = max(alice_arrive, bob_arrive)
        overlap_end = min(alice_leave, bob_leave)

        return max(0, overlap_end - overlap_start + 1)