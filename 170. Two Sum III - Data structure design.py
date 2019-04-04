class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ds = {}
        

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number not in self.ds:
            self.ds[number] = 1
        else:
            self.ds[number] += 1
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        if value % 2 == 0 and value // 2 in self.ds and self.ds[value // 2] > 1:
            return True
        # Iterate through data structure and manually check
        diff_dict = {}
        for num in self.ds:
            if num in diff_dict:
                return True
            diff_dict[value - num] = 1
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
