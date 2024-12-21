import Foundation

func solution(_ start_num:Int, _ end_num:Int) -> [Int] {
    var count = start_num
    var answer: [Int] = []
    while count <= end_num {
        answer.append(count)
        count += 1
    }
    
    return answer
}