import copy

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        d = {}
        # Save all pair sum
        n = len(nums)
        res = []
        for i in range(n-1):
            for j in range(i, n):
                s = nums[i] + nums[j]
                if s in d:
                    d[s] = d[s].extend([i,j])
                else:
                    d[s] = [i,j]
        
        for i in range(n-1):
            for j in range(j, n):
                s = target - nums[i]-nums[j]
                if d.has_key(s):
                    a = d[s]
                    if len(a) == 2:
                        if i in a or j in a:
                            continue
                        else:
                            res.append([nums[i], nums[j], nums[a[0]], nums[a[1]]])
                    else:
                        x = [nums[i], nums[j]]
                        a.remove(i)
                        a.remove(j)

                        for k in range(0,len(a),2):
                            x.append(nums[a[k]])
                            x.append(nums[a[k+1]])
                            res.append(copy.deepcopy(x))
                            x.remove(-1)
                            x.remove(-1)
        return res

                    

        