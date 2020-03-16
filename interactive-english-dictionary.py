import json
import difflib 

data = json.load(open("data.json"))

class Find():

    def __init__ (self):
        pass

    def findRequest(self):
        while True: 
            try:
                string = str(input('Search for a word you would like to translate: ')).lower()
            except:
                print('Sorry, I did not get that')
            else:
                value = difflib.get_close_matches(string, data.keys())
            
                if value:
                    newValueAnswer = str(input(f'Did you mean {value[0]}? yes(y) or no(n): ')).lower()
                    value = value[0]

                    if newValueAnswer[0] == 'y' and value:
                        if value in data:
                            return data[value]
                            break 
                        else:
                            pass
                    else: 
                        pass
                else: 
                    pass

                print('Sorry the word does not exist please double check')  


def lookup():
    result = Find().findRequest()

    if type(result) == list:
        print(f"Definition: ")   
        
        for x in result:
            print(x)
    else: 
        print(result)
lookup()
