


from gtts import gTTS
import os
from pygame import mixer # load the popular external library
import time

# using google text to speech api, convert a line to speech, 
# do count of words in the above line
# store in a text file and covert to audio/speech using gtts api
def saveandreadaudofile(filename, line):
    language = "en"
    if line != "":
        myobj = gTTS(text = line, lang=language, slow=False)
        myobj.save("welcome.mp3")
        os.system("mpg321 welcome.mp3")
        f = "welcome.mp3"
    else:
        f = open(filename.name, "r")
        contents = f.read()
        myobj = gTTS(text = contents, lang=language, slow=False)
        myobj.save("sample.mp3")
        os.system("mpg321 sample.mp3")
        f = "sample.mp3"
    

    #To play the music.
    mixer.init()
    mixer.music.load(f)
    
    mixer.music.play()
    time.sleep(60)
    

def printwordstheircounts():
    line = "Hello, This is my first program to use google text to speech api"
    saveandreadaudofile("welcome.mp3",line)
        
    # lets write below file input and output to file and save to .mp3 and have it read with gtts
    words = line.split()
    dict1 = {}
    for word in words:
        print(word)
        #dict1.update({word : 1})
        if word in dict1:
            dict1[word] = dict1[word] + 1
        else:
            dict1.update({word : 1})
    
    text_file = open("sample.txt", "w+")

    print("**********************\r\n")
    print("Given sentence is: \r\n " + line)
    text_file.write("Given sentence is: \r\n " + line)
    text_file.write("\r\n")

    print("**********************\r\n")
    print("Total number of words in a given sentence is " + str(len(dict1)))
    text_file.write("Total number of words in a given sentence is" + str(len(dict1)))
    text_file.write("\r\n")
    print("**********************\r\n")

    
    for k, v in dict1.items():
        print("'" + k + "'" + " Word is occuring is " + str(v) + " times")
        text_file.write("'" + k + "'" + " Word is occuring " + str(v) + " times")
        text_file.write("\r")

    text_file.close()
    time.sleep(5)
    saveandreadaudofile(text_file,"")
    


if __name__ == "__main__":
    printwordstheircounts()