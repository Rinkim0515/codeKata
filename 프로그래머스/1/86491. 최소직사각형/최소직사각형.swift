import Foundation

func solution(_ sizes:[[Int]]) -> Int {
    var firstIndex = 0
    var secondIndex = 0
    for i in sizes {
    let x = max(i[0], i[1]) // 60, 70, 60, 80 -> 80 저장
    // 배열마다의 값 안에서의 최댓값
    let y = min(i[0], i[1])
    //배열마다의 값 안에서의 최솟값 // 50, 30, 30, 40 -> 50 저장
        if x > firstIndex { //최댓값과 다음 최댓값을 비교해서 제일 큰값을 x에 저장
            firstIndex = x //
        }
        if y > secondIndex { //최솟값과 다음최솟값을 비교해서 제일 큰값을 y에 저장
            secondIndex = y //
        }

    }
    print(firstIndex * secondIndex)
    
    
    return firstIndex * secondIndex
}