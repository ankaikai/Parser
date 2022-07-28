# path to arrays with words and sites#
path_to_bad_words = './bad_words.txt'
path_to_dangerous_sites = './Informational_dangerous_sites.txt'

# characteristics of facebook user profile
OBSCENE_LEXICON = 1
SUSCEPTIBLE_MANIPULATION = 2
CONDUCIVE_LEARNING = 3


# extract data from txt
elements_posts = ["блять,сука нахуй, ебать", "пизда ебал, жопа жопа", "жопа, жопа жопа, osp-ua.info", "dialog.ua, proua.com.ua, ua-novosti.info", "infoaccent.net, antikor.com.ua bbc-ccnn"]
parsed_words = str(elements_posts)
# extract data from txt
def extract_data(path):
    data_read = ""
    file = open(path, encoding='utf-8')
    for line in file:
        data_read += line.lower()
    return data_read

# Characteristic of person#
def print_characteristic(characteristic):
    if characteristic == OBSCENE_LEXICON:
        print("Виражається нецензурною лексикою")
    elif characteristic == SUSCEPTIBLE_MANIPULATION:
        print("Піддається маніпуляціям")
    else:
        print("Сприятливий до навчання")


# __Here will parsed post from facebook__#
print(parsed_words)

bad_words_text = extract_data("../bad_words.txt")
informational_dang_sites = extract_data("../Informational_dangerous_sites.txt")

bad_words = bad_words_text.split("\n")
dang_sites = informational_dang_sites.split("\n")

# Checking of bad words equals
countBadWords = 0
for bad_word in bad_words:
    if bad_word in parsed_words:
        countBadWords += 1
print(f"Кількість використаних нецензурних слів: {countBadWords}")
if countBadWords >= 10:
    print_characteristic(OBSCENE_LEXICON)

# Checking of danger sites equals
countBadSites = 0
for bad_site in dang_sites:
    if bad_site in parsed_words:
        countBadSites += bad

print(f"Кількість маніпулятнивних сайтів на сторінці: {countBadSites}")
if countBadSites >= 3:
    print_characteristic(OBSCENE_LEXICON)



# Checking of danger sites equals
