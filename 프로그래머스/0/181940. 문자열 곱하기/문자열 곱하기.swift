import Foundation

func solution(_ my_string:String, _ k:Int) -> String {
    var temp = ""
    for i in 0..<k {
        temp += my_string
    }
    return temp
}