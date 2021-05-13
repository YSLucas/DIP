

# Mappers
def mapper_get_lines():
    """
    
    """
    res = []
    with open("data/validation.txt", "r", encoding="utf8") as f:
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
