func solution(_ arr:[Int], _ divisor:Int) -> [Int] {
    var arr1: [Int] = []
    for i in arr {
        if i % divisor == 0 {
            arr1.append(i)
        }
    }
    if arr1.isEmpty {
        arr1.append(-1)
    }
    arr1.sort()
    
    return arr1
}