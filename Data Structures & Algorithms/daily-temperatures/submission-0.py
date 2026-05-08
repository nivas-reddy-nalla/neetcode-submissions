class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        stack = []

        for day, temperature in enumerate(temperatures):
            while stack and stack[-1][1]<temperature:
                prevDay, _ = stack.pop()
                result[prevDay] = day-prevDay
            stack.append((day, temperature))
        
        stack.clear()
        return result