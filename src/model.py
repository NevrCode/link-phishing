import joblib
import re




class Model : 
    url = ''
    
    def __init__(self) -> None:
        self.model = joblib.load('model/random_forest_model.pkl')
        print(self.model)



    def setURL(self, url) :
        self.url = url

    def getFeature(self) :
        return [self.numDots(),
                1,
                2,
                self.urlLen(), 
                self.numTilde(), 
                4,
                self.numAnd(), 
                self.numHash(), 
                2,
                3,
                5,
                self.numQuery(), 
                3
                ]
    def predicts(self,x) :
        return self.model.predict(x)


    def numDots(self) :
        return self.url.count('.')
    
    def urlLen(self) :
        return len(self.url)
    
    def numTilde(self) :
        return  self.url.count('~')  
     
    def numAnd(self) :
        return self.url.count('&')
    
    def numHash(self) :
        return self.url.count('#')
    
    def numQuery(self) :
        return (len(self.url.split("?")[1]) if len(self.url.split("?"))>= 2 else 0)
    
    def numSubdomain(self) :
        return len(self.url.split("//")[1].split('.')[0])
    







model = Model()

model.setURL('https://www.google.com/search?q=query+')
dot = model.numSubdomain()



print(dot)

