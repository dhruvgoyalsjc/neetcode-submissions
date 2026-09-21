# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heap.append((lists[i].val, i))
        
        heapq.heapify(heap)

        dummy = curr = ListNode(None, None) # head will always be dummy.next

        while (heap):
            _, index = heapq.heappop(heap)
            curr.next = lists[index]
            curr = curr.next # make sure to update curr
            # update ith list to point to next elem in list
            lists[index] = lists[index].next
            # add next node to heap if it exists
            if (lists[index]):
                heapq.heappush(heap, (lists[index].val, index))

        return dummy.next