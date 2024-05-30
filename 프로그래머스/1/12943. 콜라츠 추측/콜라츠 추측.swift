func solution(_ num:Int) -> Int {
    var count = 0
    var temp = num
    while temp != 1  {
        
        if temp % 2 == 0{
            temp = temp / 2
            if count < 500 {
                count += 1
            } else {
                count = -1
                break
            }
            
        }else if temp % 2 != 0 {
            temp = (temp * 3) + 1
             if count < 500 {
                count += 1
            } else {
                 count = -1
                break
            }
        }
        
        
    }
    
    return count
}