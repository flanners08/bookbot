

# returns a wordcount from a string
def wordcount(the_text) -> None:
    numwords=len(str.split(the_text))
    return numwords

# returns a dictionary of character counts from a string
def charcount(the_text) -> dict:
    charcount = {}
    the_text = the_text.lower()
    for char in the_text:
        if char in charcount:
            charcount[char] += 1
        else:
            charcount[char] = 1
    return charcount 


def sort_on(items):
    return items[1]

def sorted_dict(countlist):
    items = list(countlist.items())
    items.sort(key=sort_on, reverse=True)  # Sort by value, descending
    return items


