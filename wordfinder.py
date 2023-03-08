from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path_to_txt_file):
        """ Creates a new instance of WordFinder """

        self.words_list = self.get_list_of_words_from_file(path_to_txt_file)
        self.num_of_words_read = len(self.words_list)
        print(f"{self.num_of_words_read} words read")


    def get_list_of_words_from_file(self, path_to_txt_file):
        """ Generates a list of words from a text file """
        words_list = []
        file = open(path_to_txt_file)

        for line in file:
            word = str(line.rstrip())
            words_list.append(word)

        return words_list

    def random(self):
        return choice(self.words_list)





