import Foundation

func solution(_ price:Int, _ money:Int, _ count:Int) -> Int64{
    var answer: Int = 0
    var result = 0
    for i in 1...count {
        answer += (price * i )
    }
    answer -= money
    
    guard answer >= 0 else { return Int64(0)
        }
    
    return Int64(answer)
}
