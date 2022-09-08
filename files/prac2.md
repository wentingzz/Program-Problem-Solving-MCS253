## Reverse Linked List
Write a function to reverse the linked list.

    class Node:
         def __init__(self, val=0, next=None):
             self.val = val
             self.next = next
    def reverse(head):
        cur = head
        newH = None
        while cur:
            newH = Node(cur.val, newH)
            cur = cur.next
        return newH
    
    def rev(L,R)
        if not L:
            return R
        else:
            rev(L.next, Node(L.val, R))
    
    Node* reverse(Node* head) {
        Node* prev = new Node(head->val, nullptr);
        Node* curr = head->next;
    
        while (curr != nullptr) {
            prev = new Node(curr->val, prev);
            curr = curr->next;
        }
        return prev;
    }
    
    
    
    def reverse(head):
        if not head:
            Return None;
    
        current = Node(head.val)
        next = None
        cur = head
            while cur:
                next = Node(cur.next.val, current)
                cur = cur.next
                current = next
        return current
        Node* pointer
