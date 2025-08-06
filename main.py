# bin/Python3.9
# Author : Muhammet Burak GOLEC

try:    
    import get
    import api
    import Char_change
    import getopt
    import sys
    import text_convert

except ImportError:    
    print("İmport Error")

def main():

    #url = str(input("Site : "))
    
    url = "https://tr.wikipedia.org/wiki/MOSFET"

    #print(url)

    value = str(get.get_in(url))

    value = str(Char_change.cx(value))
       
    value = get.convert(value) 

    value = api.conv(value)

    print(value)

def test():
    
    text_test="işİ ĞüçÜ"

    if Char_change.cx(text_test)=="isI GucU":
        return True

    else:
        return False

if __name__=="__main__":
    
    if test() == True:
        main()

    else:
        print("Test Error")


