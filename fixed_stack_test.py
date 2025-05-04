from enum import Enum
from fixed_stack import FixedStack

menu = Enum(
    "Menu", ["푸시", "팝", "피크", "검색", "카운트", "포함", "비우기", "종료"]
)  # 메뉴를 열거형으로 정의


def select_menu() -> menu:
    """메뉴 선택"""
    while True:
        print(
            "0: 푸시, 1: 팝, 2: 피크, 3: 검색, 4: 카운트, 5: 포함, 6: 비우기, 7: 종료"
        )
        menu = int(input("메뉴를 선택하세요: "))
        if menu in range(8):
            return menu
        print("잘못된 메뉴입니다. 다시 선택하세요.")


s = FixedStack(64)  # 스택 크기 64로 초기화

while True:
    print(f"현재 데이터 수: {len(s)} / {s.capacity}")
    menu = select_menu()  # 메뉴 선택

    if menu == 0:  # 푸시
        x = int(input("푸시할 값을 입력하세요: "))
        try:
            s.push(x)  # 스택에 푸시
        except FixedStack.Full:
            print("스택이 가득 찼습니다.")
    elif menu == 1:  # 팝
        try:
            x = s.pop()  # 스택에서 팝
            print(f"팝한 값: {x}")
        except FixedStack.Empty:
            print("스택이 비어 있습니다.")
    elif menu == 2:  # 피크
        try:
            x = s.peek()  # 스택에서 피크
            print(f"피크한 값: {x}")
        except FixedStack.Empty:
            print("스택이 비어 있습니다.")

    elif menu == 3:  # 검색
        x = int(input("검색할 값을 입력하세요: "))
        idx = s.find(x)
        if idx == -1:
            print("검색한 값이 없습니다.")
        else:
            print(f"검색한 값의 인덱스: {idx}")
    elif menu == 4:  # 카운트
        x = int(input("카운트할 값을 입력하세요: "))
        count = s.count(x)
        print(f"카운트한 값의 개수: {count}")
    elif menu == 5:  # 포함
        x = int(input("포함 여부를 확인할 값을 입력하세요: "))
        if x in s:
            print("포함되어 있습니다.")
        else:
            print("포함되어 있지 않습니다.")
    elif menu == 6:  # 비우기
        s.clear()
        print("스택을 비웠습니다.")
    elif menu == 7:  # 종료
        print("종료합니다.")
        break
    else:
        print("잘못된 메뉴입니다. 다시 선택하세요.")
    print()  # 줄 바꿈
