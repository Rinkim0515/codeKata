import Foundation

func solution(_ n:Int) -> Int {
    
    var result = 0
 
    
    for ai in 1...n {
        if ai%2 == 0 {
            result += ai
        }
        
    }
    
    
    return result
}