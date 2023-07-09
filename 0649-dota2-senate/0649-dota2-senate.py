class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = collections.deque()
        dire = collections.deque()
        n = len(senate)


        for i in range(len(senate)):
            radiant.append(i) if senate[i] == "R" else dire.append(i)
        
        while radiant and dire:
            rindex = radiant.popleft()
            dindex = dire.popleft()

            if rindex < dindex:
                radiant.append(rindex + n)
            else:
                dire.append(dindex + n)
            
            # print(n)
      
        
        return "Radiant" if radiant else "Dire"

