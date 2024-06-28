func solution(_ s: String, _ n: Int) -> String {
    var result = ""

    for char in s {
        if char == " " {
            result += " "
        } else {
            let asciiValue = char.asciiValue!
            let isUppercase = asciiValue >= 65 && asciiValue <= 90
            let isLowercase = asciiValue >= 97 && asciiValue <= 122
            var newAsciiValue = asciiValue

            if isUppercase {
                newAsciiValue = (asciiValue - 65 + UInt8(n)) % 26 + 65
            } else if isLowercase {
                newAsciiValue = (asciiValue - 97 + UInt8(n)) % 26 + 97
            }

            result += String(UnicodeScalar(newAsciiValue))
        }
    }

    return result
}