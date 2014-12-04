# -*- coding: utf-8 -*-
#!/usr/bin/python


################################################
####### THE CHEATSHEET OF LETTER CODES: ########


# ś (si) = \xc5\x9b
#ą = \xc4\x85
# ź (zi)
#ć (ci) = \xc4\x87
#dź (dzi) =\xc5\xba


################################################
####### THE FUNCTION KASHUBY: ##################

def kashuby(x):
    #the word is turned into an array
    a = list(x)
# BELOW : control print; to be enabled when a check is needed
#    print a
    l = len(a)

#this checks whether a certain element of the array doesn't belong to the alphabet.
#if it's so, it increments z.
    z = 0
    for i in range(0,l):
        if(a[i].isalpha()==False):
            z += 1

#if z>0, there are special signs so we need to have each letter after a space.
#this ensures that the strange signs don't get messed up as they would with list(x)
    if(z>0):
        x = raw_input("Proszę podaj słowo raz jeszcze, po każdym znaku umieszczając spację: \n")
        a = x.split(" ")
#BELOW: a control print of the special array
#        print a

    l = len(a)

#a standard, brute force and sloppy way of exchanging one-letter Pols into Kashs

    for i in range(0,l):
        if(a[i]=="ś"):
            a[i] = "s"
        elif(a[i]=="\xc4\x87"):
            a[i] = "c"
        elif(a[i]=="\xc5\xba"):
            a[i] = "z"

#BELOW: a control print
#    print "the length is %d" % (l)


#a standard, brute force and sloppy way of exchanging two-letter Pols into Kashs
#the for loop must be therefore restricted
    for i in range(0,l-1):

        if(a[i]+a[i+1]=="si"):
            a[i+1] = ""
        elif(a[i]+a[i+1]=="ci"):
            a[i+1] = ""
        elif(a[i]+a[i+1]=="zi"):
            a[i+1] = ""
        elif((a[i]+a[i+1]=="ro") | (a[i]+a[i+1]=="ró")):
            a[i] = "a"
            a[i+1] = "r"
    print "".join(a)


################################################
####### MAIN FUNCTION: ########################
x = raw_input("Daj mi słowo:  ")
kashuby(x)
