import requests
import sys

def main(url_parameter):

    if url_parameter:
        url = url_parameter
    else:
        url = "https://s3.ap-south-1.amazonaws.com/haptikinterview/chats.txt"
    
    data = {}
    file = requests.get(url)
    chat_text_list = file.text.split("\n")

    for line in chat_text_list:
        if line:
            try:
                start = line.index("<") + len("<")
                end = line.index(">",start)
                name = line[start:end]
            except:
                name = ""
            wordcount = len(line.split())-1
            if name in data:
                data[name][0] += 1
                data[name][1] += wordcount
            else:
                data[name] = [1, wordcount]
    
    first = ["", 0]
    second = ["", 0]
    third = ["", 0]

    for name in data:
        score = data[name][0]*data[name][0] + data[name][1]
        if score >= first[1]:
            third = second
            second = first
            first = [name, score]
        elif first[1] > score >= second[1]:
            third = second
            second = [name, score]
        elif score >= 3:
            third = [name, score]

    print([first[0], second[0], third[0]])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main("")