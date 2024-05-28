import Foundation

func solution(_ numbers:[Int]) -> Double {
    
    
    var result = 0
    for us in 0...(numbers.count-1) {
        result += numbers[us]
}
    return (Double(result)/Double(numbers.count))
}