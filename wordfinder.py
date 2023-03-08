from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary.
        >>> word_finder = WordFinder("test.txt")
        4 words read
        >>> word_finder.get_list_of_words_from_file("test.txt")
        ['Merit', 'Carrot', 'Parrot', 'Karat']
    """

    def __init__(self, path_to_txt_file):
        """ Creates a new instance of WordFinder """

        self.words_list = self.get_list_of_words_from_file(path_to_txt_file)
        # TODO: get rid of 16 and len(self.words_list) rename words_list to words
        # self.num_of_words_read = len(self.words_list)
        print(f"{self.num_of_words_read} words read")

    def __repr__(self):
        return f"<WordFinder path_to_txt_file={self.path_to_txt_file}>"

    def get_list_of_words_from_file(self, path_to_txt_file):
        """ Generates a list of words from a text file """
        words_list = []  # TODO: could be a list comprehension
        file = open(path_to_txt_file)

        for line in file:
            word = str(line.rstrip())
            words_list.append(word)

        return words_list

    def random(self):
        """ Gets a random word from the list of words"""
        return choice(self.words_list)


class SpecialWordFinder(WordFinder):
    """SpecialWordFinder: filters out comments and blank lines,
     returns random word """

    # def __init__(self, path_to_txt_file):
    #     """ Extends from WordFinder, creates SpecialWordFinder"""
    #     super().__init__(path_to_txt_file)

    def __repr__(self):
        return f"<SpecialWordFinder path_to_txt_file={self.path_to_txt_file}>"

    def get_list_of_words_from_file(self, path_to_txt_file):
        """ Generates filtered list of words"""
        # TODO: how to properly extend from super on longer methods
        # super().get_list_of_words_from_file() + ?
        words_list = []

        for line in super().get_list_of_words_from_file(path_to_txt_file):
            if not line == '' and not line.startswith('#'):
                word = line
                words_list.append(word)

        return words_list
