class TopologicalSort:
    def __init__(adjlist, self) -> None:
        self.adjlist = adjlist

# Recursive Topological Sort that uses DFS
    def RecursiveSort(self) -> [list]:
        def dfs(node):
            for nei in self.adjlist[node]:
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei)
            ans.append(node)
        ans = []
        seen = set()
        for i in self.adjlist:
            if i not in seen:
                seen.add(i)
                dfs(i)
        return ans
