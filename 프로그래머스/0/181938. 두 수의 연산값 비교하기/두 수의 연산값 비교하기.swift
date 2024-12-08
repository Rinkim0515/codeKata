import Foundation

func solution(_ a:Int, _ b:Int) -> Int {
    let value = 2 * a * b
    guard let strValue = Int(String(a) + String(b))
    else { return 0 }
    
    if value > Int(strValue) {
        return value
    } else { return strValue }
    
    
}