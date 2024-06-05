func solution(_ arr:[Int]) -> [Int] {
    guard arr.count > 1 else{ return [-1]}
        
    var temp : [Int] = []
    var minNum = 0
    
    minNum = arr.min()!
    
    temp = arr.filter{$0 > minNum}

    
    
     
    return temp
}