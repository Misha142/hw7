def pararam(text1):
    glas='АаЕеЁёИиОоУуЫыЭэЮюЯя'
    glas_first=0
    for el in text1[0]:
        if el in glas:
                glas_first+=1
    for word in text1:
        x=0
        for el in word:
            if el in glas:
                x+=1
        if x!=glas_first:
            return 'Пам парам'
    return 'Парам пам-пам'


text1=input().split()
#text1='пара-ра-рам рам-пам-папам па-ра-па-да'.split()
print(pararam(text1))