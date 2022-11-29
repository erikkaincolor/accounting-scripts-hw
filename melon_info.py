"""Print out all the melons in our inventory."""

from melons import melons 

# DEFAULT VAR:flesh color, rind color, and average weight

def print_melon(melons):
    """Print each melon with corresponding attribute information."""
    for k_ey, val in melons.items():
        print(k_ey)
        for keyss, valss in val.items():
            print(f"{keyss}: {valss}")

#this drained me omg i even tried the zip function

# i kept wanting to do the "for k_ey, val in melons.items()""...
# and a regular for loop inside of that and trying to index with brackets...
