import math

class ListofListsSort:
    max_number_length = 0

    def get_number_length(self, num):
        """
        Get the number of digits in an integer.

        Args:
            num (int): The integer to count digits.

        Returns:
            int: The number of digits in the integer.
        """
        return int(math.log10(num)) + 1

    def int_to_list(self, num: int):  # 469 -> [9,6,4]
        """
        Convert an integer to a list of digits.

        Args:
            num (int): The integer to convert.

        Returns:
            list: The list of digits in the integer, in reverse order.
        """
        numlist = []
        num = int(num)
        len = 1
        while num >= 10:
            n = num % 10
            numlist.append(n)
            num = num // 10
            len += 1
        self.max_number_length = max(len, self.max_number_length)
        numlist.append(num)
        return numlist

    def pad_number_list_with_zeros(self, numlist: list):  # [9,6,4]  -> [9,6,4,0,0,0]
        """
        Add zeros to the end of a list to make it the same length as the longest list.

        Args:
            numlist (list): The list to pad with zeros.

        Returns:
            int: The length of the final padded list.
        """
        lena = len(numlist)
        pad = self.max_number_length - lena
        finalL = lena + pad
        if pad > 0:
            numlist.extend([0] * pad)
        return finalL

    def insert_number_list(self, numlist: list, parent: list):
        """
        Insert a number list into the list of lists, creating new sublists as necessary.

        Args:
            numlist (list): The number list to insert.
            parent (list): The parent list to insert into.
        """
        if numlist:
            digit = numlist.pop()
            if parent:
                parent.append( [digit, []])
                self.insert_number(numlist, parent[-1][1])
            else:
                parent.append( [digit, []])
                self.insert_number(numlist, parent[-1][1])
        else:
            if parent == []:
                parent.append([1, []])
            else:
                parent[0][0] += 1

    def insert_number(self, numlist: list, parent: list):
        """
        Recursively insert a number list into the list of lists, creating new sublists as necessary.

        Args:
            numlist (list): The number list to insert.
            parent (list): The parent list to insert into.
        """
        if numlist:
            digit = numlist.pop()
            # print(lemh, len(parent))
            lenL = max(0, len(parent) - 1)
            # print(lop, len(parent))
            i = min(lenL, digit)
            if parent:
                while i > -1:
                    if parent[i][0] == digit:
                        self.insert_number(numlist, parent[i][1])
                        break

                    elif parent[i][0] > digit:
                        if i == 0:
                            parent.insert(0, [digit, []])
                            self.insert_number(numlist, parent[0][1])
                            break
                        i -= 1

                    elif parent[i][0] < digit:
                        parent.insert(i + 1, [digit, []])
                        self.insert_number(numlist, parent[i + 1][1])
                        break
            else:
                parent.append( [digit, []])
                self.insert_number(numlist, parent[0][1])
        else:
            if parent == []:
                parent.append([1, []])
            else:
                parent[0][0] += 1

    def collapse_list_of_lists( self, lol: list, onelist: list = [], sum: int = 0 ):  # collapses list of lists back into a list of numbers
        """
        Recursively flattens a list of lists of digits into a single list of integers.

        Args:
            lol (list): The list of lists to be flattened.
            onelist (list, optional): The resulting list of integers (defaults to an empty list).
            sum (int, optional): The current integer being constructed (defaults to 0).

        Returns:
            None. The result is stored in the `onelist` argument.
        """
        #if lol:
            #print(lol)
            #lol.sort(key=lambda x: x[0], reverse=False)
            #print(lol)
        for list in lol:
            if list[1] == []:
                i = list[0]
                while i > 0:
                    onelist.append(sum)
                    i -= 1
                break
            self.collapse_list_of_lists(list[1], onelist, (sum * 10) + list[0])

    def sort_list(self, nums: list):
        """
         Sorts a list of integers in ascending order using a List of Lists data structure.

         Args:
          nums (list): A list of integers to sort.

         Returns:
           list: A new list of integers sorted in ascending order.
        """
        list = []
        lolanswr = []  # list of lists answer
        onelist = []
        for num in nums:
            list.append(self.int_to_list(num))
        for numlist in list:
            self.pad_number_list_with_zeros(numlist)
            self.insert_number(numlist, lolanswr)
        # print(answr)
        self.collapse_list_of_lists(lolanswr, onelist)
        return lolanswr
        # print(self.rtaa(answr, g))


def main(): 
        while True:
            try:
                user_input = input("Enter a list of integers separated by commas: ")
                integer_list = [int(x.strip()) for x in user_input.split(",")]
                sorted_list = ListofListsSort().sort_list(integer_list)
                print("The sorted list is:", sorted_list)
                return
            
            except ValueError:
                print("Error: Invalid input. Please enter a list of integers separated by commas.")
            
            except Exception as e:
                print("An error occurred:", e)

if __name__ == "__main__":
    main()

# [23,67,3,5]

# [0,2,6]
# [5,3][3]

# [0,4,6,7]
