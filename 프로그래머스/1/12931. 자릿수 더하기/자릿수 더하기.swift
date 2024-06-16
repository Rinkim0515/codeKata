import Foundation

func solution(_ n:Int) -> Int
{
    var answer:Int = 0
    var temp = n

    while temp != 0 {
        answer += temp % 10
        temp = temp / 10
    }
    
    
    return answer
}