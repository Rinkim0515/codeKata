import Foundation

func solution(_ n:Int) -> Int {
    var result = Int(String(String(n,radix:3).reversed()))!
    result = Int(String(result),radix:3)!
    
    return result
}