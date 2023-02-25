import re
WORD_REGEX=re.compile(r"\b\w+\b")
with open("input/1497","r")as  file:
    
    for line in file:
        title_start = line.find("Project Gutenberg eBook of ") + len("Project Gutenberg eBook of ")
        
        title_end = line.find(",", title_start)
        title = line[title_start:title_end]
        print(title)
        author_start = line.find("by ", title_end) + len("by ")
        author_end = line.find("\n", author_start)
        author = line[author_start:author_end]
        print (author)
        #text = line[line.find("*** START OF THIS PROJECT GUTENBERG EBOOK", author_end):]
        break
    words =WORD_REGEX.findall(file)

    for word in words.split():
        if len(word)> 10:
            print (word)
            break

