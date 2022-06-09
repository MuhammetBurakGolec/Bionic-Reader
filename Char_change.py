def cx(text):
   
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