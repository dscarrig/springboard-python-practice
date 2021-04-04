def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    result = ""

    index = 0
    for l in phrase:
        if index == 0:
            result += l.upper()
        elif phrase[index - 1] == " ":
            result += l.upper()
        else:
            result += l.lower()
    
        index += 1

    return result

print(titleize('this is awesome'))
print(titleize('oNLy cAPITALIZe fIRSt'))