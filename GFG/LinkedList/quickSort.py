'''
Structure of linked list Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

def getTail(cur):
    while cur is not None and cur.next is not None:
        cur = cur.next
    return cur


def partition(head, end):
    pivot = end
    prev = None
    cur = head
    tail = pivot

    newHead = None

    while cur != pivot:
        if cur.data < pivot.data:
            if newHead is None:
                newHead = cur
            prev = cur
            cur = cur.next
        else:
            if prev:
                prev.next = cur.next
            tmp = cur.next
            cur.next = None
            tail.next = cur
            tail = cur
            cur = tmp

    if newHead is None:
        newHead = pivot

    newEnd = tail

    return pivot, newHead, newEnd


def quickSortRecur(head, end):
    if head is None or head == end:
        return head

    pivot, newHead, newEnd = partition(head, end)

    if newHead != pivot:
        temp = newHead
        while temp.next != pivot:
            temp = temp.next

        temp.next = None

        newHead = quickSortRecur(newHead, temp)

        tail = getTail(newHead)
        tail.next = pivot

    pivot.next = quickSortRecur(pivot.next, newEnd)

    return newHead


def quickSort(head):
    if head is None or head.next is None:
        return head

    tail = getTail(head)
    return quickSortRecur(head, tail)