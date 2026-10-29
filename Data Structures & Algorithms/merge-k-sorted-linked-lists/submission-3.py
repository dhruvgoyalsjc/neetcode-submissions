# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        heap = []

        for i, lst in enumerate(lists):
            if lst:
                heap.append((lst.val, i))
        heapq.heapify(heap)
        
        dummy = curr = ListNode()
        while heap:
            _, index = heapq.heappop(heap)
            curr.next = lists[index]
            curr = curr.next

            lists[index] = lists[index].next

            if lists[index]:
                heapq.heappush(heap, (lists[index].val, index))
        
        return dummy.next