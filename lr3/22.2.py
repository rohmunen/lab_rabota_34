#БСБО-05-19 Салынь Даниил Леонидович
def partial_sums(*nums):
    result_list = [0]
    list_nums = list(nums)
    for i in range(0, len(list_nums)):
        if i == 0:
            result_list.append(list_nums[i])
        else:
            result_list.append(sum(list_nums[:i + 1]))
    return (result_list)


print(partial_sums(13))
print(partial_sums(1, 0.5, 0.25, 0.125))
