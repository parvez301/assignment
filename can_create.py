
def check_if_word_is_formed(others, inputLen, nextStart):
    """ This function is recursive and eventually returns 
    True or False depending on whether the word is formed or not
    """
    for r in others:
        if r[0] == nextStart:
            if inputLen == r[1]:
                return True
            else:
                others.remove(r)
                nextStart = r[1]
                return check_if_word_is_formed(others, inputLen, nextStart+1)
    return False

def can_create(listOfStrings, input):
    """ This function is detects the first word and 
    uses check_id_word_is_formed function to 
    determine boolean output for can_create
    """
    possibleStarts = []
    others = []
    inputLen = len(input)-1
    if inputLen != -1:
        for word in listOfStrings:
            i = input.find(word)
            if i >= 0:
                endIndex = i+len(word)-1
                if i != 0:
                    others.append([i, endIndex])
                else:
                    possibleStarts = [i, endIndex]
        nextStart = possibleStarts[1]+1
        if others:
            if check_if_word_is_formed(others, inputLen, nextStart):
                return True
            return False
        elif possibleStarts:
            return True
        else:
            return False
    else:
        return False


def main():
    listOfDataStrings = ['back', 'end', 'front', 'tree']
    inputToCheck = 'backend'
    print(can_create(listOfDataStrings, inputToCheck))

if __name__ == '__main__':
        main()
