from graph import Graph

f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()


# Put our words in a set for O(1) lookup
word_set = set()
for word in words:
    word_set.add(word.lower())

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def get_neighbors(word1, words):
    return_words = []
    for word2 in words:
        numDif = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                numDif += 1
        if numDif == 1:
            # make a edge
            return_words.append(word2)

    return return_words


# word_set = ['sail', 'bail', 'boil', 'boll',
#             'bolt', 'boat', 'asjdhfkjasdhf', 'make']


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


# BFS with path


def find_word_ladder(beginWord, endWord):
    # build graph
    # each word is a node
    # each connection is every other word that is the same length and only has one letter diffrence
    graph = Graph()
    filteredWords = []
    for word1 in word_set:
        if len(word1) == len(beginWord):
            filteredWords.append(word1)

    for word1 in filteredWords:
        graph.add_vertex(word1)

    for word1 in filteredWords:
        neighbors = get_neighbors(word1, filteredWords)

        for neighbor in neighbors:
            graph.add_edge(word1, neighbor)

    return graph.bfs(beginWord, endWord)


print(find_word_ladder("sail", "boat"))
