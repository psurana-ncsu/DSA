class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        store = set()
        for val in bank:
            store.add(val)
        visited= set()
        queue = deque([startGene])
        mapp = {"A":["C", "G", "T"], "C":["A", "G", "T"], "G":["C", "A", "T"], "T":["C", "G", "A"]}
        level =0
        while queue:
            t = len(queue)
            for i in range(t):
                curr = queue.popleft()
                if curr==endGene:
                    return level
                visited.add(curr)
                for j in range(8):
                    for s in mapp[curr[j]]:
                        temp = curr[0:j]+s+curr[j+1:8]
                        if temp not in visited and temp in store:
                            queue.append(temp)
            level+=1
        return -1

        
