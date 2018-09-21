import math
from time import *
 



class Fraction():
    def __init__(self, num, den):
        self.num = num
        self.den = den
        if type(self.den) == Radical:
            if self.num == 1:
                self.num = Radical(self.den.rad())
            else:  
                self.num = self.num + "root(" + str(self.den.rad()) + ")"
            self.den = self.den.square()
    def flip(self):
        helper = self.num
        self.num1 = str(self.den)
        self.den1 = helper
        if type(self.den1) == Radical:
            if self.num1 == "1":
                self.num = "root(" + str(self.den1.rad()) +")"
                self.den = self.den1.square()
                return Fraction(self.num, self.den)
            else:  
                self.num = self.num1 +  "root(" + str(self.den1.rad()) + ")"
                self.den = self.den1.square()
                if str(self.num1) == str(self.den1.square()):
                    return Fraction(Radical(1, str(self.num1)), "1")
                return Fraction(self.num, self.den)
        return Fraction(self.num1, self.den1)
    def __str__(self):
        if self.den == 0:
            return "undefined (-)"
        if self.num == self.den:
            return "1"
        elif self.den == "1" or self.den == 1:
            return str(self.num)
        else:
            return str(self.num) + "/" + str(self.den)
    def numerator(self):
        return self.num
    def denominator(self):
        return self.den
    
class Radical():
    def __init__(self, outsideRadical, radicand):
        self.radicand = radicand
        self.factors = []
        self.outsideFactor = outsideRadical
        if self.outsideFactor == 1:
            self.simplified = False
        else:
            self.simplified = True
    def rad(self):
        return self.radicand
    def square(self):
        return self.radicand
    def __str__(self):
        if self.simplified == False:
            return "root(" + str(self.radicand) + ")"
        else:
            return str(self.outsideFactor) + "root(" + str(self.radicand) + ")"
            
def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def simplifyToPrimes(x):
    factorList = []
    for i in range(2, x):
        if x % i == 0:
            factorList.append(i)
            x = math.floor(x / i)
            if isPrime(x):
                factorList.append(x)
    return factorList
            
        
        




def unitCircle(trigOp, numer, denom):
    '''returns the value (in simplest radical form and decimal if
       numer and denom correspond with points on the unit circle, just
       decimal if not) of
       
             (numer * pi)
       trigOp(----------)
             (  denom   )
             
       
       >>> unitCircle("cos", 5,6)
       'decimal: -0.866     radical: -root(3)/2'
       
       >>> unitCircle("sec", 5, 6)
       'decimal: -1.155     radical: -2root(3)/3'
       
       >>> unitCircle("csc",2,1)
       'decimal: undefined (-)     radical: undefined (-)'
       
       >>> unitCircle("csc",1,4)
       'decimal: 1.414     radical: root(2)'
       
       >>> unitCircle("sin",1,9)
       'decimal: 0.342'
       
    '''
    numer = int(numer)
    denom = int(denom)
    referenceAngles = [0, 30, 45, 60, 90]
    trigOperations = ["sine", "sin", "cosine", "cos", "tangent", "tan", "cosecant", "csc", "secant", "sec", "cotangent", "cot"]
    degAngle = ((numer//1) * 180) // (denom//1)
    trigOp = trigOp.lower()
    if degAngle > 360 or degAngle < 0 or numer < 0 or denom <= 0:
        raise ValueError("point is not on the unit circle.")
    if trigOp not in trigOperations:
        raise ValueError("not a valid trigonometric operation.")
    negativeMode = False
    if degAngle <= 90:
        referenceAngle = degAngle
    elif degAngle <= 180:
        referenceAngle = 180 - degAngle
        if trigOp == "cosine" or trigOp == "cos" or trigOp == "tangent"  or trigOp == "tan" or trigOp == "secant" or trigOp == "sec" or trigOp == "cotangent" or trigOp == "cot":
            negativeMode = True
    elif degAngle <= 270:
        if trigOp == "cosine" or trigOp == "cos" or trigOp == "sine"  or trigOp == "sin" or trigOp == "secant" or trigOp == "sec" or trigOp == "cosecant" or trigOp == "csc":
            negativeMode = True
        referenceAngle = degAngle - 180
    elif degAngle <= 360:
        if trigOp == "sine" or trigOp == "sin" or trigOp == "tangent"  or trigOp == "tan" or trigOp == "cosecant" or trigOp == "csc" or trigOp == "cotangent" or trigOp == "cot":
            negativeMode = True
        referenceAngle = 360 - degAngle
    if referenceAngle in referenceAngles:
        radicalMode = True
    else:
        radicalMode = False
    if trigOp == "sine" or trigOp == "sin" or trigOp == "cosecant" or trigOp == "csc":
        if referenceAngle == 0:
            answerRadical = Fraction(0, 1)
            answerDecimal = 0
            if trigOp == "cosecant" or trigOp == "csc":
                answerRadical = answerRadical.flip()
                answerDecimal = "undefined (-)"
        elif referenceAngle == 30:
            answerRadical = Fraction(1,2)
            answerDecimal = 0.5
            if trigOp == "cosecant" or trigOp == "csc":
                answerRadical = answerRadical.flip()
                answerDecimal = 2
        elif referenceAngle == 45:
            answerRadical = Fraction(Radical(1, 2), 2)
            answerDecimal = 0.707
            if trigOp == "cosecant" or trigOp == "csc":
                answerRadical = answerRadical.flip()
                answerDecimal = 1.414
        elif referenceAngle == 60:
            answerRadical = Fraction(Radical(1, 3), 2)
            answerDecimal = 0.866
            if trigOp == "cosecant" or trigOp == "csc":
                answerRadical = answerRadical.flip()
                answerDecimal = 1.155
        elif referenceAngle == 90:
            answerRadical = Fraction(1,1)
            answerDecimal = 1
            if trigOp == "cosecant" or trigOp == "csc":
                answerRadical = answerRadical.flip()
                answerDecimal = 1
        else:
            radians = math.radians(referenceAngle)
            answerDecimal = (((math.sin(radians)) * 1000) // 1) / 1000
            if trigOp == "cosecant" or trigOp == "csc":
                answerDecimal = (((1 / answerDecimal) * 1000) // 1) / 1000
    elif trigOp == "cosine" or trigOp == "cos" or trigOp == "secant" or trigOp == "sec":
        if referenceAngle == 0:
            answerRadical = Fraction(1, 1)
            answerDecimal = 1
            if trigOp == "secant" or trigOp == "sec":
                answerRadical = answerRadical.flip()
                answerDecimal = 1
        elif referenceAngle == 30:
            answerRadical = Fraction(Radical(1, 3), 2) 
            answerDecimal = 0.866
            if trigOp == "secant" or trigOp == "sec":
                answerRadical = answerRadical.flip()
                answerDecimal = 1.155
        elif referenceAngle == 45:
            answerRadical = Fraction(Radical(1, 2), 2)
            answerDecimal = 0.707
            if trigOp == "secant" or trigOp == "sec":
                answerRadical = answerRadical.flip()
                answerDecimal = 1.414
        elif referenceAngle == 60:
            answerRadical = Fraction(1, 2)
            answerDecimal = 0.5
            if trigOp == "secant" or trigOp == "sec":
                answerRadical = answerRadical.flip()
                answerDecimal = 2
        elif referenceAngle == 90:
            answerRadical = Fraction(0, 1)
            answerDecimal = 0
            if trigOp == "secant" or trigOp == "sec":
                answerRadical = answerRadical.flip()
                answerDecimal = "undefined (-)"
        else:
            radians = math.radians(referenceAngle)
            answerDecimal = (((math.cos(radians)) * 1000) // 1) / 1000
            if trigOp == "secant" or trigOp == "sec":
                answerDecimal = (((1 / answerDecimal) * 1000) // 1) / 1000
    else:
        if referenceAngle == 0:
            answerRadical = Fraction(0, 1)
            answerDecimal = 0
            if trigOp == "cotangent" or trigOp == "cot":
                answerRadical = answerRadical.flip()
                answerDecimal = "undefined (-)"
        elif referenceAngle == 30:
            answerRadical = Fraction(1, Radical(1, 3)) 
            answerDecimal = 0.577
            if trigOp == "cotangent" or trigOp == "cot":
                answerRadical = answerRadical.flip()
                answerDecimal = 1.732
        elif referenceAngle == 45:
            answerRadical = Fraction(1,1)
            answerDecimal = 1
            if trigOp == "cotangent" or trigOp == "cot":
                answerRadical = answerRadical.flip()
                answerDecimal = 1
        elif referenceAngle == 60:
            answerRadical = Fraction(Radical(1, 3), 1)
            answerDecimal = 1.732
            if trigOp == "cotangent" or trigOp == "cot":
                answerRadical = answerRadical.flip()
                answerDecimal = 0.577
        elif referenceAngle == 90:
            answerRadical = Fraction(1,0)
            answerDecimal = "undefined (-)"
            if trigOp == "cotangent" or trigOp == "cot":
                answerRadical = answerRadical.flip()
                answerDecimal = 0
        else:
            radians = math.radians(referenceAngle)
            answerDecimal = (((math.tan(radians)) * 1000) // 1) / 1000
            if trigOp == "cotangent" or trigOp == "cot":
                answerDecimal = (((1 / answerDecimal) * 1000) // 1) / 1000
                
    if radicalMode == True:
        if negativeMode == True and str(answerDecimal) != "0" and str(answerDecimal) != "undefined (-)":
            answer = "decimal: -" + str(answerDecimal) + "     radical: -" + str(answerRadical)
            return answer
        else:
            answer = "decimal: " + str(answerDecimal) + "     radical: " + str(answerRadical)
            return answer
    else:
        if negativeMode == True and str(answerDecimal) != "0" and str(answerDecimal) != "undefined (-)" :
            answer = "decimal: -" + str(answerDecimal)
            return answer
        else:
            answer = "decimal: " + str(answerDecimal)
            return answer
        
def pointsToPointSlope(x1,y1,x2,y2):
    ''' returns, given two points, the equation of the line
        in point-slope form, the preferred linear equation
        form on the AP Calculus AB exam
        
        >>> pointsToPointSlope(0,0,0,0)
        'x = 0'
        
        >>> pointsToPointSlope(2,3,9,3)
        'y = 3'
        
        >>> pointsToPointSlope(2,3,9,4)
        'y - 3 = 1/7(x - 2)'
        
        >>> pointsToPointSlope(2,3.1,9,9.2)
        'y - 3.1 = 0.871(x - 2)'
        
        >>> pointsToPointSlope(1,2,6,12)
        'y - 2 = 2(x - 1)'
        
    '''
    if x2 - x1 == 0:
        x = x2
        return "x = " + str(x)
    elif y2 - y1 == 0:
        y = y1
        return "y = " + str(y)
    else:
        if type(x1) != int or type(y1) != int or type(x2) != int or type(y2) != int:
            m = (((((y2-y1)/(x2-x1)) * 1000) // 1) / 1000)
            return "y - " + str(y1) + " = " + str(m) + "(x - " + str(x1) + ")"
        else:
            mnumer = (y2-y1)
            mdenom = (x2-x1)
            if mnumer > mdenom:
                for i in range(2, mdenom + 1):
                    if mnumer % i == 0 and mdenom % i == 0:
                        mnumer = mnumer / i
                        mdenom = mdenom / i
            else:
                for i in range(2, mnumer + 1):
                    if mnumer % i == 0 and mdenom % i == 0:
                        mnumer = mnumer / i
                        mdenom = mdenom / i
                        
            if mdenom == 1:
                finalM =  int (mnumer // mdenom) // 1
                return "y - " + str(y1) + " = " + str(finalM) + "(x - " + str(x1) + ")"
            
            else:
                return "y - " + str(y1) + " = " + str(mnumer) + "/" + str(mdenom) + "(x - " + str(x1) + ")"
            
def SAS(side1,side2,angle):
    '''returns (to the thousandths place) the area of a
       triangle, given the lengths of two sides and the angle
       (in degrees) at the intersection of the two sides
       
       >>> SAS(6,6,30)
       '9'
       
       >>> SAS(5,12,90)
       '30'
       
       >>> SAS(27,13,125)
       '143.351'
       
       >>> SAS(68,41,78)
       '1363.537'
       
       >>> SAS(8,15,90)
       '60'
       
    '''
    
    angleRadians = math.radians(angle)
    area = (((((side1 * side2) // 2 * math.sin(angleRadians) * 1000) // 1) / 1000))
    if math.ceil(area) - area <= .1:
        area = math.ceil(area)
    return str(area)



def simplifyRadical(x):
    '''returns (in simplest radical form) the simplified
       form of sqrt(x)
       
       >>> simplifyRadical(16)
       '4'
       
       >>> simplifyRadical(361)
       '19'
       
       >>> simplifyRadical(14)
       'root(14)'
       
       >>> simplifyRadical(48)
       '4root(3)'
       
       >>> simplifyRadical(104)
       '2root(26)'
       
    '''
    if math.sqrt(x) % 1 == 0:
        return str(math.floor(math.sqrt(x)))
    if isPrime(x):
        return Radical(1,x)
    outsideRadical = 1
    insideRadical = 1
    radic = Radical(1, x)
    for i in range(3):
        for i in range(2, ((radic.radicand // 2)+1)):
            if radic.radicand % i == 0:
                if isPrime(i):
                    radic.factors.append(i)
                else:
                    for factor in simplifyToPrimes(i):
                        radic.factors.append(factor)
                radic.radicand = math.floor(radic.radicand / i)
                if isPrime(radic.radicand):
                    radic.factors.append(radic.radicand)
                    break
    radic.factors.sort() #sort function found on Stack Overflow at https://stackoverflow.com/questions/3426108/how-to-sort-a-list-numerically
    previousNumber = radic.factors[0]
    factorCount = 0
    factorCountList = []
    previousNumberList = []
    for i in radic.factors:
        if i == previousNumber:
            factorCount += 1
        else:
            if factorCount % 2 == 1:
                if factorCount == 1:
                    insideRadical *= previousNumber
                else:
                    outsideRadical *= (previousNumber * (factorCount // 2))
                    insideRadical *= previousNumber
                    
            else:
                outsideRadical *= (previousNumber * (factorCount // 2))
            previousNumber = i
            factorCountList.append(factorCount)
            previousNumberList.append(previousNumber)
            factorCount = 1
    factorCountList.append(factorCount)
    if factorCountList[len(factorCountList) -1] % 2 == 1:
        if factorCountList[len(factorCountList) -1] == 1:
            insideRadical *= previousNumberList[len(previousNumberList) -1]
        else:
            insideRadical *= previousNumberList[len(previousNumberList) -1]
            outsideRadical *= (previousNumberList[len(previousNumberList) -1] * (factorCountList[len(factorCountList) -1] // 2))
    else:
        outsideRadical *= (previousNumberList[len(previousNumberList) -1] * (factorCountList[len(factorCountList) -1] // 2))
    return str(Radical(outsideRadical, insideRadical))
                
            
        
    
    
            
    
            
            
def quadraticFormula(a,b,c):
    '''returns (to the thousandths place) the two roots (zeroes)
       of a given quadratic equation ax^2 + bx + c with inputs
       a, b, and c
       
       >>> quadraticFormula(1,5,6)
       'value 1: -2 or -2.0     value 2: -3 or -3.0'
       
       >>> quadraticFormula(1,-3,2)
       'value 1: 2 or 2.0     value 2: 1 or 1.0'
       
       >>> quadraticFormula(1,7,2)
       'value 1: -0.299 or (-7 + root(41)) / 2     value 2: -6.702 or (-7 - root(41)) / 2'
       
       >>> quadraticFormula(1,9,3)
       'value 1: -0.347 or (-9 + root(69)) / 2     value 2: -8.654 or (-9 - root(69)) / 2'
       
       >>> quadraticFormula(1.1,7.1,6.1)
       'value 1: -1.235     value 2: -6.576'
       

    '''
    a = float(a)
    b = float(b)
    c = float(c)
    radicalMode = False
    part1 = b * b
    part2 = 4 * a * c
    if float(part1 - part2) % 1 == 0:
        radicalMode = True
        discriminant = math.floor(b**2 - 4 * a * c)
        radicalString = simplifyRadical(discriminant)
    value1 = (((((-b + math.sqrt(b**2 - 4 * a * c)) / 2*a) * 1000) // 1) / 1000)
    if math.ceil(value1) - value1 <= .1:
        value1 = math.ceil(value1)
    value2 = (((((-b - math.sqrt(b**2 - 4 * a * c)) / 2*a) * 1000) // 1) / 1000)
    if math.ceil(value2) - value2 <= .1:
        value2 = math.ceil(value2)
    
    if radicalMode == False:
        answer = "value 1: " + str(value1) + "     value 2: " + str(value2)
        return answer
    else:
        
        if type(radicalString) != Radical:
            if len(radicalString) <= 4:
                if float(str(radicalString)) % 1 == 0:
                    radicalString = math.floor(float(radicalString))
                    answer1 = str((-b + radicalString) / (2 * a))
                    answer2 = str((-b - radicalString) / (2 * a))
                    return "value 1: " + str(value1) + " or " + answer1 +"     value 2: " + str(value2) + " or " + answer2
            
            
            
        answer1 = "(" + str(-b) + " + " + str(radicalString)  + ") / " + str(2 * a)
        answer2 = "(" + str(-b) + " - " + str(radicalString)  + ") / " + str(2 * a)
        return "value 1: " + str(value1) + " or " + answer1 +"     value 2: " + str(value2) + " or " + answer2
        
        
def getunitCircleValues():
    trig = ["sine", "sin", "cosine", "cos", "tangent", "tan", "cosecant", "csc", "secant", "sec", "cotangent", "cot"]
    useFunction = False
    useFunctionn = False
    useFunctiond = False
    while useFunctionn == False:
        print("Enter value n, as it appears on n * pi")
        print("                                ------")
        n = input("                                   d   ")
        if n == "s":
            return False
        try:
            numerator = int(n)
        except ValueError:
            print("Not an integer.")
            return True
        if numerator < 1 or numerator > 5:
            print("Invalid input.")
            return True
        else:
            useFunctionn = True
            while useFunctiond == False:
                print("Enter value d, as it appears on n * pi")
                print("                                ------")
                d = input("                                   d   ")
                if d == "s":
                    return False
                try:
                    denominator = int(d)
                except ValueError:
                    print("Not an integer.")
                    return True
                if (numerator * 180 / denominator) < 0 or (numerator * 180 / denominator) > 360:
                    print("Invalid input. Not on Unit Circle")
                    return True
                else:
                    useFunctiond = True
                    while useFunction == False:
                        operator = str(input("Enter the trig function you'd like to use: "))
                        if operator == "s":
                            return False
                        if operator not in trig:
                            print("Invalid input. Not a valid trig function.")
                            return True
                        else:
                            useFunction = True
                            numerator = int(numerator)
                            denominator = int(denominator)
                            return unitCircle(operator, numerator, denominator)
                        
def getQuadraticFormulaValues():
    useFunctiona = False
    useFunctionb = False
    useFunctionc = False
    while useFunctiona == False:
        a = input("Enter value a: ")
        if a == "s":
            return False
        try:
            a = float(a)
        except ValueError:
            print("Not a valid number.")
            return True
        if a == 0:
            print("Invalid input.")
            return True
        else:
            useFunctiona = True
            while useFunctionb == False:
                b = input("Enter value b: ")
                if b == "s":
                    return False
                try:
                    b = float(b)
                except ValueError:
                    print("Not a valid number.")
                    return True
                else:
                    useFunctionb = True
                    while useFunctionc == False:
                        c = input("Enter value c: ")
                        if c == "s":
                            return False
                        try:
                            b = float(b)
                        except ValueError:
                            print("Not a valid number.")
                            return True

                        else:
                            useFunctionc = True
                            return quadraticFormula(a,b,c)
                        
def getSASValues():
    useFunctiona = False
    useFunctionb = False
    useFunctionc = False
    while useFunctiona == False:
        a = input("Enter side a: ")
        if a == "s":
            return False
        try:
            a = float(a)
        except ValueError:
            print("Not a valid number.")
            return True
        if a <= 0:
            print("Invalid input.")
            return True
        else:
            useFunctiona = True
            while useFunctionb == False:
                b = input("Enter side b: ")
                if b == "s":
                    return False
                try:
                    b = float(b)
                except ValueError:
                    print("Not a valid number.")
                    return True
                if b <= 0:
                    print("Invalid input.")
                    return True
                else:
                    useFunctionb = True
                    while useFunctionc == False:
                        c = input("Enter angle c: ")
                        if c == "s":
                            return False
                        try:
                            c = float(c)
                        except ValueError:
                            print("Not a valid number.")
                            return True
                        if c <= 0 or c >= 360:
                            print("Invalid angle.")
                            return True
                        else:
                            useFunctionc = True
                            return SAS(a,b,c)
    
                        
def getSimplifyRadicalValues():
    useFunction = False
    while useFunction == False:
        radical = input("Enter a radical to be simplified: ")
        if radical == "s":
            return False
        try:
            radical = int(radical)
        except ValueError:
            print("Not an integer.")
            return True
        radical = int(radical)
        useFunction = True
        return simplifyRadical(radical)
    
    
def getPointsToPointSlopeValues():
    useFunctionx1 = False
    useFunctiony1 = False
    useFunctionx2 = False
    useFunctiony2 = False
    while useFunctionx1 == False:
        x1 = input("Enter x1: ")
        if x1 == "s":
            return False
        try:
            x1 = float(x1)
        except ValueError:
            print("Not a valid number.")
            return True
        else:
            useFunctionx1 = True
            while useFunctiony1 == False:
                y1 = input("Enter y1: ")
                if y1 == "s":
                    return False
                try:
                    y1 = float(y1)
                except ValueError:
                    print("Not a valid number.")
                    return True
                else:
                    useFunctiony1 = True
                    while useFunctionx2 == False:
                        x2 = input("Enter x2: ")
                        if x2 == "s":
                            return False
                        try:
                            x2 = float(x2)
                        except ValueError:
                            print("Not a valid number.")
                            return True
                        else:
                            useFunctionx2 = True
                            while useFunctiony2 == False:
                                y2 = input("Enter y2: ")
                                if y2 == "s":
                                    return False
                                try:
                                    y2 = float(y2)
                                except ValueError:
                                    print("Not a valid number.")
                                    return True
                                else:
                                    useFunctiony2 = True
                                    if x1 == x2 and y1 == y2:
                                        print("Cannot give the same point twice.")
                                        return True
                                    return pointsToPointSlope(x1,y1,x2,y2)
                            
    
                



        
        
def main():
    pass
    functional = True
    print("Hello, welcome to the Math Helper!")
    sleep(1)
    print("These are the mathematcal helpers supported by this program: ")
    sleep(.5)
    print("1. Unit Circle")
    print("2. Points to Point-Slope Form")
    print("3. Simplify A Radical")
    print("4. Solve For Roots of a Quadratic Funtion")
    print("5. Solve For Area of a Triangle Given A Side, Angle, and Side")
    sleep(.5)
    while functional:
        functionSelect = input("Which will you choose? (Press s at any time to quit)")
        if type(functionSelect) != str:
            print("Goodbye!")
            functional = False
        else:
            while int(functionSelect) > 5 and int(functionSelect) < 1:
                sleep(.5)
                functionSelect = int(input("Invalid Input. Which will you choose? (Press s at any time to quit) "))
    

    
if __name__ == "__main__":
    main()
    #import doctest
    #doctest.testmod()
            
            
        
        
    
    
    
    
    
    
    
    
    
         
        
       