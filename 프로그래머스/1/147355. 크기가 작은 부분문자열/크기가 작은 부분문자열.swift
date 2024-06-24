import Foundation

func solution(_ t:String, _ p:String) -> Int {
    var length = p.count
    var pInt = Int(p)!
    var cnt = 0
    for i in 0...(t.count - length ) {
        let s = t.dropFirst(i).prefix(length)
        if pInt >= Int(s)! { cnt += 1 }
    }
    return cnt
}