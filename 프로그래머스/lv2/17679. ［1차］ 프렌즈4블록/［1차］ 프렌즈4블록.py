def solution(m, n, board):
    answer = 0
    Kakao_board = [list(b) for b in board]
    while True:
        delete = set()
        for i in range(m - 1):
            for j in range(n - 1):
                if Kakao_board[i][j] == Kakao_board[i][j + 1] == Kakao_board[i + 1][j] == Kakao_board[i + 1][j + 1] != 0:
                    delete.update(
                        [(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)])
        if len(delete) == 0:
            break
        for i, j in delete:
            Kakao_board[i][j] = 0
            answer += 1
        for j in range(n):
            temp = []
            for i in range(m):
                if Kakao_board[i][j] != 0:
                    temp.append(Kakao_board[i][j])
            for i in range(m - 1, -1, -1):
                if temp:
                    Kakao_board[i][j] = temp.pop()
                else:
                    Kakao_board[i][j] = 0
    return answer
