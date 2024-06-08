import Foundation

func solution(_ a:[Int], _ b:[Int]) -> Int {
    var resultArr : [Int] = []
    var result : Int = 0
    
    for i in 0...a.count - 1 {
        resultArr.append(a[i]*b[i])
    }
    result = resultArr.reduce(0,+)
    return result
    
}