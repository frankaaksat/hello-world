"""
In this script we want to open the appended .xml file and extract the x- ,y- and z-position. We can use this to get 
the approximated range by the use of simple math. First of all we should use the terminal to create a virtual environment(venv). 
After this is activated we can pip install the "xmltodict" package from the terminal. This package convert a .xml 
file to a "python ordered dictionary". Loading the .xml file and converting is already done. 

Look for the TODO statements. And fill in. 

"""
# TODO Put in the absolute path to Ephemeris_ASBM1.xml
filePath = "Ephemeris_ASBM1"

# ----------------------------------- NO CHANGES NEEDED HERE
import xmltodict  # This library must be "pip installed" before it can be imported

# load Ephemeris_ASBM1.xml and save it in a variable called "ephemeris"
with open(filePath, "r") as f:
    ephemeris = f.read()
    ephemeris = xmltodict.parse(ephemeris)

# how many datapoints/measurepoint from ephemeris.xml.
nmb_datapoint = len(ephemeris["lre"]["Datasegment"])

# we want to extract these measurements from the variable "ephemeris"
ephemeris_parameters = (
    "SC_X_ECI_position",
    "SC_Y_ECI_position",
    "SC_Z_ECI_position",
    "Calendar_time",
)

# ----------------------------------- START FILLING IN UNDER HERE

# TODO Create a function that retrive the parameters defined in the variable "ephemeris_parameters" above.
def extractParameter(ephemeris_string):
    """
    Extracts ephemeris data
    """
    # TODO most of the function is already written. But some parts are missing
    #       * Create an ampty list before the loop. This will store each measurement through the for-loop
    #       * The extracted value will be stored in a variable called "tmp_store". This should be appended to the empty list you have created
    #       * return the newly populated list

    for idx in range(nmb_datapoint):
        tmp_store = ephemeris["lre"]["Datasegment"][idx][ephemeris_string]




# TODO  * Use the function you made above to extract all selected measurement.
#       * The first parameter for the x-position ("xPos_as_string") can be extracted as below(after you have created the function)
#       * Write "yPos_as_String" and "zPos_as_String"
xPos_as_string = extractParameter(ephemeris_parameters[0])


# TODO  the issue now is that "xPos_as_string" is a list of strings these needs to be converted to floats.

# TODO  * Now when you have x-, y- and z-pos you can use simple math to find the range. e.g https://en.wikipedia.org/wiki/Euclidean_distance. (Pythagorean theorem)
#       * Remember that the center of earth is one of the points at location (0, 0, 0)
#       * Maybe the "math" or "numpy" library can be used to simplify things.


# ---------- plotting and visualization
# TODO  * Use the matplotlib library to visualize the result in a plot.
#       * To import the library pip install and import it with the syntax "import matplotlib.pyplot as plt"
#       * y-axis should contain the range
#       # Try to put the dates on x-axis
