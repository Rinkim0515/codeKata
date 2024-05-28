import Foundation

func solution(_ n:Int, _ k:Int) -> Int {
    var result: Int
    var num = n
    var mok = 0
    
    result = (n * 12000) + (k * 2000)
    if num >= 10 {
        mok = num / 10
        }
    result -= mok * 2000
 

    
    
    
    return result
}