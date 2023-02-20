def solution(m, n, board):
    answer = 0
		# board를 2차원 배열로 변환
    Kakao_board = [list(b) for b in board]
    while True:
				# 없어진 블록들을 담을 set을 선언
        delete = set()
				# set에 없어질 블록들을 모두 담아 줌. 4*4 체크한 뒤 set에 담아서 중복 제거
        for i in range(m - 1):
            for j in range(n - 1):
                if Kakao_board[i][j] == Kakao_board[i][j + 1] == Kakao_board[i + 1][j] == Kakao_board[i + 1][j + 1] != 0:
                    delete.update(
                        [(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)])
				# 더이상 없앨 블록 없으면 이제 return하러 고고씽
        if len(delete) == 0:
            break
				# delete에 담긴 블록들을 전부 없애고(0 처리), answer에 하나씩 += 1
        for i, j in delete:
            Kakao_board[i][j] = 0
            answer += 1
				# 남은 블록들을 아래로 쭉 밀기 위하여 보드를 상 -> 하로 탐색
        for j in range(n):
						# 남은 블록들만 임시 배열에 담아 줌
            temp = []
            for i in range(m):
                if Kakao_board[i][j] != 0:
                    temp.append(Kakao_board[i][j])
						# 하 -> 상 방향으로 temp에 들어간 블록들을 차곡차곡 쌓아 줌
            for i in range(m - 1, -1, -1):
                if temp:
                    Kakao_board[i][j] = temp.pop()
								# 다 떨어졌으면 위에는 빈 공간
                else:
                    Kakao_board[i][j] = 0
    return answer