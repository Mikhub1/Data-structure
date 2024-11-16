recursive_search(self, head, x):
        if head is None:
            return False
        if head.data == x:
            return True
        return self.recursive_search(head.next, x)

    def search(self, x):
        return self.recursive_search(self.head, x)