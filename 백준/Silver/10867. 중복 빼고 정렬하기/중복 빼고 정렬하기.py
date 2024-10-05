def sort_unique_numbers():  # 함수 정의
    N = int(input())  # 첫 번째 입력: 정수 N을 입력받아 정수로 변환
    numbers = list(map(int, input().split()))  # 두 번째 입력: N개의 정수를 리스트로 입력받아 정수로 변환
    unique_sorted_numbers = sorted(set(numbers))  # 중복 제거(set) 후 오름차순 정렬(sorted)
    print(" ".join(map(str, unique_sorted_numbers)))  # 리스트의 정수를 문자열로 변환 후 공백으로 구분하여 출력


sort_unique_numbers()