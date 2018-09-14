
 



class Fraction():
    def __init__(self, num, den):
        self.num = num
        self.den = den
    def flip(self):
        helper = str(self.numerator)
        self.num = self.den
        self.den = helper
        if type(self.den) == Radical:
            if self.num == 1:
                self.num = str(self.den.rad())
            else:  
                self.num = self.num +  str(self.den.rad())
            self.den = self.den.square() 
    def __str__(self):
        if self.den == 0:
            return "undefined (-)"
        if self.num == self.den:
            return "1"
        elif self.den == 1:
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
             (  denom   )                                          '''
    
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
            answerRadical = Fraction(1, 2)
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
            answerDecimal = (((math.sin(radians)) * 100) % 1) / 100
            if trigOp == "cosecant" or trigOp == "csc":
                answerDecimal = (((1 / answerDecimal) * 100) % 1) / 100
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
            answerDecimal = (((math.cos(radians)) * 1000) % 1) / 1000
            if trigOp == "secant" or trigOp == "sec":
                answerDecimal = (((1 / answerDecimal) * 1000) % 1) / 1000
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
            answerDecimal = (((math.tan(radians)) * 1000) % 1) / 1000
            if trigOp == "cotangent" or trigOp == "cot":
                answerDecimal = (((1 / answerDecimal) * 1000) % 1) / 1000
                
    if radicalMode == True:
        if negativeMode == True:
            answer = "decimal: -" + str(answerDecimal) + "     radical: -" + str(answerRadical)
            return answer
        else:
            answer = "decimal: " + str(answerDecimal) + "     radical: " + str(answerRadical)
            return answer
    else:
        if negativeMode == True:
            answer = "decimal: -" + str(answerDecimal)
            return answer
        else:
            answer = "decimal: " + str(answerDecimal)
            return answer
            
            
        
        
    
    
    
    
    
    
    
    
    
         
        
       