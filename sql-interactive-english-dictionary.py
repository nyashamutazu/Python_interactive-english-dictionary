import mysql.connector
import difflib 

con = mysql.connector.connect(
    user = 'ardit700_student',
    password ='ardit700_student',
    host = '108.167.140.122',
    database = 'ardit700_pm1database'
)

cusor = con.cursor()





class Find():

    def __init__ (self):
        pass

    def findRequest(self):
        while True: 
            try:
                searched_query = str(input('Search for definition: '))
            except:
                print('Sorry, I did not get that')
            else:
                query = cusor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' AND length(Experssion) > 1" % searched_query)

                data = cusor.fetchall()

            
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
        
        for x, y in result: 
            print(y)
    else: 
        print(result)
lookup()
