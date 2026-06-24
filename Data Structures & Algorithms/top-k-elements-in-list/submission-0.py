class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter: dict[int, int] = {}
        
        for n in nums:
            if n in counter:
                counter[n] += 1
            else:
                counter[n] = 1
        
        sorted_counter = dict(sorted(counter.items(), key = lambda x: x[1], reverse = True))
        result = []
        for i in range(k):
            result.append(list(sorted_counter.keys())[i])
        return result
            

