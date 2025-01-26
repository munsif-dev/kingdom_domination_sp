def list_sorter(nums):
    #numsnew = nums     # here nums and numsnew are pointing to the same list in memory
    #if you need to create a new list in memory, you can use the following
    numsnew = nums.copy()
    #it copies the elements of nums to numsnew
    numsnew.sort()
    return numsnew


nums1 = [4,23,53,23,54,6,4,3,4,5,4,3,3]
print(nums1)
print(list_sorter(nums1))

print(nums1)

