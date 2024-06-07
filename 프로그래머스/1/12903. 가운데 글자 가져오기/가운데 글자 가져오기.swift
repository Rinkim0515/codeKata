func solution(_ s:String) -> String {
    let leng = s.count
    let sIsArray = Array(s)
    let midAt = leng/2

    if leng % 2 == 0 {
        return String(sIsArray[midAt - 1...midAt])
    } else {
        return String(sIsArray[midAt])
    }
}