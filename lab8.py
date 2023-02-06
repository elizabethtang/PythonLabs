###################################################
# APS106 - Winter 2022 - Lab 8 - Corner Detection #
###################################################

#from lab8_image_utils import display_image, image_to_pixels
#from operator import itemgetter

################################################
# PART 1 - RGB to Grayscale Conversion         #
################################################

def rgb_to_grayscale(rgb_img):
    """
    (tuple) -> tuple
    
    Function converts an image of RGB pixels to grayscale.
    Input tuple is a nested tuple of RGB pixels.
    
    The intensity of a grayscale pixel is computed from the intensities of
    RGB pixels using the following equation
    
        grayscale intensity = 0.3 * R + 0.59 * G + 0.11 * B
    
    where R, G, and B are the intensities of the R, G, and B components of the
    RGB pixel. The grayscale intensity should be *rounded* to the nearest
    integer.
    """
    
    ## TODO complete the function
    tup=[]
    for item in rgb_img:
        (r,g,b)=item
        print(r)
        grey=0.3*r+0.59*g+0.11*b 
        grey=round(grey)
        tup.append(grey)
    tup=tuple(tup)
    return tup
    

############################
# Part 2b - Dot Product    #
############################

def dot(x,y):
    """
    (tuple, tuple) -> float
    
    Performs a 1-dimensional dot product operation on the input vectors x
    and y. 
    """
    
    ## TODO complete the function
    total=0
    for item in range(len(x)):
        multiply=x[item]*y[item]
        total+=multiply 
    total=float(total)
    return total 


######################################
# Part 2c - Extract Image Segment    #
######################################

def extract_image_segment(img, width, height, centre_coordinate, N):
    """
    (tuple, int, int, tuple, int) -> tuple
    
    Extracts a 2-dimensional NxN segment of a image centred around
    a given coordinate. The segment is returned as a tuple of pixels from the
    image.
    
    img is a tuple of grayscale pixel values
    width is the width of the image
    height is the height of the image
    centre_coordinate is a two-element tuple defining a pixel coordinate
    N is the height and width of the segment to extract from the image
    
    """
    ## TODO complete the function
    L1 = list (img)
    L2 = []
    L3 = []
    final = []
    while len(L1) != 0:
        L2. append (L1[0:width])
        for f in L1[0:width]:
            L1.remove(f)
    x= centre_coordinate[1]
    y= centre_coordinate[0]
    start = y - (N//2)
    if start>=0:
        s = L2[start: (start+N)]
    else:
        s = L2[0: (N)]
    s2 = x - (N//2)
    if s2 >= 0:
        for m in s:
            n=m[s2:(s2+N)]
            L3.append(n)
    else:
        for m in s:
            n= i[0: (N)]
            L3.append (n)
    for i in L3:
        for m in i:
            final.append(m)
    final = tuple(final)
    return final    
img=(4 ,87, 233, 245, 227, 209, 190, 
2, 59, 235, 246, 229, 219, 200, 
17, 99, 230, 220, 211, 210, 201, 
46, 58, 196, 165, 201, 179, 150, 
82, 63, 41, 169, 190, 188, 145, 
99, 55, 54, 55, 74, 23, 12, 
45, 55, 56, 45, 155, 145, 156)
#print(extract_image_segment(img, 7, 7, (4,1), 3))
#print(extract_image_segment(img, 7,7, (2,2), 5) )
######################################
# Part 2d - Kernel Filtering         #
######################################

def kernel_filter(img, width, height, kernel):
    """
    (tuple, int, int, tuple) -> tuple
    
    Apply the kernel filter defined within the two-dimensional tuple kernel to 
    image defined by the pixels in img and its width and height.
    
    img is a 1 dimensional tuple of grayscale pixels
    width is the width of the image
    height is the height of the image
    kernel is a 2 dimensional tuple defining a NxN filter kernel, n must be an odd integer
    
    The function returns the tuple of pixels from the filtered image
    """

    ## TODO complete the function
    lst=[]
    x=width
    ker=[]
    for z in kernel:
        for y in z:
            ker.append(y)
    while x>0:
        lst.append(0)
        x-=1
    x=width
    height=height-1
    start=width-1
    import math
    kernelN=len(ker)
    N=int(math.sqrt(kernelN))
    
    centre_coordinate=[1,1]
    while height>1:
        lst.append(0)
        while width>1:
            image=extract_image_segment(img, width, height, centre_coordinate, N)
            dotted=dot(image,ker)
            lst.append(dotted)
            centre_coordinate[0]+=1
            width-=1
        width=start
        centre_coordinate[0]=1
        lst.append(0)
        height-=1
        centre_coordinate[1]+=1
    while x>0:
        lst.append(0)
        x-=1
    lst=tuple(lst)
    return lst
kernel=((1/16,1/8,1/16 ),(1/8,1/4,1/8),(1/16,1/8,1/16 ))
print(kernel_filter(img, 7, 7, kernel))

###############################
# PART 3 - Harris Corners     #
###############################

def harris_corner_strength(Ix,Iy):
    """
    (tuple, tuple) -> float
    
    Computes the Harris response of a pixel using
    the 3x3 windows of x and y gradients contained 
    within Ix and Iy respectively.
    
    Ix and Iy are  lists each containing 9 integer elements each.

    """

    # calculate the gradients
    Ixx = [0] * 9
    Iyy = [0] * 9
    Ixy = [0] * 9
    
    for i in range(len(Ix)):
        Ixx[i] = (Ix[i] / (4*255))**2
        Iyy[i] = (Iy[i] / (4*255))**2
        Ixy[i] = (Ix[i] / (4*255) * Iy[i] / (4*255))
    
    # sum  the gradients
    Sxx = sum(Ixx)
    Syy = sum(Iyy)
    Sxy = sum(Ixy)
    
    # calculate the determinant and trace
    det = Sxx * Syy - Sxy**2
    trace = Sxx + Syy
    
    # calculate the corner strength
    k = 0.03
    r = det - k * trace**2
    
    return r

def harris_corners(img, width, height, threshold):
    """
    (tuple, int, int, float) -> tuple
    
    Computes the corner strength of each pixel within an image
    and returns a tuple of potential corner locations. Each element in the
    returned tuple is a two-element tuple containing an x- and y-coordinate.
    The coordinates in the tuple are sorted from highest to lowest corner
    strength.
    """
    
    # perform vertical edge detection
    vertical_edge_kernel = ((-1, 0, 1),
                            (-2, 0, 2),
                            (-1, 0, 1))
    Ix = kernel_filter(img, width, height, vertical_edge_kernel)
    
    # perform horizontal edge detection
    horizontal_edge_kernel = ((-1,-2,-1),
                              ( 0, 0, 0),
                              ( 1, 2, 1))
    Iy = kernel_filter(img, width, height, horizontal_edge_kernel)
    
    # compute corner scores and identify potential corners
    border_sz = 1
    corners = []
    for i_y in range(border_sz, height-border_sz):
        for i_x in range(border_sz, width-border_sz):
            Ix_window = extract_image_segment(Ix, width, height, (i_x, i_y), 3)
            Iy_window = extract_image_segment(Iy, width, height, (i_x, i_y), 3)
            corner_strength = harris_corner_strength(Ix_window, Iy_window)
            if corner_strength > threshold:
                #print(corner_strength)
                corners.append([corner_strength,(i_x,i_y)])

    # sort
    corners.sort(key=itemgetter(0),reverse=True)
    corner_locations = []
    for i in range(len(corners)):
        corner_locations.append(corners[i][1])

    return tuple(corner_locations)


###################################
# PART 4 - Non-maxima Suppression #
###################################

def non_maxima_suppression(corners, min_distance):
    """
    (tuple, float) -> tuple
    
    Filters any corners that are within a region with a stronger corner.
    Returns a tuple of corner coordinates that are at least min_distance away from
    any other stronger corner.
    
    corners is a tuple of two-element coordinate tuples representing potential
        corners as identified by the Harris Corners Algorithm. The corners
        are sorted from strongest to weakest.
    
    min_distance is a float specifying the minimum distance between any
        two corners returned by this function
    """
    
    ## TODO complete the function
    F=[]
    truefalse=[]
    F.append(corners[0])
    for z in corners:
        (x,y)=z
        for a in F:
            (x1,y1)=a
            import math
            d=math.sqrt((x-x1)**2+(y-y1)**2)
            if d>=min_distance:
                truefalse.append(True)
            else:
                truefalse.append(False)
        if False in truefalse:
            None
        else:
            F.append(z)
        truefalse=[]
    F=tuple(F)    
    return F