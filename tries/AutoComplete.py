# Autocomplete.py


class TrieNode():
    def __init__(self):
        self.next = {}
        self.is_leaf = False
    ## END

    def add_into_trie(self, word):
        for ch in word:
            if(ch not in self.next):
                node = TrieNode()
                self.next[ch] = node
            ## END
            self = self.next[ch]
        ## END
        self.is_leaf = True
    ## END

    def search(self, item):
        if(self.is_leaf and len(item) == 0):
            return True
        ## END
        first = item[:1]
        str = item[1:]
        if first in self.next:
            return self.next[first].search(str)
        else:
            return False
        ## END
    ## END

    def traversal(self, item):
        if(self.is_leaf):
            print(item)
        ## END
        for i in self.next:
            s = item + i
            self.next[i].traversal(s)
        ## END
    ##END

    def autoComplete(self, item):
        i = 0
        s = ''
        while i < len(item):
            k = item[i]
            s += k
            if k in self.next:
                self = self.next[k]
            else:
                return 'NOT FOUND'
            ## END
            i += 1
        ## END
        self.traversal(s)
        return 'END'
    ## END
## END


def main():
    list_of_words = ["sit", "sin"] #, "sir", "sine", "show", "shows", "shown", ]
    trie_node = TrieNode()
    for word in list_of_words:
        trie_node.add_into_trie(word)
    ## END
    print(trie_node.autoComplete("si"))
## END


if __name__ == "__main__":
    import profile
    main()
    # profile.run("main()")
## END
