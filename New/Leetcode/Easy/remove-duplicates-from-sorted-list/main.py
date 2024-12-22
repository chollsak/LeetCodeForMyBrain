from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    @staticmethod
    def from_list(values: List[int]) -> Optional['ListNode']:
        if not values:
            return None
        
        head = ListNode(values[0])
        current = head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next
        return head     

    def to_list(self) -> List[int]:
        result = []
        current = self
        while current:
            result.append(current.val)
            current = current.next
        return result  


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head  # Return the modified linked list directly

s = Solution()
l1 = ListNode.from_list([1, 1, 2])

result = s.deleteDuplicates(l1)
print(result.to_list())
