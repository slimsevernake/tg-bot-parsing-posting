def format(tag):
    stringgg = ""
    for i in range(0, len(tag)):
        if "span" in str(tag[i]):
            tag.pop(i)
    for string in tag:
        stringgg += str(string).replace("h1", "h3").replace("h2", "h4")
    return(stringgg)
