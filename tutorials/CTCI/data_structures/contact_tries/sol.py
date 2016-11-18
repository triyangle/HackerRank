class Trie:
    def __init__(self):
        self.val = ''
        self.branches = {}
        self.usage = 0

    def add(self, word):
        node = self
        for char in word:
            node = node.add_char(char)

    def add_char(self, char):
        if self.usage == 1:
            self.val += char
            return self

        if char in self.branches:
            branch = self.branches[char]
        else:
            self.branches[char] = Trie()
            branch = self.branches[char]

        if branch.usage == 1 and len(branch.val) > 1:
            branch.split_suffix()

        branch.val = char
        branch.usage += 1
        return branch

    def split_suffix(self):
        self.branches[self.val[1]] = Trie()
        sub_branch = self.branches[self.val[1]]
        sub_branch.val = self.val[1:]
        sub_branch.usage += 1

    def has_same_suffix(self, rest_partial):
        return self.val[1:][:len(rest_partial)] == rest_partial

    def find(self, partial):
        node = self
        for i, char in enumerate(partial):
            if node.usage == 1:
                rest_partial = partial[i:]
                return print(int(node.has_same_suffix(rest_partial)))
            if char not in node.branches:
                return print(0)
            node = node.branches[char]
        return print(node.usage)

contacts = Trie()

n = int(input().strip())

for a0 in range(n):
    op, contact = input().strip().split(' ')
    Trie.__dict__[op](contacts, contact)
