#####################################################
# APS106 Winter 2022 - Lab 7 - Chemical Eqn Checker #
#####################################################

######################################################
# PART 1 - Complete the function below to deocompose
#          a compound formula written as a string
#          in a dictionary
######################################################

def mol_form(compound_formula):
    """(str) -> dictionary
    When passed a string of the compound formula, returns a dictionary 
    with the elements as keys and the number of atoms of that element as values.
    
    >>> mol_form("C2H6O")
    {'C': 2, 'H': 6, 'O': 1}
    >>> mol_form("CH4")
    {'C': 1, 'H': 4}
    """
     
    # TODO your code here
    dictionary ={}
    lst=[]
    compound_formula=compound_formula[::-1]
    length=len(compound_formula)
    lengthdeleted=0
    for x in range(length):
        x-=lengthdeleted
        print(x)
        charachter=compound_formula[x]
        
        if charachter.isupper():
            q=compound_formula [:x+1]
            q=q[::-1]
            lst.append (q)
            q=q[::-1]
            compound_formula=compound_formula.replace(q,"",1)
            q=len(q)
            lengthdeleted+=q
    for x in lst:
        item=""
        numbers=0
        cont=True
        for item in x:
            if cont==True:
                if item.isupper():
                    letters=item
                elif item.islower():
                    letters+=item
                    cont=False
                if item.isdigit():
                    index=x.index(item)
                    added=x[index:]
                    added=int(added)
                    numbers+=added
            if not x[-1].isdigit():
                numbers+=1
        if letters in dictionary:
            dictionary[letters]+=numbers
        else:
            dictionary[letters]=numbers
            
    return dictionary 
print (mol_form('C2H3333ClO',) )            
######################################################
# PART 2 - Complete the function below that takes two 
#          tuples representing one side of a
#          chemical equation and returns a dictionary
#          with the elements as keys and the total
#          number of atoms in the entire expression
#          as values.
######################################################
    
def expr_form(expr_coeffs,expr_molecs):
    """
    (tuple (of ints), tuple (of dictionaries)) -> dictionary
    
    This function accepts two input tuples that represent a chemical expression,
    or one side of a chemical equation. The first tuple contains integers that
    represent the coefficients for molecules within the expression. The second
    tuple contains dictionaries that define these molecules. The molecule
    dictionaries have the form {'atomic symbol' : number of atoms}. The order
    of the coefficients correspond to the order of molecule dictionaries.
    The function creates and returns a dictionary containing all elements within
    the expression as keys and the corresponding number of atoms for each element
    within the expression as values.
    
    For example, consider the expression 2NaCl + H2 + 5NaF
    
    >>> expr_form((2,1,5), ({"Na":1, "Cl":1}, {"H":2}, {"Na":1, "F":1}))
    {'Na': 7, 'Cl': 2, 'H': 2, 'F': 5}
    
    """
    # TODO your code here
    dictionary={}
    for index in range(len(expr_molecs)):
        compound=expr_molecs[index]
        listcompound=list(compound)
        coefficient= expr_coeffs[index]
        for molecule in compound: 
            number = compound[molecule]
            number=int(number)
            number= number * coefficient
            if molecule not in dictionary:
                dictionary[molecule]=number
            else:
                dictionary[molecule]+=number
    return dictionary 

########################################################
# PART 3 - Check if two dictionaries representing
#          the type and number of atoms on two sides of
#          a chemical equation contain different
#          key-value pairs
########################################################

def find_unbalanced_atoms(reactant_atoms, product_atoms):
    """
    (Dict,Dict) -> Set
    
    Determine if reactant_atoms and product_atoms contain equal key-value
    pairs. The keys of both dictionaries are strings representing the 
    chemical abbreviation, the value is an integer representing the number
    of atoms of that element on one side of a chemical equation.
    
    Return a set containing all the elements that are not balanced between
    the two dictionaries.
    
    >>> find_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "Na" : 1, "Cl" : 2})
    {'Na'}
    
    >>> find_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "Na" : 2, "Cl" : 2})
    set()
    
    >>> find_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "F" : 2, "Cl" : 2})
    {'F', 'Na'}
    """
    
    # TODO your code here
    unbalenced=[]
    for molecule in reactant_atoms:
        if molecule in product_atoms:     
            reactant = reactant_atoms[molecule] 
            product = product_atoms[molecule]
            if not reactant==product:
                unbalenced.append (molecule)
        else:
            unbalenced.append (molecule)
    for molecule in product_atoms:
        if molecule in reactant_atoms:     
            reactant = reactant_atoms[molecule] 
            product = product_atoms[molecule]
            if not reactant==product:
                unbalenced.append (molecule)
        else:
            unbalenced.append (molecule)
    unbalenced=set(unbalenced)
    return unbalenced

            

########################################################
# PART 4 - Check if a chemical equation represented by
#          two nested tuples is balanced
########################################################

def check_eqn_balance(reactants,products):
    """
    (tuple,tuple) -> Set
    
    Check if a chemical equation is balanced. Return any unbalanced
    elements in a set.
    
    Both inputs are nested tuples. The first element of each tuple is a tuple
    containing the coefficients for molecules in the reactant or product expression.
    The second element is a tuple containing strings of the molecules within
    the reactant or product expression. The order of the coefficients corresponds
    to the order of the molecules. The function returns a set containing any
    elements that are unbalanced in the equation.
    
    For example, the following balanced equation
    C3H8 + 5O2 <-> 4H2O + 3CO2
    
    would be input as the following two tuples:
    reactants: ((1,5), ("C3H8","O2"))
    products: ((4,3), ("H2O","CO2"))
    
    >>> check_eqn_balance(((1,5), ("C3H8","O2")),((4,3), ("H2O","CO2")))
    set()
    
    Similarly for the unbalanced equation
    
    C3H8 + 2O2 <-> 4H2O + 3CO2
    
    would be input as the following two tuples:
    reactants: ((1,2), ("C3H8","O2"))
    products: ((4,3), ("H2O","CO2"))
    
    >>> check_eqn_balance(((1,2), ("C3H8","O2")),((4,3), ("H2O","CO2")))
    {'O'}
    
    """
    
    #TODO your code here
    relements=reactants[1]
    expr_molecs=[]
    for x in relements:
        first=mol_form(x)
        expr_molecs.append (first)    
    expr_coeffs= reactants [0]
    reactant_atoms= expr_form(expr_coeffs,expr_molecs)
    
    pelements=products[1]
    expr_molecs=[]
    for x in pelements:
        first=mol_form(x)
        expr_molecs.append (first)    
    expr_coeffs= products [0]
    product_atoms= expr_form(expr_coeffs,expr_molecs)    
    unbalenced=find_unbalanced_atoms(reactant_atoms, product_atoms)
    
    return unbalenced

