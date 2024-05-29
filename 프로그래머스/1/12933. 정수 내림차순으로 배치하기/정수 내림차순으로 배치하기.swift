func solution(_ n:Int64) -> Int64 {
    let temp = String(n)
    var result = String(temp.sorted(by: >))
    
    
    return Int64(result)!
}