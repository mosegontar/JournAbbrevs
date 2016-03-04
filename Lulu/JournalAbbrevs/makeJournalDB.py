import shelve

journal_dict = shelve.open('journal_dict')

data = open('master.txt', 'r').readlines()

for entry in data:
    entry = entry.strip('\n')
    journal_kv = entry.split('=')
    journal_dict[journal_kv[0].lower()] = journal_kv[1].lower()

journal_dict.close()
