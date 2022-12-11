import LexicalDict

class Token():

    #constructor for token
    def __init__(self, tokens:list(str)) -> None:
        self.tokens = tokens 
        self.type = None # str for token type
        self.current = 0 # int for token code
        self.currentToken = tokens[self.current]

    def getNextToken(self):
        if self.current < len[self.tokens]:
            self.current += 1

        self.currentToken = self.tokens[self.current]

    def toList(file):
        fl= open(file).read().split()
        return fl

    typeList = LexicalDict.LexAnalyzer.typeList

    def sortLexTypes(file):
        fl = Token.toList(file)
        for i in fl:
            if i in LexicalDict.Lex.lexList:
                Token.typeList.append(LexicalDict.Lex.lexList.index(i))
            else:
                Token.typeList.append(0)


    def error(self):
        print("There is a syntax error in the code. ")

    #<start> --> <poi>
    def start(self):
        self.poi()
    
    def poi(self):
        #<poi> -->  <when> | <during> | <as_> | <block> 
        if self.currentToken == "when": #when/if 
            self.when()
        elif self.currentToken == "con": #con/while
            self.con()
        elif self.currentToken == "asig":  #asig
            self.as_()
        elif self.currentToken == '(':   #block
            self.block()
        else:
            self.error()
    

