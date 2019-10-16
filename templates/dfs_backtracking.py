class Solution(object):

    def permute(self,nums):
        rtlist = []
        templist = []
        self.backtrack(rtlist,templist,nums)
        return rtlist


    #rtlist用来存储所有的返回所有排列，templist用来生成每个排列
    def backtrack(self,rtlist,templist,nums):
        if(len(templist) == len(nums)):
            rtlist.append(templist[:])
        else:
            for i in nums:

                if(i in templist): #如果在当前排列中已经有i了，就continue，相当于分支限界，即不对当前节点子树搜寻了
                    continue
                templist.append(i)
                self.backtrack(rtlist,templist,nums)
                templist.pop() #把结尾的元素用nums中的下一个值替换掉，遍历下一颗子树
