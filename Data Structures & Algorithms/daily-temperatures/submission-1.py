class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        output = [0] * n
        # for temp in reversed(temperatures):
        #     if current < temp:
        #         current = temperatures.pop()
        #     else:
        #         temperatures.pop()
        # for i in range(length):
        #     if current < temperatures[i]:


        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                output[prev_index] = i - prev_index
            stack.append(i)

        return output