class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # Approach 1: bfs with explicit mutation generation and visited set
        # time = O(nl^2), space = O(nl) where n = len(bank) and l = len(gene)
        # if endGene is not in the bank, return -1 immediately
        if endGene not in bank:
            return -1
        # initialize the queue with the startGene and set of visited genes
        queue = deque([(startGene, 0)])
        visited = set([startGene])
        # define possible mutations
        mutations = ['A', 'C', 'G', 'T']
        while queue:
            currentGene, mutationCount = queue.popleft()
            # if the current gene is the endGene, return the mutation count
            if currentGene == endGene:
                return mutationCount
            # try all possible single mutations
            for i in range(len(currentGene)):
                for m in mutations:
                    # create a new gene by mutating the i-th position
                    if currentGene[i] != m:
                        newGene = currentGene[:i] + m + currentGene[i+1:]
                        # if the new gene is in the bank and not visited
                        if newGene in bank and newGene not in visited:
                            visited.add(newGene)  # mark new gene as visited
                            queue.append((newGene, mutationCount + 1))  # add new gene to queue with incremented count
        # if we exit the loop without finding endGene, return -1
        return -1



        # # Approach 2: bfs with level order traversal and direct comparison
        # # time = O(n^2l) therefore slower if n>l, space = O(nl)
        # queue = deque([startGene])  # initialize queue with startGene
        # count = 0  # to track the number of mutations
        # while queue and count <= len(bank):
        #     # print(queue)
        #     levelSize = len(queue)  # number of genes to process at current level
        #     for _ in range(levelSize):
        #         gene = queue.popleft()  # get the first gene in the queue
        #         # find the gene that is one letter different from the current gene
        #         for option in bank:
        #             # print(gene, option)
        #             # terminate directly if reaching the end goal
        #             if gene == endGene:
        #                 return count  # return the mutation count if endGene is found
        #             diff = 0  # to count the number of differences
        #             for i in range(8):  # genes are of length 8
        #                 if gene[i] != option[i]:
        #                     diff += 1  # increment diff for each differing letter
        #             if diff == 1 and option not in queue:  # only one letter difference
        #                 queue.append(option)  # add the option to the queue
        #     count += 1  # increment mutation count after processing current level
        # return -1  # return -1 if no valid mutation path is found