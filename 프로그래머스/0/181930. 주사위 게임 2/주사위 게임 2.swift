import Foundation

func solution(_ a:Int, _ b:Int, _ c:Int) -> Int {
    //pow가 되나?
    var count = 0
    let num1 = a + b + c 
    let num2 = (a * a) + (b * b) + (c * c)
    let num3 = (a * a * a) + (b * b * b) + (c * c * c)
    let cases = [ a == b, a == c, b == c]
    
    for i in cases {
        if i == true {
            count += 1
        } 
    }
    if count == 0 {
        return num1
    } else if count == 1{
        return num1 * num2
    } else {
        return num1 * num2 * num3
    }
    

}