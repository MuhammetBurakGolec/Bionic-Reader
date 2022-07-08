from queue import PriorityQueue


try:
    import text_convert

except  ImportError:
    print("Import Error --char_change--")


def cx(text):
    for x in range(len(text)):
        if text[x] == 'ı':
            #ID 1
            pass

        if text[x] == 'İ':
            #ID 2
            pass

        if text[x].lower == 'ö':
            #ID 3
            pass

        if text[x].lower == 'ç':
            #ID 4
            pass

        if text[x] == '':
            #ID 5
            pass
            


    text = text.replace('ı', 'i')
    text = text.replace('İ', 'I')
    text = text.replace('ö', 'o')
    text = text.replace('Ö', 'O')
    text = text.replace('ç', 'c')
    text = text.replace('Ç', 'C')
    text = text.replace('ü', 'u')
    text = text.replace('Ü', 'U')
    text = text.replace('ş', 's')
    text = text.replace('Ş', 'S')
    text = text.replace('ğ', 'g')
    text = text.replace('Ğ', 'G')
    
    return text