import random
from collections import OrderedDict

# defining CFG Rules in class

class CFGRule(OrderedDict):
    def __init__(self, *args):
        super().__init__(map(lambda s: s.replace(' ', '').split('->'), args))

    def __repr__(self):
        return '\n'.join('{} -> {}'.format(k, v) for k, v in self.items())

    def getRules(self, token):
        return self[token].split('|')

# Defining Generation of sentences

def create_sentence(cfgrule, start='S'):
    string = []
    def depthfirst(root):
        local_str = ''
        product = random.choice(cfgrule.getRules(root))
        return loopOver(local_str, product)

    def loopOver(local_str, product):
        for character in product:
            if character in cfgrule:
                outcome = depthfirst(character)
                if outcome:
                    string.append(outcome)
            else:
                local_str += character
        return local_str

    depthfirst(start)
    return ' '.join(string[:-1]).capitalize() + string[-1]


if __name__ == "__main__":

    #   Defining grammar rules that are given in the cfg.gr file

    rules = ['S -> NP VP', 'VP -> Verb NP', 'NP -> Det Noun |NP PP', 'PP -> Prep NP', 'Noun -> Adj Noun', 'Verb -> "ate" | "wanted" | "kissed" | "washed" | "pickled"',
        'Det -> "the" | "a" | "every"', 'Noun -> "president" | "sandwich" | "pickle" | "mouse" | "floor"', 'Adj -> "fine" | "delicious" | "beautiful" | "old"', 'Prep -> "with" | "on" | "under" | "in"']

    # Renaming for simplicity
    table = dict(OrderedDict([('VP', 'A'), ('NP', 'B'), ('PP', 'C'), ('Noun', 'D'), ('Verb', 'E'), ('Det', 'F'), ('Adj', 'G'), ('Prep', 'H')]))

    i=0
    while (i<len(rules)):
        rules[i] = rules[i].replace('\"', '')
        for key in table:
            rules[i] = rules[i].replace(key, table[key])
        i = i+1

    context_free_grammar = CFGRule(*rules)

    text_file = open("random-sentence.txt", "w+")

    # Run your program multiple times
    print("Sentences are generated randomly is given below:")
    print("**************************")
    i=0
    while (i<5):
        print("*** %d . sentence is generated ***" % (i))
        gnd_sentence = create_sentence(context_free_grammar)
        print(gnd_sentence)
        print("\n")
        i =i+1
        text_file.write(gnd_sentence)

    text_file.close()
