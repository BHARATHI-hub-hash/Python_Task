#defining function
def minimize_mango_difference(mangoes, M):
    #sort
    mangoes.sort()

    #minimum diff
    min_diff = float('inf')

    #finding the minimum diff
    for i in range(len(mangoes) - M + 1):
        diff = mangoes[i + M - 1] - mangoes[i]
        min_diff = min(min_diff, diff)

        #return min value
        return min_diff
mangoes = [12, 4, 7, 9, 15, 10]
M=3
result = minimize_mango_difference(mangoes, M)
print(f"The minimum difference iss: {result}")