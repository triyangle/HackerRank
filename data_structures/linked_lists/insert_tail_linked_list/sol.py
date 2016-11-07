def Insert(head, data):
#    if not head:
#        head = Node(data)
#    elif not head.next:
#        head.next = Node(data)
#    else:
#       Insert(head.next, data)
#    return head

    if not head:
        return Node(data)
    return Node(head.data, Insert(head.next, data))
