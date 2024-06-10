func solution(_ s:String) -> String {
    var temp : [String] = s.map{String($0)}
    var result : String = ""
    
    temp.sort(by: >)
    
    result = temp.joined(separator: "")
    
    return result
}

