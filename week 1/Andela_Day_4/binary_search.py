
class BinarySearch(list):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        for i in range(1, a + 1):
            self.append(i * b)
            self.length = len(self)
#our search method containing the val argument
    def search(self, val):

        self.sort()
        left = 0
        right = self.length - 1
        count = 0
        present = False

        # checking if argument is not present in the list
        if val not in self:
            present = True
            val_index = -1


        # trying to check if argument is present in the list
        if val == self[self.a]:
            val_index = self.a
            present = True
        elif val == self[self.last]:
            val_index = self.last
            present = True

        # binary search algorithm using a while loop
        while right <= left and not present:
            mid = (right + left) // 2
            if self[mid] == val:
                present = True
                val_index = mid
            else:
                count += 1  # update counter when an interaction occurs
                if val < self[mid]:
                    left = mid - 1
                else:
                    right = mid + 1

        return {'count': count, 'index': val_index}
       