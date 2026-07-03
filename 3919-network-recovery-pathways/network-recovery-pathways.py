class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        adj = [[] for _ in range(n)]
        indeg = [0] * n
        costs_set = set()
        has_edge = False
        
        for u, v, cost in edges:
            if online[u] and online[v]:
                adj[u].append((v, cost))
                indeg[v] += 1
                costs_set.add(cost)
                has_edge = True
        
        if not has_edge:
            return -1
        
        # Topological sort (Kahn's algorithm) — valid for any edge-cost subset
        topo = []
        indeg_copy = indeg[:]
        dq = deque(i for i in range(n) if indeg_copy[i] == 0)
        while dq:
            u = dq.popleft()
            topo.append(u)
            for v, cost in adj[u]:
                indeg_copy[v] -= 1
                if indeg_copy[v] == 0:
                    dq.append(v)
        
        INF = float('inf')
        
        def check(T: int) -> bool:
            dist = [INF] * n
            dist[0] = 0
            for u in topo:
                if dist[u] == INF:
                    continue
                du = dist[u]
                for v, cost in adj[u]:
                    if cost >= T:
                        nd = du + cost
                        if nd < dist[v]:
                            dist[v] = nd
            return dist[n - 1] <= k
        
        costs = sorted(costs_set)
        lo, hi = 0, len(costs) - 1
        ans = -1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(costs[mid]):
                ans = costs[mid]
                lo = mid + 1
            else:
                hi = mid - 1
        
        return ans