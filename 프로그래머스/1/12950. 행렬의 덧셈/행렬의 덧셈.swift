func solution(_ arr1:[[Int]], _ arr2:[[Int]]) -> [[Int]] {
    let legngth = arr1.count
    var resultArr : [[Int]] = []
    
    for i in 0..<legngth {
        resultArr.append([])
        for j in 0..<arr1[i].count {
            resultArr[i].append(arr1[i][j]+arr2[i][j])
        }
  
    }
    
    
    return resultArr
}
