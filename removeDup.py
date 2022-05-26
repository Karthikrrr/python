nums=[1,1,2]
i=0
index=0
x=list()
for i in range(0,len(nums)-1):
    if(nums[i]!=nums[i+1]):
        #print(nums[i])
        #print(nums[i+1])
        nums[index]=nums[i]
        i=i+1
        index=index+1
    print(index)