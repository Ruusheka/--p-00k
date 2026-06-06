def merge(self,interval):
    interval.sort()
    
    merged=[]
    
    for i in interval:
        if not merged or merged[-1][1] < i[0]:
            merged.append(i)
        else:
            merged[-1][1] = max(merged[-1][1],i[1])
        
    return merged