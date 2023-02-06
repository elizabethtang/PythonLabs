############################################################
# APS106 Winter 2022 - LAB 9 - Wind Turbine Placement OOP  #
############################################################

import csv

class Point:
    """
    A point in a two-dimensional coordinate plane
    """
    
    def __init__(self, x, y):
        """
        Create a point with an x and y coordinate
        """
        self.x = x
        self.y = y
        
    def __str__(self):
        """
        Generate a string representation of a point
        """
        return "(" + str(self.x) + "," + str(self.y) + ")"


############################
# Part 1 - Circle Class
############################
class Circle:
    """
    A circle in a two-dimensional coordinate plane
    """
    
    def __init__(self, centre_x, centre_y, radius):
        """
        Create a rectangle defined by its bottom left and top right corner
        coordinates
        """
        self.centre = Point(centre_x, centre_y)
        self.radius = radius
        
    def __str__(self):
        """
        Generate a string representation of a rectangle
        """
        return ("Circle with centre coordinate " + 
                str(self.centre) + " and radius " + str(self.radius))
    
    def move(self, horizontal_translation, vertical_translation):
        """
        (Circle, int, int) -> None
        
        Alters the location of a circle by translating the coordinates
        of its centre coordinates.
        """
        # TODO complete the method

        self.centre.x=self.centre.x+horizontal_translation
        self.centre.y=self.centre.y+vertical_translation    
    
    def overlap(self, circB):
        """
        (Circle, Circle) -> bool
        
        Checks whether two circles overlap, return true if they overlap, false otherwise
        """
    
        # compute the distance between the centres
        d = ((self.centre.x - circB.centre.x) ** 2 + (self.centre.y - circB.centre.y) ** 2) ** (1/2)
        return d < (self.radius + circB.radius)

        
##############################
# Part 2 - Wind Turbine Class
##############################
class WindTurbine:
    """
    A wind turbine placed in a two-dimensional area
    """
    
    def __init__(self, id_number, placement_centre_x, placement_centre_y, placement_radius):
        """
        Create a wind turbine
        """
        self.id_number = id_number
        self.placement = Circle(placement_centre_x,placement_centre_y, placement_radius)
        
        self.overlapping_turbines = []
    
    def __str__(self):
        """
        Generate a string representation of a WindTurbine object
        """
        return ("Wind Turbine ID: " + str(self.id_number) + 
                ", Placement: " + str(self.placement))

        
    def move(self, horizontal_translation, vertical_translation):
        """
        (WindTurbine, int, int) -> None
        
        Alters the location of a wind turbine by translating the coordinates
        of its bottom left and top right corner coordinates. After moving the 
        turbine, the overlapping turbine list should be reset to an empty
        list.
        
        The change in the x and y coordinates are specified by the
        horizontal_translation and vertical_translation parameters, respectively.
        """
        # TODO complete the method (approx. 2 lines of code)
        self.placement.move(horizontal_translation,vertical_translation)
        self.overlapping_turbines=[]
    def overlap(self, turbineB):
        """
        (WindTurbine, WindTurbine) -> bool
        
        Checks for overlap between a wind turbine and another turbine (turbineB).
        """
        # TODO complete the method (approx. 1 line of code)
        x=self.placement.overlap (turbineB.placement)
        return x
        
    def validate_placement(self, turbines):
        """
        (WindTurbine, list of WindTurbines) -> None
        
        Check if the postion of a wind turbine is valid by checking for
        overlapping areas with all other wind turbines.
        """
        # TODO complete the method (approx. 3-4 lines of code)
        for x in turbines:
            if not self.id_number==x.id_number and self.overlap(x)==True:
                    self.overlapping_turbines.append (x)
            

##########################################
# Part 3 - Load Wind Turbines from File
##########################################

def load_turbine_placements(turbine_filename):
    """
    (str) -> list of WindTurbines

    Opens a csv file containing wind turbine IDs, and placement 
    info (centre coordinates and radius) and returns a list
    of WindTurbine objects for each turbine defined in the file
    """

    # TODO Complete the function
    turbines=[]
    with open(turbine_filename, 'r') as csv:
        contents=csv.readlines()        
        contents=contents[1:]
    for line in contents:
        length=len(line)
        line=line[:length-1]
        line=line.split(',')
        lst=[]
        for x in line:
            x=int(x)
            lst.append(x)
        (a,b,c,d)=lst
        g=WindTurbine(a,b,c,d)
        turbines.append (str(g))
    return turbines

##########################################
# Part 4 - Testing Wind Turbine Placement
##########################################

def check_turbine_placements(turbines):
    """
    (list of WindTurbines) -> int
    
    Checks a list of wind turbines to identify turbines with invalid (overlapping)
    placements. The function should return the number of turbines with 
    invalid placements.
    
    All placements should be evaluated using the validate_placement method from
    the WindTurbine class.
    """
    
    ## TODO complete the function
    overlapped=set()    
    for x in turbines:
        x.validate_placement(turbines)
        for turbine in x.overlapping_turbines:
            turb=turbine.id_number
            overlapped.add(turb)
    number=len(overlapped)
    return number
