func solution(_ num:Int) -> Int {
    guard num != 1 else{ return 0 }
    var count = 0
    var temp = num
    
    while temp != 1  {
        temp = temp % 2 == 0 ? temp/2 : (temp * 3) + 1
        count += 1
        if count > 500 { break }
    }
    return count > 500 ? -1 : count
}