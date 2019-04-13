class Solution:
    def nextClosestTime(self, time: str) -> str:
        h, m = time.split(":")
        origin = set(time)
        i = int(h)
        j = int(m)
        
        while True:
            j += 1
            if j == 60:
                j = 0
                i += 1
            if i == 24:
                i = 0
            str_i = str(i) if i > 9 else "0" + str(i)
            str_j = str(j) if j > 9 else "0" + str(j)
            cur_time = str_i + ":" + str_j
            if set(cur_time).issubset(origin):
                return cur_time
