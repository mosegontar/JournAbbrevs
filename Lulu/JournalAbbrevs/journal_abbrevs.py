import shelve

def journal_lookup(search_term):
    keyword = [x for x in search_term.split() if x > 3]
    journal_dict = shelve.open('journal_dict')

    found = []
    for key, value in journal_dict.items():
        if set(keyword).issubset(set(key.split())):
            found.append((key, value))

    for index, item in enumerate(sorted(found)):
        print '[%d] ' % index + item[0].title() + ' = ' + item[1].title()



if __name__ == "__main__":    
    
    while True:
        print "S to Search | Q to Quit"
        choice = raw_input("> ")
        
        if choice.lower() == 'q':
            break
        elif choice.lower() == 's':
            journal_keyword = raw_input("Journal Keyword Search: ")
            print "-" * 20
            print
            journal_lookup(journal_keyword.lower())       
        else:
            print "Unintelligble...What do you want to do?"
