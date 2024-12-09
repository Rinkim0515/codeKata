import Foundation


func solution(_ numer1:Int, _ denom1:Int, _ numer2:Int, _ denom2:Int) -> [Int] {
let top = numer1 * denom2 + numer2 * denom1
    let bottom = denom1 * denom2
    
    func gcd(_ a: Int, _ b: Int) -> Int {
        var a = a, b = b
        while b != 0 {
            let remainder = a % b
            a = b
            b = remainder
        }
        return a
    }
    
    let divisor = gcd(top, bottom)
    return [top / divisor, bottom / divisor]
}