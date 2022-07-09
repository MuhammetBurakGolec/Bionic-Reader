try:
    import text_convert


except  ImportError:
    print("Import Error --char_change--")


def cx(text):
    for x in range(len(text)+1):
        if text[x] == 'ı':
            #ID 1
            text_convert.matrix_append(x,1)

        if text[x] == 'İ':
            #ID 2
            text_convert.matrix_append(x,2)
            
        if text[x].lower == 'ö':
            #ID 3
            text_convert.matrix_append(x,3)


        if text[x].lower == 'ç':
            #ID 4
            text_convert.matrix_append(x,4)


        if text[x] == 'ü':
            #ID 5
            text_convert.matrix_append(x,5)


        if text[x] == 'ş':
            #ID 6
            text_convert.matrix_append(x,6)


        if text[x] == 'ğ':
            #ID 7
            text_convert.matrix_append(x,7)
            


    text = text.replace('ı', 'i')
    text = text.replace('İ', 'I')
    text = text.replace('ö', 'o')
    text = text.replace('Ö', 'O')
    text = text.replace('ç', 'c')
    text = text.replace('Ç', 'C')
    text = text.replace('ü', 'u')
    text = text.replace('ş', 's')
    text = text.replace('Ü', 'U')
    text = text.replace('Ş', 'S')
    text = text.replace('ğ', 'g')
    text = text.replace('Ğ', 'G')
    
    return text