


lst1=[]
def count(lst):
    for i in lst:
        if len(i)>5:
            lst1.append(i)
    print(lst1)

lst=['meghana','viratkohili','dhoni','megh','surya']
count(lst)