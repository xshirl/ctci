# replace all spaces with %20

def urlify(str):
    return str.strip().replace(' ', '%20')

print(urlify("Mr John Smith"))