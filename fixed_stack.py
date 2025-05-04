from typing import Any


class FixedStack:

    class Empty(Exception):
        """비어 있는 FixedStack에 pop 또는 top을 호출했을 때 발생"""

        pass

    class Full(Exception):
        """가득 차 있는 FixedStack에 push를 호출했을 때 발생"""

        pass

    def __init__(self, capacity: int) -> None:
        """스택 초기화"""
        self.stk = [None] * capacity  # 스택 본체
        self.capacity = capacity  # 스택 크기
        self.ptr = 0  # 스택 포인터

    def __len__(self) -> int:
        """스택에 쌓여 있는 데이터 수를 반환"""
        return self.ptr

    def is_empty(self) -> bool:
        """스택이 비어 있나요?"""
        return self.ptr <= 0

    def is_full(self) -> bool:
        """스택이 가득 차 있나요?"""
        return self.ptr >= self.capacity

    def push(self, value: Any) -> None:
        """스택에 푸시"""
        if self.is_full():
            raise FixedStack.Full  # 스택이 가득 찬 경우 예외 발생
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        """스택에서 팝"""
        if self.is_empty():
            raise FixedStack.Empty  # 스택이 비어 있는 경우 예외 발생
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        """스택에서 피크"""
        if self.is_empty():
            raise FixedStack.Empty  # 스택이 비어 있는 경우 예외 발생
        return self.stk[self.ptr - 1]

    def clear(self) -> None:
        """스택을 비움"""
        self.ptr = 0

    def find(self, value: Any) -> int:
        """스택에서 value를 찾아 인덱스를 반환"""
        for i in range(self.ptr - 1, -1, -1):
            if self.stk[i] == value:
                return i
        return -1
    
    def count(self, value: Any) -> int:
        """스택에서 value의 개수를 반환"""
        count = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                count += 1
        return count
    
    def __contains__(self, value: Any) -> bool:
        """스택에 value가 포함되어 있나요?"""
        return self.count(value) > 0
    
    def dump(self) -> None:
        """스택 안의 모든 데이터를 바닥에서 꼭대기 순서로 출력"""
        if self.is_empty():
            print("스택이 비어 있습니다.")
        else:
            print(self.stk[:self.ptr])
