

def same_necklace(word):

    checklist = []
    for i in range(len(word)):
        scramble = word[i+1::] + word[0:i]
        checklist.append(scramble)
    print(checklist)

same_necklace('Nicole')