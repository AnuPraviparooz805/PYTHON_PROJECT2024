class permutation:
    def insert():
        my_nums=[]
        n=int(input('Enter the limit of your list   : '))
        print('Enter your list of number...')
        for i in range(n):
            num=int(input())
            my_nums.append(num)    
        return my_nums
    
    def permutn(nums):
        result = [[]]
        for n in nums:
            new_list = []
            for perm in result:
                for i in range(len(perm)+1):
                    neww=perm[:i] + [n] + perm[i:]
                    new_list.append(neww)
            result = new_list
        return result
P=permutation
my_nums=P.insert()
end_result=P.permutn(my_nums)
print("All permutation\n",end_result)