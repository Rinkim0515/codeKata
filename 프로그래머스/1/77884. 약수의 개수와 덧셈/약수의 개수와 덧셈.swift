
import Foundation

func solution(_ left:Int, _ right:Int) -> Int {
    var count = 0
    var arr1 : [Int] = []
    for i in left...right {
        
        for j in 1...i {
            
            if i % j == 0 {
                count += 1
            }
            
        }
        if count % 2 == 0 {
            arr1.append(i)
        } else {
            arr1.append(-i)
        }
        count = 0
        
    }
    
    return arr1.reduce(0,+)
}