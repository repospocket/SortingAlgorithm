import json

class Node:
    def __init__(self, value=None):
        self.val = value
        self.leaves = []
        self.repeated_numbers_count = 0  # for repeated numbers in the list to be sorted
        self.Leaves_length = 0  # length of current self.leaves to not use len()

class NodeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Node):
            # Convert Node object to a dictionary
            return {'digit': obj.val, 'children': obj.leaves}
        return super().default(obj)

class TrieNodeSort:
    def int_to_list(self, num):  # 469 -> [9,6,4]
        numlist = []
        num = int(num)
        len = 1
        while num >= 10:
            n = num % 10
            numlist.append(n)
            num = num // 10
            len += 1
        self.maxlen = max(len, self.maxlen)
        numlist.append(num)
        # numlist.reverse()
        return numlist

    def pad_w_zeros(self, numlist):  # [9,6,4]  -> [9,6,4,0,0,0]
        # mutable items not allowed?
        pad = self.maxlen - len(numlist)
        while pad > 0:
            numlist.append(0)
            pad -= 1

    def insert_into_trie(self, numlist, parent):
        if numlist:
            digit = numlist.pop()
            lenL = max(0, parent.Leaves_length - 1)
            i = min(lenL, digit)
            if parent.leaves:
                while i > -1:
                    leaf = parent.leaves[i]

                    if leaf.val == digit:
                        self.insert_into_trie(numlist, leaf)
                        break

                    elif leaf.val > digit:
                        if i == 0:
                            node = Node(digit)
                            parent.leaves.insert(0, node)
                            parent.Leaves_length += 1
                            self.insert_into_trie(numlist, node)
                            break
                        i -= 1

                    elif leaf.val < digit:
                        node = Node(digit)
                        parent.leaves.insert(i + 1, node)
                        parent.Leaves_length += 1
                        self.insert_into_trie(numlist, node)
                        break
            else:
                node = Node(digit)
                parent.leaves.append(node)
                parent.Leaves_length += 1
                self.insert_into_trie(numlist, node)
                print(digit)
        else:
            parent.repeated_numbers_count += 1

    def print_trie(self, node, list, sum=0):
        sum += node.val
        if node.leaves:
            for num in node.leaves:
                self.print_trie(num, list, sum * 10)
        else:
            while node.repeated_numbers_count > 0:
                list.append(sum)
                node.repeated_numbers_count -= 1

        return list

    def sort_list(self, nums):
        self.maxlen = 0
        result = Node(0)
        list = []
        final = []
        for num in nums:
            list.append(self.int_to_list(num))
        for numlist in list:
            self.pad_w_zeros(numlist)
            self.insert_into_trie(numlist, result)
        self.print_trie(result, final)
        return [result, final]

def main():
    while True:
        try:
            user_input = input("Enter a list of integers separated by commas: ")
            integer_list = [int(x.strip()) for x in user_input.split(",")]
            sorted_list = TrieNodeSort().sort_list(integer_list)
            print("The sorted list is:", sorted_list)
            return

        except ValueError:
            print(
                "Error: Invalid input. Please enter a list of integers separated by commas.")

        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()
