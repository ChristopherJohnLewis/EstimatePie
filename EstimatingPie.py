#Chris Lewis
#1/15/17
#Estimating pie. The Precision increases as p_d increases
def main():
    p_d = 101 #The diameter of the circle or the length of the square the circle is enscribed into
    radius = p_d/2
    CellsInCircle = 1 + int(radius)*4 #the 1 is coordinate 0,0, since it is always in the circle so it can just be added in, radius*4 is the number of x's or y's that are 0 for one quadrant of the circle, these are always in the circle
    additive =0 #number of cells in the circle, the ones defined by CellsInCircle are not there
    TotalCells =0 #number of cells in the square that are not defined by the CellsInCircle or additive
    for y in range(int(radius)+1): #plus one is to make sure 0 is counted for
        for x in range(int(radius)+1):
            x2 = x*x
            y2 = y*y
            comparative = x2+y2
            if(comparative <= (radius*radius)) & (x != 0) & (y != 0): #first condition is to make sure the middle of the cell is defined to be in the radius
                additive +=4 #add four because this is only to take into account one quadrant, the 4 will take into account all 4 quadrants
            elif (comparative > (radius*radius)) & (x != 0) & (y != 0):
                TotalCells +=4
    CellsInCircle += additive
    TotalCells +=CellsInCircle
    EstimateCS = CellsInCircle/TotalCells
    EstimatePie = EstimateCS*4
    print("Cells in circle:",CellsInCircle,"\nTotal number of cells:",TotalCells, "\nEstimate of A_c/A_s:",EstimateCS,"\nEstimate of pie:", EstimatePie)
main()