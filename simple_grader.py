#lib
import subprocess
import sys
from importlib import import_module

#function to centered average from list of nums
#used to compare outputs from external programs
def centered_average(nums:list):
    #initialize min and max
    maxn = nums[0]
    minn = nums[0]
    
    #initialize total and count
    total = 0
    count = len(nums)
    
    #for each num in nums, check if new max or min
    for num in nums:
        if num > maxn:
            maxn = num
        if num < minn:
            minn = num
        
        #add num to total
        total += num
    
    #get average by subtracting max and min from total and
    #dividing result by count - 2
    avg = (total - maxn - minn) / (count - 2)
    return int(avg)

#function to get correct output
def correct(s):
    #split testcase values (s) and get number of test cases (t)
    s = s.split()
    t = int(s[0])
    
    #initialize index and out list
    index = 1
    out = []
    
    #go through each test case
    for i in range(1, t + 1):
        #get number of values and increase index
        k = int(s[index])
        index += 1
        
        #initialize list of test case values
        k_values = []
        
        #add each value of test case to list
        for j in range(k):
            k_values.append(int(s[index]))
            index += 1
        
        #get correct output of testcase and append to out list
        out_str = f"Case #{i}: {centered_average(k_values)}"
        out.append(out_str)
    
    return out

def main():
    #get source files
    #and for each file, run and compare output
    for arg in sys.argv[1:]:
        script = arg
        
        #open testcases file
        with open("testcases.txt") as f:
            in_str = f.read()
            
            #get correct output by passing in testcases to correct()
            correct_outs = correct(in_str)
            
            #run test script and store outputs as list
            result = subprocess.run(['python', script], input=in_str, capture_output=True, text=True)
            test_outs = result.stdout.split("\n")[:-1]
            
            #initialize count and pass_count
            count = 0
            pass_count = 0
            
            #for each correct output, compare to test output
            for i in range(len(correct_outs)):
                count += 1
                
                #if test output is same as correct output for case
                #print pass
                if correct_outs[i] == test_outs[i]:
                    pass_count += 1
                    print(f"Test Case {i + 1} passed.")
                    
                #else print fail
                else:
                    print(f"Test Case {i + 1} failed.")
            
            #print number of cases passed out of total cases.
            print(f"{pass_count}/{count} case(s) passed.")

main()
