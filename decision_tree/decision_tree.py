#libraries
import math

#classes
class Decision:
    name: str
    answers: dict
        
    def __init__(self, name: str):
        self.name = name
    
    def init_answers(self, answers: dict):
        self.answers = answers
    
    def get_answer(self, data: dict):
        feature = data[self.name]
        
        if feature in self.answers:
            answer = self.answers[feature]
        else:
            print("ERROR: INVALID DATA SET")
            return -1
        
        if answer in [True, False]:
            return answer
        else:
            return answer.get_answer(data)
        
#decisions
DECISIONS = ["patrons", "hungry", "type", "frisat"]

PATRONS = Decision(DECISIONS[0])
HUNGRY = Decision(DECISIONS[1])
TYPE = Decision(DECISIONS[2])
FRISAT = Decision(DECISIONS[3])

#answers
PATRONS.init_answers({"none": False, "some": True, "full": HUNGRY})
HUNGRY.init_answers({"yes": TYPE, "no": False})
TYPE.init_answers({"french": True, "italian": False, "thai": FRISAT, "burger": True})
FRISAT.init_answers({"no": False, "yes": True})

#data set
data_set = []

f = open("input.txt", "r")

for line in f.readlines():
    features = line.split()
    data = {"patrons": features[0], "hungry": features[1], "type": features[2], "frisat": features[3]}
    data_set.append(data)
    
f.close()

#analyze data
data_results = []

for data in data_set:
    result = PATRONS.get_answer(data)
    data_results.append([data, result])
    print(result)
    
entropy = []

for i, decision in enumerate(DECISIONS):
    answer_set = {}
    
    for result in data_results:
        answer = result[0][decision]
        
        if answer in answer_set:
            nums = answer_set[answer]
            answer_set[answer] = [nums[0] + 1 * result[1], nums[1] + 1]
        else:
            answer_set[answer] = [1 * result[1], 1]
    
    for answer in answer_set:
        nums = answer_set[answer]
        
        p = nums[0] / nums[1]
        n = (nums[1] - nums[0]) / nums[1]
        
        if p == 0:
            p = 1
            
        if n == 0:
            n = 1
        
        entropy = -1 * (p) * math.log2(p) + -1 * (n) * math.log2(n)
        answer_set[answer] = [entropy, nums[1]]
        
    entropy = 0
    
    for answer in answer_set:
        nums = answer_set[answer]
        entropy += nums[0] * nums[1] / 12
    
    print(f"{decision}? is {entropy:.4f} bits.")