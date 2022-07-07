class Trie:
    """A node in a prefix tree, i.e. trie
    """
    def __init__(self, char='', parent=None):
        # The character at this node (may be empty str in case of root)
        self.char = char
        # Pointer to parent node
        self.parent = parent
        # Map from following characters to child nodes
        self.childmap = {}
        # Whether this node represents the end of a complete word. e.g. the 'R'
        # node at the end of 'NIGER'
        self.is_word = False
        
    @property
    def children(self):
        return self.childmap.values()
    
    @property
    def is_root(self):
        return self.parent == None
    
    @property
    def charseq(self):
        """Sequence of characters from root down to this node, as a string.
        """
        if self.is_root:
            return ''
        return self.parent.charseq + self.char
        
    def add_string(self, s):
        if not s:
            return
        ch = s[0]
        if ch not in self.childmap:
            self.childmap[ch] = Trie(ch, self)
        # If there's only one character left, then this last child node should have its 'complete word' bit set to True
        if len(s) == 1:
            self.childmap[ch].is_word = True
        self.childmap[ch].add_string(s[1:])
        
    def wordy_children(self):
        """Yield nodes in the subtree rooted at this node having the is_word flag set.
        """
        if self.is_word:
            yield self
        for child in self.children:
            yield from child.wordy_children()
    
    def n_wordy_children(self):
        return len(list(self.wordy_children()))
    
    def shortest_prefix(self):
        """Return the shortest character sequence (starting from the root) which
        corresponds to the path to a node which:
            - has this node as a descendant
            - has exactly one wordy node as a descendant
        If no such sequence exists, return None.
        """
        if self.n_wordy_children() > 1:
            return None
        shorter_prefix = self.parent.shortest_prefix()
        return shorter_prefix or self.charseq
    
    def shortest_unique_prefixes(self):
        """yield a series of (a, b) tuples, where b is a complete word, and a
        is the shortest unique prefix for that word.
        """
        for wordy in self.wordy_children():
            word = wordy.charseq
            prefix = wordy.shortest_prefix()
            yield prefix, word
    
