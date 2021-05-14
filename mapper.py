

# Mappers
def mapper_get_lines(path):
    """
    Converts .txt to strings and puts it in a list
    
    @param path: path to text data
    @return    : list
    """
    res = []
    with open("data/" + path + ".txt", "r", encoding="utf8") as f:
        lines = f.readlines()

        for line in lines:
            line = line.strip()
            if line != "":
                res.append(line)
    
    return res

def mapper_replace_punct(text, sign):
    """
    Replace all punctuation with % and replace spaces with _

    @param  sign: leestekens
    @return     : text waar leestekens vervangen zijn
    """
    res = []
    for line in text:
        for i in sign:
            line = line.replace(i, "%")
        
        line = line.replace(" ", "_")
        line = line.lower()
        res.append(line)

    return res
