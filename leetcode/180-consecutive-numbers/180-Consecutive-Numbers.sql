select distinct l1.num as ConsecutiveNums
from Logs l1
Join Logs l2 on l1.id + 1 = l2.id
Join Logs l3 on l1.id + 2 = l3.id
Where l1.num = l2.num and l2.num = l3.num;