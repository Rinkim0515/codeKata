def solution(brown, yellow):
    
    total = brown + yellow
    for i in range(3,total + 1):
        if total % i == 0:
            j = total // i
            if (i - 2) * ( j - 2 ) == yellow:
                return sorted([i,j], reverse = True)
                
                    
                
            
        
            
            
    
    