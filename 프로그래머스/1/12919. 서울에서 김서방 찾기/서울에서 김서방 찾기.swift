func solution(_ seoul:[String]) -> String {
    var result = 0
    for (num,name) in seoul.enumerated() {
        if name == "Kim" {
            result = num 
        }
    }
    return "김서방은 \(result)에 있다"
}