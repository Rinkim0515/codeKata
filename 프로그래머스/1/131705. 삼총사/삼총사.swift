import Foundation

func solution(_ number:[Int]) -> Int {
   
    var count = 0
    let length = number.count
    for a in 0..<length {
        for b in (a + 1)..<length {
            for c in (b + 1)..<length {
                if number[a] + number[b] + number[c] == 0 { count += 1 }
            }
        }
                
    }
    return count
}