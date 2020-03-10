"""
このファイルに解答コードを書いてください
"""
def keyFunc(e):
  return e[0]

# Main Function
if __name__ == '__main__':
    inputFile = open('.\input.txt', 'r')
    inputLines = inputFile.readlines()

    inputList = []
    result = ''

    for input in inputLines:
        if ':' in input:
            i, s = input.split(':')
            inputList.append([i, s.rstrip()])
        else:
            m = int(input)
            break
    inputFile.close()

    inputList.sort(key=keyFunc)

    for input in inputList:
        if m % int(input[0]) == 0:
            result += input[1]

    if result == "":
        print(m)
    else:
        print(result)