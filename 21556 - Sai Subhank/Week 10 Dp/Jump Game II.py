class Solution(object):
    def jump(self, n):
        count=0 
        l=r=0
        rnxt=0
        i=0
        steps=0                                       
        jumpcount=0 
        if len(n) == 1:
            return 0
        while r<len(n)-1:
            for i in range(l, r+1):
                print("i=",i,l,r,"1")
                rnxt = max(rnxt, i + n[i])
                print(rnxt)
            l = r + 1
            r = rnxt
            print(l,r,"2")
            steps+=1
            print(steps,"step")
        return steps
            
