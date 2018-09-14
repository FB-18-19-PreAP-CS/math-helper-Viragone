
 



class Fraction():
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def flipandsimplify(self):
        helper = self.numerator
        self.numerator = self.denominator
        self.denominator = helper
        if type(self.denominator) == Radical:
            self.numerator = self.numerator * self.denominator.radicand()
            self.denominator = self.denominator.square() 
    def __str__(self):
        if denominator == 0:
            print("undefined (-)")
        if numerator == denominator:
            print("1")
        elif denominator == 1:
            print(numerator)
        else:
            print(str(numerator) + "/" + str(denominator))
    def numerator(self):
        return self.numerator
    def denominator(self):
        return self.denominator
    
class Radical():
    def __init__(self, radicand):
        self.radicand = radicand
    def radicand(self):
        return radicand
    def square(self):
        return radicand
    def __str__(self):
        print("root(" + randicand + ")")
        
        
        




def unitCircle(trigOp, numer, denom):
    '''returns the value (in simplest radical form and decimal if
       numer and denom correspond with points on the unit circle, just
       decimal if not) of
       
             (numer * pi)
       trigOp(----------)
             (  denom   )                                          '''
    
    referenceAngles = [0, 30, 45, 60, 90]
    trigOperations = ["sine", "sin", "cosine", "cos", "tangent", "tan", "cosecant", "csc", "secant", "sec", "cotangent", "tan"]
    degAngle = ((numer//1) * 180) // (denom//1)
    if degAngle > 360 or degAngle < 0 or numer < 0 or denom <= 0:
        raise ValueError("point is not on the unit circle.")
    if trigOp not in trigOperations:
        raise ValueError("not a valid trigonometric operation.")
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
    if degAngle in referenceAngles:
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
            answerDecimal = 1.0
            if trigOp == "cosecant" or trigOp == "csc":
                answerRadical = answerRadical.flip()
                answerDecimal = 1.0
        else:
            radians = math.radians(referenceAngle)
            answerDecimal = (((math.sin(radians)) * 100) % 1) / 100
            if trigOp == "cosecant" or trigOp == "csc":
                answerDecimal = (((1 / answerDecimal) * 100) % 1) / 100
    elif trigOp == "cosine" or trigOp == "cos" or trigOp == "secant" or trigOp == "sec":
        if referenceAngle == 0:
            answerRadical = Fraction(1, 1)
            answerDecimal = 1.0
            if trigOp == "secant" or trigOp == "sec":
                answerRadical = answerRadical.flip()
                answerDecimal = 1.0
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
            answerRadical = Fraction(1, 1)
            answerDecimal = 1.0
            if trigOp == "secant" or trigOp == "sec":
                answerRadical = answerRadical.flip()
                answerDecimal = 1.0
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
        
        
    
    
    
    
    
    
    
    
    
         
        
       