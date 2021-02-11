def findDupletters(arr):
    arr_dict={}
    arr_set=set()
    for letter in arr:
        if letter in arr_dict:
            #it's a duplicated string or letter
            arr_set.add(letter)
            arr_dict[letter]+=1
        else:
            arr_dict[letter]=1
    print (list(arr_set))
    
arr=["1","2","3","4","5","6","7","8","9","2","3","4","5","2","3","4","5","9","0"]
findDupletters(arr)


