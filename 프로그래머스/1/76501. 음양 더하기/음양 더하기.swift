import Foundation

func solution(_ absolutes:[Int], _ signs:[Bool]) -> Int {
    var result = 0
    var i = 0
    
    while i < absolutes.count {
        result += signs[i] ? absolutes[i] : -(absolutes[i])
        i += 1
    }
   
    
    return result
}