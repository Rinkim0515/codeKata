func solution(_ n:Int) -> String {
    var result = String(repeating: "수박", count: n / 2)
    
    guard n >= 0 else {return ""}
    
    switch n % 2 == 0 {
    case true : return result
    case false : return result + "수"
    
    }
    
    
}