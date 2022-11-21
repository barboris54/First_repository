def slicer(tupple,n):
    if n in tupple:
        if tupple.count(n) > 1:
            b =tupple.index(n)
            c = tupple.index(n,b+1)
            return tupple[b:c+1]
        else:
            f = tupple.index(n)
            return tupple[f:]

    else:
        return ()
print(slicer((1,8,3,4,8,8,9,2),8))
print(slicer((1,2,3),8))
print(slicer((1,2,8,5,1,2,9),8))