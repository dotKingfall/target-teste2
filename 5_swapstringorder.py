def main():
    txt = input("Write the text which shall be reversed\n> ")
    print(txt[::-1]) ## Invert string order
    print("or even...")
    
    anthtxt = ""
    for c in range(len(txt)-1, -1, -1):
        anthtxt += txt[c]
    
    print(anthtxt)
    return True
    
main()