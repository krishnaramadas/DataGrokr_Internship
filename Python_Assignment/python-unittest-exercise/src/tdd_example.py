class TDDExample():
    def __init__(self):
        pass

    def reverse_string(self, input_str: str):
        """
        Reverses order of characters in string input_str.
        """
        return input_str[::-1]

    def find_longest_word(self, sentence: str) :
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        longest = max(sentence.split(), key=len)
        return longest

    def reverse_list(self, input_list: list) :
        """
        Reverses order of elements in list input_list.
        """
        return input_list[::-1]

    def count_digits(self, input_list: list, number_to_be_counted: int):
        """
        Return count of digits
        """
        count = 0
        for no in input_list:
            if (no == number_to_be_counted):
                count = count + 1
        return count
