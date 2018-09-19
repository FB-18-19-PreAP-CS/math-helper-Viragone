import math
 



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
                    return Fraction(Radical(str(self.num1)), "1")
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
    def __init__(self, radicand):
        self.radicand = radicand
    def rad(self):
        return self.radicand
    def square(self):
        return self.radicand
    def __str__(self):
        return "root(" + str(self.radicand) + ")"
        
        
        




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
            answerRadical = Fraction(Radical(2), 2)
            answerDecimal = 0.707
            if trigOp == "cosecant" or trigOp == "csc":
                answerRadical = answerRadical.flip()
                answerDecimal = 1.414
        elif referenceAngle == 60:
            answerRadical = Fraction(Radical(3), 2)
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
            answerRadical = Fraction(Radical(3), 2) 
            answerDecimal = 0.866
            if trigOp == "secant" or trigOp == "sec":
                answerRadical = answerRadical.flip()
                answerDecimal = 1.155
        elif referenceAngle == 45:
            answerRadical = Fraction(Radical(2), 2)
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
            answerRadical = Fraction(1, Radical(3)) 
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
            answerRadical = Fraction(Radical(3), 1)
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
       
       >>> SAS(2,3,30)
               
    '''
    
    angleRadians = math.radians(angle)
    area = ((((side1 * side2) // 2 * math.sin(angleRadians) * 1000) // 1) / 1000)
    return area



    
       
        
        
def main():
    pass
    
if __name__ == "__main__":
    #main()
    import doctest
    doctest.testmod()
            
            
        
        
    
    
    
    
    
    
    
    
    
         
        
       