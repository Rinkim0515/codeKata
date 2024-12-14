import Foundation

func solution(_ a:Int, _ b:Int) -> Int {
    guard let num1 = Int(String(a) + String(b)), 
    let num2 = Int(String(b) + String(a))  else { return 0 }
    if num1 == num2 || num1 > num2 {
        return num1
    } else { return num2 }
    
    
    
} 