class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digit = []
        letter = []
        output = []
        for l in logs:
            if l.split()[1].isdigit():
                digit.append(l)
            else:
                letter.append(l)
        
        letter = sorted(letter, key = lambda x: (x.split(' ',1)[1], x.split(' ',1)[0]))
        output.extend(letter) 
        output.extend(digit)
        return output
