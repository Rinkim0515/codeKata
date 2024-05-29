func solution(_ x:Int) -> Bool {
    var str: [Int] = []
    var temp = 0
    str = String(x).map{ Int(String($0))! }
    for i in str {
        temp += i
    }
    if x % temp == 0 {
                return true
    } else {
        return false
    }
    
    
}