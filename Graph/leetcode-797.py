"""
797. All Paths From Source to Target
Difficulty: Medium
Related Topic: Graph, DFS, Recursive


Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

Example:
Input: [[1,2], [3], [3], []] 
Output: [[0,1,3],[0,2,3]] 
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Note:

The number of nodes in the graph will be in the range [2, 15].
You can print different paths in any order, but you should keep the order of nodes inside one path.
"""

class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def _walk_path(idx, path):

            if len(graph[idx]) == 0:
                path_list.append(path)

            for vertex in graph[idx]:
                _walk_path(vertex, path + [vertex])

            return path_list

        path_list = []

        return _walk_path(0, [0])


graph = [[1,2], [3], [3], []] 
solution = Solution()
output = solution.allPathsSourceTarget(graph)

print(output)
