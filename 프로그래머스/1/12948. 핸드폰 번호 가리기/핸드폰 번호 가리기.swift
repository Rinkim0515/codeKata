func solution(_ phone_number:String) -> String {
    let maskedPrefix = String(repeating:"*",count : phone_number.count - 4)
    let suffix = phone_number.suffix(4)
    return maskedPrefix + suffix
}