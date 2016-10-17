from itertools import permutations
import codecs
import pdb
from random import shuffle
import enchant
import nltk

def perm_shuffled(string, num, known):
    word_len = len(known) + num
    trial = []
    with codecs.open('words', 'r', encoding='utf8') as f:
        trial = f.read().splitlines()
    trial = [item for item in trial if len(item) == word_len]

    # Test the constraints one by one.
    selected = []
    for entry in trial:
        s = string
        flag = 1
        for char_idx, char in enumerate(entry):
            if len(known.keys()) > 0 and char_idx in known.keys():
                    # If it is a constraint, check it
                    if char != known[char_idx]:
                        flag = 0
                        break
            else:
                # Not a constraint, check it with the surplus text constraint
                if char in s:
                    i = s.find(char)
                    s = s[0:i]+s[i+1:]
                else:
                    flag = 0
                    break
        if flag == 1:
            selected.append(entry)

    return selected


def shuffled_perm(s,num, known):
	perms = list(permutations(s, num))
	shuffle(perms)
	res = []
	i = []
	a = []
	print "Stage 1"
	perms = list(set(perms))
        i = ["".join(p) for p in perms]
	i = list(set(i))	
        #print i
	print "Stage interim"	
        yard = 0
        for entry in i:
            tmp = entry
            yard = 0
            for j in known.keys():
                tmp = tmp[0:yard] + tmp[yard:j] + known[j[1]] + tmp[j:]
                yard = j+1
            a.append(tmp)
        #print a
        d = enchant.Dict("en_us")
        for e in a:
            if d.check(e):
                res.append(e)
        print "Stage 2"
        res = list(set(res))
        return ["".join(p) for p in res] # rebuild strings and return


def main():
    print "Welcome to the Vanirud Interface for solving Word Puzzles. Please enter your input encoded string and the allowed remnant characters as requested."
    secret = raw_input("Enter encoded word, using underscores and lowercase letters: ")
    string = raw_input("Enter string of available characters: ")
    num = 0
    known = {}
    reg_str = r""
    for idx, entry in enumerate(secret):
        if entry == '_':
            num+=1
        else:
            known[idx] = entry
            reg_str += entry


    print perm_shuffled(string, num, known)

if __name__ == '__main__':
    main()
