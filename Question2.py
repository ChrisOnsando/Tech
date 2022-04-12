#Write a python function to find the length of the last word
def length_last_word(A):
    arr=A.split(' ')
    size=len(arr)
    if(size==1):
        return len(A)

    last_word=arr[-1]
    return last_word

A="HelloWorld"
print(length_last_word(A))