"""what is the  recursive problem of coin change?
the coin change problem seeks a solution that returns the min number of coins required to sum up to  the given value .
the recursive approach checks the length of all the combinations which sum up to give the value and returns the minimum
combination length """

####program 

def count(s,target):
    if target==0:
        return 1
    #return 0 if total becomes negative
    if target<0:
        return 0
    #initialize the total number of ways to zero
    result=0
    #do for each coin
    for c in s:
        #recur to see if total can be reached by including current coin 'c'
        result+=count(s,target-c)
        #return the total number of ways
    return result
if __name__=='__main__':
    #'n' coins of given denomination
    s=[1,2,3]
    #total change required
    target=3
    print("total number of ways to get 3:",count(s,target))
    
