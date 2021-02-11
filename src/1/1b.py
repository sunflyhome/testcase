def findDupletters(arr):
    arr_dict={}
    arr_set=set()
    for letter in arr:
        if arr[letter] in arr_dict:
            #it's a duplicated string or letter
            arr_set.add(arr[letter])
            arr_dict[arr[letter]]+=1
        else:
            arr_dict[arr[letter]]=1
    print (list(arr_set))
    
dict={"1":"a",
"2":"b",
"4":"c",
"5":"d",
"8":"e",
"9":"a",
"0":"b"}

findDupletters(dict)


