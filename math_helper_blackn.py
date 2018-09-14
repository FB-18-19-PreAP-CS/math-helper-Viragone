
 



class Fraction():
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def flip(self):
        helper = self.numerator
        self.numerator = self.denominator
        self.denominator = helper
    def __str__(self):
        print(str(numerator) + "/" + str(denominator))
        
        




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
    if degAngle <= 90:
        referenceAngle = degAngle
    elif degAngle <= 180:
        referenceAngle = 180 - degAngle
    elif degAngle <= 270:
        referenceAngle = degAngle - 180
    elif degAngle <= 360:
        referenceAngle = 360 - degAngle
    if degAngle > 360 or degAngle < 0 or referenceAngle not in referenceAngles:
        raise ValueError("point is not on the unit circle.")
    if trigOp not in trigOperations:
        raise ValueError("not a valid trigonometric operation.")
    if degAngle in referenceAngles:
            radicalMode = True
    if trigOp == "sine" or trigOp == "sin":
        if referenceAngle == 0:
            answerRadical = "0"
            answerDecimal = 0
        if referenceAngle == 30:
            answerRadical = "1/2"
            answerDecimal = 0.5
        if referenceAngle == 45:
            answerRadical = "sqrt(2)/2"
            answerDecimal = 0.707
        if referenceAngle 
    
    
    
    
    
    
    
    
    
    
         
        
       