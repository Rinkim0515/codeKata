func solution(_ s: String) -> String{
    var temp: String = ""
    var count: Int = 0
    
    for i in s.indices
    {
        guard String(s[i]) != " "  else{ temp.append(" ") ; count = 0 ; continue }
        
        count % 2 == 0 ? temp.append(s[i].uppercased()) : temp.append(s[i].lowercased())
        count += 1
       
    }
    return temp
}