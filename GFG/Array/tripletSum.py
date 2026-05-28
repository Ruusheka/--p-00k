class Solution:
    def countTriplet(self, arr):
        # code hereclass Solution:
        arr.sort()
        n=len(arr)
        trip=set()
        
        for i in range(n):
            seen=set()
            
            for j in range(i+1,n):
                need=arr[j]-arr[i]
                
                if need in seen:
                    a=need
                    b=arr[i]
                    c=arr[j]
                    
                    trip.add(tuple(sorted((a,b,c))))
                seen.add(arr[j])
            
        return len(trip)
                