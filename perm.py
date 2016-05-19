from itertools import permutations
from random import shuffle
import enchant
import nltk
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
        for entry in i:
            tmp = entry
            carry = 0
            for j in known:
                tmp = tmp[0:j[0]+carry] + j[1] + tmp[j[0]+carry:]
                carry += 1
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
    secret = raw_input("Enter encoded word, using underscores and uppercase letters: ")
    string = raw_input("Enter string of available characters: ")
    num = 0
    known = []
    for idx, entry in enumerate(secret):
        if entry == '_':
            num+=1
        else:
            known.append([idx, entry])

    print shuffled_perm(string, num, known)

if __name__ == '__main__':
    main()
