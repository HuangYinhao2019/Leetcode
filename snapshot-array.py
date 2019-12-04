import math
class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.snaparr = [0] * length
        self.setarr = [0] * length
        self.snaptime = 0
        for i in range(length):
            self.snaparr[i] = [0]
            self.setarr[i] = [0]
    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.setarr[index].append(val)
        self.snaparr[index].append(self.snaptime)

    def snap(self):
        """
        :rtype: int
        """
        self.snaptime += 1
        return self.snaptime - 1

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        mid = (int)(len(self.snaparr[index]) / 2)
        l = (int)(len(self.snaparr[index]) / 2)
        while mid < len(self.snaparr[index]) and mid > 0:
            if self.snaparr[index][mid] > snap_id and snap_id >= self.snaparr[index][mid-1]:
                return self.setarr[index][mid-1]
            else:
                if self.snaparr[index][mid-1] > snap_id:
                    l = math.ceil(l / 2)
                    mid = mid - l
                else:
                    if self.snaparr[index][mid] <= snap_id:
                        l = math.ceil(l / 2)
                        mid = mid + l
        return self.setarr[index][len(self.setarr[index])-1]

test = SnapshotArray(3)
test.set(0,5)
test.snap()
test.set(0,6)
print(test.get(0,0))