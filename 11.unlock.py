def unlock(code,unlockcode):

    count=0

    while(code>0):

        a=code%10
        b=unlockcode%10

        count+=min(abs(a-b),10-abs(a-b))

        code=code//10
        unlockcode=unlockcode//10
    return count

code = 28756;
unlockcode = 98234

print(unlock(code,unlockcode))

print(unlock(1919,0000))
