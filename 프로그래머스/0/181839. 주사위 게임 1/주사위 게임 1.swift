import Foundation

func solution(_ a:Int, _ b:Int) -> Int {
    let isAEven = a % 2 != 0 //true가 홀수 
    let isBEven = b % 2 != 0 // true가 홀수 
    
    if isAEven && isBEven {
        return (a * a) + (b * b)
    } else if isAEven || isBEven{
        return 2 * (a + b)
    } else {
        return a - b > 0 ? a - b : -(a - b)
    }
    
}