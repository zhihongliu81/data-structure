def oddEvenList(head):
        if not head:
            return head
            
        res = odd = head
        evenHead = even = head.next

        while evenHead or (even and even.next):
            if even and even.next:
                odd.next = even.next
                odd = odd.next
                even.next = odd.next
                even = even.next
            else:
                odd.next = evenHead
                head = evenHead
                odd = head
                evenHead = even = head.next

        return res
