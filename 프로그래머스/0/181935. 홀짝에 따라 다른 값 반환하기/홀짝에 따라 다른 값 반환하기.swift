import Foundation

func solution(_ n:Int) -> Int {
    
    var isEven = n % 2 == 0
    var total = 0
            
    for i in 1...n {
        if isEven {
            if i % 2 == 0 {
                total += i * i
            }
        } else {
            if i % 2 != 0 {
                total += i
            }
        }
    }

    
    return total
}