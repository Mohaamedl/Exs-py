def replaceNums(text):
    words=(text).split()
    print(words)
    nums={"1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine","0":"zero"}
    for word in words:
        for num in nums.keys():
            if word==num:
                words=list(map(lambda x: x.replace(word,nums.get(num)),words))
    text=' '.join(map(str,words))
    return text   
print(replaceNums("era uma ves 2 batatas e 4 meloes"))