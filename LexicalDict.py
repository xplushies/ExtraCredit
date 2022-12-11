import re
#from _typeshed import Self
class Lex:
    lexList = []

    

    lexList.insert(0, "start")
    lexList.insert(1, "when")  #if statment
    lexList.insert(2, "con")  #while statement
    lexList.insert(3, "block")  #block statment
    lexList.insert(4, "as_")  #assignemt statement

    lexList.insert(5, "expr")  #expression
    lexList.insert(6, "term")  #term
    lexList.insert(7, "factor")  #factor

    lexList.insert(8, "bool_expr")  #boolean expression
    lexList.insert(9, "boolAnd")  #boolean and
    lexList.insert(10, "boolEqu")  #boolean equal to
    lexList.insert(11, "boolRel")  #boolean relation operation

    lexList.insert(12, "{")  #start
    lexList.insert(13, "}")  #end

    lexList.insert(14, "(")  #parenR bracket
    lexList.insert(15, ")")  #parenL bracket
    lexList.insert(16, "[")  #squareR bracket
    lexList.insert(17, "]")  #squareL bracket

    lexList.insert(18, "/")  #division
    lexList.insert(19, "%")  #modulous
    lexList.insert(20, "*")  #multiple
    lexList.insert(21, "+")  #addition
    lexList.insert(22, "-")  #subtraction

    lexList.insert(23, "=")  #assignment
    lexList.insert(24, "<")  #lessThan sign
    lexList.insert(25, ">")  #greaterThan sign
    lexList.insert(26, "<=") #greaterThanEqualTo
    lexList.insert(27, ">=") #greaterThanEqualTo
    lexList.insert(28, "==") #equalTo
    lexList.insert(29, "!=") #doesNotEqual

    lexList.insert(30, ":")   #colen
    lexList.insert(31, ";")   #end of stmt
    lexList.insert(32, "@")   #1 byte memory suffix
    lexList.insert(33, "#")   #2 byte memory suffix
    lexList.insert(34, "$")   #3 byte memory suffix
    lexList.insert(35, "^")   #4 byte memory suffix
    lexList.insert(36, "&")   #and
    lexList.insert(37, "|")   #or
    lexList.insert(38, "\\")  #escape character
    lexList.insert(39, ",")   #comma
    lexList.insert(40, "else")#else
    #lexList.insert(41, "<:")  #single line comment beginning
    #lexList.insert(42, ":>")  #single line comment end
    #lexList.insert(43, "<<:") #multi-line comment beginning
    #lexList.insert(44, ":>>") #multi-line comment end


    lexList.insert(50, " ")  #space

class error():
    error = ("There is a Lexical error here.")

class varName:
    varPattern = re.compile(r"\b\w{6,8}\b")

#natiral_literal: whole numbers w/out decimals
class natNum:
    numPattern = re.compile(r"(\d)+[@#$^]*")

#decimals/fractions
class realNum:
    numPattern = re.compile(r"((\d)*[\.])?(\d)+[@#$^]*")

class bool:
    true = "true"
    false = "false"
    boolTypes = [true, false]

class char:
    charPattern = re.compile(r"\'[a-zA-Z0-9]\'")

class string:
    stringPattern = re.compile(r"\"[a-zA-Z0-9]+\"")

class LexAnalyzer:

    def toList(file):
        fl= open(file).read().split()
        return fl

    numErrors = 0
    lexCount = 0 #total lexemes, excluding comments
    def analyzer(file):
        fl = LexAnalyzer.toList(file)
        current = 0 #current int index of token list
        length = len(fl)
        lexCount = 0 #total lexemes, excluding comments
        #accounts for single line comments
        while (current < length):
            if fl[current] != "<:" and fl[current] != "<<:":
                LexAnalyzer.checkLex(fl[current])
                LexAnalyzer.fl2.append(fl[current])
                current +=1
            elif fl[current] == "<:":
                current += 1 #skip
                while (fl[current] != ":>"):
                    current += 1 #skip
                if (fl[current] == ":>"):
                    current += 1 #skip
                    #if a single line comment doesn't end with :>>, lex error and break loop
                else:
                    error()
                    break
            elif fl[current] == "<<:":
                current += 1 #skip
                while (fl[current] != ":>>"):
                    current += 1 #skip
                if (fl[current] == ":>>"):
                    current += 1 #skip
                    #if a mult line comment doesn't end with :>>, lex error and break loop
                else:
                    error()
                    break


        #returns num of errors in the file and is grammatically correct        
        if LexAnalyzer.numErrors == 1:
            print("There was " + str(LexAnalyzer.numErrors) + " lexical error in the code.")
        else:
            print("There were " + str(LexAnalyzer.numErrors) + " lexical errors in the code.")

    #List of lexemes without comments
    fl2 = []
    #corresponding list of lexeme type attribute
    typeList = []

    #helper method for analyzer
    def checkLex(token):
        if token in Lex.lexList:
            print(token + " is a lexeme.")
            if token == "=":
                LexAnalyzer.typeList.append("asig")
                LexAnalyzer.lexCount += 1
            elif token == ("<" or "<=" or ">" or ">=" or "==" or "!="):
                LexAnalyzer.typeList.append("boolOp")
                LexAnalyzer.lexCount += 1
            elif token == ("+" or "-" or "*" or "/" or "%"):
                LexAnalyzer.typeList.append("mathOp")
                LexAnalyzer.lexCount += 1
            elif token == ("&" or "|"):
                LexAnalyzer.typeList.append("logicOp")
                LexAnalyzer.lexCount += 1
            elif token == ("@" or "#" or "$" or "^"):
                LexAnalyzer.typeList.append("memorySuffix")
                LexAnalyzer.lexCount += 1
            elif token == ("(" or ")" or "{" or "}" or "[" or "]"):
                LexAnalyzer.typeList.append("parenthesis")
                LexAnalyzer.lexCount += 1
            elif token == (";" or "," or ":" or "."):
                LexAnalyzer.typeList.append("punctuation")
                LexAnalyzer.lexCount += 1
            elif token == ("else"):
                LexAnalyzer.typeList.append("else")
                LexAnalyzer.lexCount += 1
            elif token == (" "):
                LexAnalyzer.typeList.append("space")
                LexAnalyzer.lexCount += 1
            elif token == ("\\"):
                LexAnalyzer.typeList.append("escape")
                LexAnalyzer.lexCount += 1
            elif token == ("\""):
                LexAnalyzer.typeList.append("string")
                LexAnalyzer.lexCount += 1
            elif token == ("\'"):
                LexAnalyzer.typeList.append("char")
                LexAnalyzer.lexCount += 1
            elif token == ("true" or "false"):
                LexAnalyzer.typeList.append("bool")
                LexAnalyzer.lexCount += 1
            elif token == ("if" or "when" or "con" or "block" or "as_"):
                LexAnalyzer.typeList.append("keyword")
                LexAnalyzer.lexCount += 1
            else:
                LexAnalyzer.typeList.append("undefined type")
                LexAnalyzer.lexCount += 1
            #LexAnalyzer.typeList.append("undefined type")
            #LexAnalyzer.lexCount += 1
        elif natNum.numPattern.fullmatch(token):
            print(token + " is a natNum lexeme.")
            LexAnalyzer.typeList.append("natNum")
            LexAnalyzer.lexCount += 1
        elif realNum.numPattern.fullmatch(token):
            print(token + " is a realNum lexeme.")
            LexAnalyzer.typeList.append("realNum")
            LexAnalyzer.lexCount += 1
        elif varName.varPattern.fullmatch(token):
            print(token + " is a varName lexeme.")
            LexAnalyzer.typeList.append("varName")
            LexAnalyzer.lexCount += 1
        elif string.stringPattern.fullmatch(token):
            print(token + " is a string lexeme.")
            LexAnalyzer.typeList.append("string")
            LexAnalyzer.lexCount += 1
        elif char.charPattern.fullmatch(token):
            print(token + " is a char lexeme.")
            LexAnalyzer.typeList.append("char")
            LexAnalyzer.lexCount += 1
        else:
            print(token + " is not a lexeme, so this is a lexical error.")
            LexAnalyzer.numErrors += 1
            LexAnalyzer.typeList.append("undefined")

    def printTypeList():
        print(LexAnalyzer.typeList)

    def printReadList():
        print(LexAnalyzer.fl2)
        

    
    