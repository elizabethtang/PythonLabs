###############################################
# APS106  2022 - Lab 5 - Measurement Parser   #
###############################################

############################
# Part 1 - Email to Name   #
############################

def email_to_name(email):
    """
    (str) -> str
    
    Given a string with the format "first_name.last_name@domain.com",
    return a string "LAST_NAME,FIRST_NAME" where all the characters are upper
    case
    
    
    >>> email_to_name("anna.conda@mail.utoronto.ca")
    'CONDA,ANNA'
    """
    
    ## TODO: YOUR CODE HERE
  

    at=email.rfind('@')
    email=email[:at]
    period=email.rfind('.')
    first=email[:period]
    
    last=email[(period+1):]
    name=(last+','+first)
    name=name.upper()
    return name
###############################
# Part 2 - Count Measurements #
###############################

def count_measurements(s):
    """
    (str) -> int
 
    Given s, a string representation of comma separated site-measurement
    pairs, return the total number of measurements
 
    >>> count_measurements("B, 5.6, Control, 5.5, Db, 3.2")
    3
    
    >>> count_measurements("Control, 7.5")
    1
    """
    
    #TODO: YOUR CODE HERE

    s=s.split(', ')
    count =0
    
    for char in s :
        if char.isdigit():
            count +=1
        else :
            s.remove (char)
 
    length=len(s) 
            
    return length  
######################################
# Part 3 - Calculate Site Average    #
######################################

def calc_site_average(measurements, site):
    """
    (str, str) -> float
 
    Given s, a string representation of comma separated site-measurement
    pairs, and the name of a site, 
    return the average of the site measurements to one decimal place
    
    
    >>> calc_site_average("A, 4.2, B, 6.7, Control, 7.1, B, 6.5, Control, 7.8, Control, 6.8, A, 3.9", "Control")
    7.2
    """
    
    ## TODO: YOUR CODE HERE
    
    measurements=measurements.replace (" ", "")
    measurements=measurements.split(',')    
    newmeasurements=[]
    for item in measurements: 
        if item==site :
            index=measurements.index (site)
            indexnumber=index+1
            newmeasurements.append(measurements [indexnumber])
            measurements.remove(measurements [index])
    number=len(newmeasurements)
    newmeasurements =[float(item) for item in newmeasurements]
    total=sum(newmeasurements)
    average=total/number
    average = round (average,1)
    return average

###############################
# Part 4 - Generate Summary   #
###############################

def generate_summary(measurement_info, site):
    """
    (str, str) -> str
    
    Extract technician name, number of measurements, and average of control
    site pH level measurements from string of technician measurements. Input
    string is formatted as
    
        firstname.lastname@domain.com, date, sitename, measurement, sitename, measurement, ...
    
    returns a string with the extracted information formatted as
    
        LASTNAME,FIRSTNAME,number of measurements,average pH of specified site
 
    >>> generate_summary("dina.dominguez@company.com, 01/11/20, A, 4.2, B, 6.7, Control, 7.1, B, 6.5, Control, 7.8, Control, 6.8, A, 3.9", "Control")
    'DOMINGUEZ,DINA,7,7.2'
    """
   
    ## TODO: YOUR CODE HERE
    measurement_info=measurement_info.split(', ')
    email=str(measurement_info [0])
    s = measurement_info [2:]
    s=', '.join(str(x) for x in s)
    measurements1=measurement_info [2:]
    measurements1=','.join(str(y) for y in measurements1)
    avg=calc_site_average(measurements1, site)
    name= email_to_name(email)
    count=str(count_measurements(s))
    avg= str(avg)
    return name + ',' + count + ',' + avg


## TODO: YOUR TEST CODE HERE - REMEMBER TO DELETE THESE LINES BEFORE SUBMITTING
