from typing import Any
from collections import deque


class Stack:

    def __init__(self, maxlen: int = 256) -> None:
        """스택 초기화"""
        self.capacity = maxlen
        self.__stk = deque([], maxlen)

    def __len__(self) -> int:
        """스택에 쌓여 있는 데이터 수를 반환"""
        return len(self.__stk)

    def is_empty(self) -> bool:
        """스택이 비어 있나요?"""
        return len(self.__stk)
    
    def is_full(self) -> bool:
        """스택이 가득 차 있나요?"""
        return len(self.__stk) == self.__stk.maxlen
    
    def push(self, value: Any) -> None:
        """스택에 푸시"""
        self.__stk.append(value)

    def pop(self) -> Any:
        """스택에서 팝"""
        return self.__stk.pop()

    def peek(self) -> Any:
        """스택에서 피크"""
        return self.__stk[-1]

    def clear(self) -> None:
        """스택을 비움"""
        self.__stk.clear()

    def find(self, value: Any) -> int:
        """스택에서 value를 찾아 인덱스를 반환"""
        try:
            return self.__stk.index(value)
        except ValueError:
            return -1

    def count(self, value: Any) -> int:
        """스택에서 value의 개수를 반환"""
        return self.__stk.count(value)

    def __contains__(self, value: Any) -> bool:
        """스택에 value가 포함되어 있나요?"""
        return value in self.__stk

    def dump(self) -> None:
        """스택 안의 모든 데이터를 바닥부터 꼭대기 순서로 출력"""
        print(self.__stk)    