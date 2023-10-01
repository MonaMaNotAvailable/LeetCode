from typing import List
# import json

def combine(n: int, k: int) -> List[List[int]]:
    sol=[]
    def backtrack(remain,comb,nex):
		# solution found
        if remain==0:
            sol.append(comb.copy())
        else:
			# iterate through all possible candidates
            for i in range(nex,n+1):
				# add candidate
                comb.append(i)
                # print(remain, comb, nex)
				#backtrack
                backtrack(remain-1,comb,i+1)
				# remove candidate
                comb.pop()
            
    backtrack(k,[],1)
    return sol

result = combine(20, 15)
print(result)

# # Convert the result to JSON format
# result_json = json.dumps(result)

# # Write the JSON data to a text file
# with open('output.txt', 'w') as file:
#     file.write(result_json)