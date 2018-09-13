
 







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
    
    
    
    
    
    
    
    
    
    
         
        
       