class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        # dfs helper function
        def recursiveSearch(variableValuesDict:[str, List[Tuple[str, float]]], A: str, B: str, visited: set) -> float:
            # path to itself
            if A == B:
                return 1.0
            # mark A to avoid cycle
            visited.add(A)
            # iterate through A's nearby variable
            for variable, value in variableValues[A]:
                # skip visited
                if variable in visited: 
                    continue
                # no need for dfs since directly connected
                if variable==B:
                    return value
                # if not a direct connection, start dfs for each nearby variable and the final destination
                result = recursiveSearch(variableValues, variable, B, visited)
                # if a valid path exist, multiply instead of divide (a / c = a / b * b / c)
                if result != -1.0:
                    return value*result
            # base case: no valid path exist
            return -1.0


        # construct a dict to record direct connections both way
        variableValues = {}
        for i in range(len(equations)):
            A = equations[i][0]
            B = equations[i][1]
            value = values[i]

            # record A -> B
            if A not in variableValues:
                variableValues[A] = []
            variableValues[A].append((B, value))

            # record B -> A
            if B not in variableValues:
                variableValues[B] = []
            variableValues[B].append((A, 1.0/value))
        # print(variableValues)

        output = []
        for query in queries:
            C = query[0]
            D = query[1]
            # both C & D is reachable
            if C in variableValues and D in variableValues: 
                visited = set()
                result = recursiveSearch(variableValues, C, D, visited)
                output.append(result)
            else: #if any is unreachable, add -1.0 directly
                output.append(-1.0)
        
        return output