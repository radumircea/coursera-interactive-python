# calculator with all buttons

# import simplegui and access it through simplegui var
import simplegui


# intialize globals
store = 12
operand = 3


# event handlers for calculator with a store and operand

def output():
    """prints contents of store and operand"""
    global input1
    print input1.get_text()
    print "Store = ", store
    print "Operand = ", operand
    print ""
    
def swap():
    #docstring
    """ swap contents of store and operand"""
    # access global variables
    global store, operand
    # swap store with operand
    store, operand = operand, store
    # run output function
    output()

def add():
    """add store with operand """
    global store, operand
    store += operand
    output()

def sub():
    """add store with operand """
    global store, operand
    store -= operand
    output()    

def mult():
    global store, operand
    store *= operand
    output()

def div():
    global store, operand
    if operand == 0:
        print "Cannot divide by 0!"
    else:
        store /= operand
        output()

def input_handler(input_text):
    # check if number
    global operand
    if input_text.isdigit():
        number = int(input_text)
        operand = number
    else: 
        print "Input is not valid!"
    

# create frame
frame = simplegui.create_frame("Calculator", 300, 300)

# register event handlers
frame.add_button("Print", output, 100)
frame.add_button("Swap", swap, 100)
frame.add_button("Add", add, 100)
frame.add_button("Sub", sub, 100)
frame.add_button("Mult", mult, 100)
frame.add_button("Div", div, 100)
input1 = frame.add_input("Label", input_handler, 200)
# get frame rolling
frame.start()