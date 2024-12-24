import Foundation

func solution(_ num_list:[Int]) -> Int {
    var even = ""
    var odd = ""
    for i in num_list {
        if i % 2 != 0 {
            even += String(i)
        } else {
            odd += String(i)
        }
    }
    guard let answer1 = Int(even),
    let answer2 = Int(odd) else { return 0 }
    
    
    
    return answer1 + answer2
}