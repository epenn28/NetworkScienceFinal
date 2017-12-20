import math

DEBUGVALS = True

def customerInRange(customer, facility):
    distance = math.sqrt(math.pow(customer[0]-facility[0],2)+math.pow(customer[1]-facility[1],2))
    return distance <= facility[2]

def customerDistance(c1, c2):
    distance = math.sqrt(math.pow(c1[0]-c2[0],2)+math.pow(c1[1]-c2[1],2))
    return distance

def fitInCell(customers, maxSize):
    maxRange = customerDistance(customers[0], customers[1])
    return maxRange <= maxSize

def customerMidpoint(c1, c2):
    midpointX = (c1[0] + c2[0]) / 2
    midpointY = (c1[1] + c2[1]) / 2
    return (midpointX, midpointY)

if __name__ == "__main__":
    facilityList = []
    customerList = []
    needsNewCell = []
    if DEBUGVALS:
        smallMin = 5
        smallMax = 25
        f0 = [50, 0, 30, 1000]
        f1 = [-50, 0, 30, 1500]
        c0 = [40, 10]
        c1 = [-40, 10]
        c2 = [10, 5]
        c3 = [-10, 0]
        facilityList.append(f0)
        facilityList.append(f1)
        customerList.append(c0)
        customerList.append(c1)
        customerList.append(c2)
        customerList.append(c3)
        print("The default values are as follows:")
        print("Facility 0: ", f0)
        print("Facility 1: ", f1)
        print("Customer 0: ", c0)
        print("Customer 1: ", c1)
        print("Customer 2: ", c2)
        print("Customer 3: ", c3)
    else:
        smallMin = input("Enter minimum range of small cells: ")
        smallMax = input("Enter maximum range of small cells: ")

        addFacility = True
        addCustomers = True
        while(addFacility):
            newFacility = input("Please enter an existing base station's information, separated by commas: x location, y location, range, operating cost\n")
            newFacility = newFacility.split(",")
            newFacility = [int(i.strip()) for i in newFacility]
            #print(newFacility)
            # new facility is a list [xVal, yVal, range, operating cost]

            addInput = input("Would you like to add another facility? y/n: ").lower()
            if addInput in ["n", "no"]:
                addFacility = False
            elif addInput in ["y", "yes"]:
                addFacility = True
            else:
                print("Invalid input, please try again")
            facilityList.append(newFacility)

        while(addCustomers):
            newCustomer = input("Please enter a customer's information, separated by commas: x location, y location\n")
            newCustomer = newCustomer.split(",")
            newCustomer = [int(i.strip()) for i in newCustomer]
            #print(newCustomer)
            # new customer is a list [xVal, yVal]

            addInput = input("Would you like to add another customer? y/n: ").lower()
            if addInput in ["n", "no"]:
                addCustomers = False
            elif addInput in ["y", "yes"]:
                addCustomers = True
            else:
                print("Invalid input, please try again")
            customerList.append(newCustomer)

    for customer in customerList:
        rangeList = []
        for facility in facilityList:
            rangeList.append(customerInRange(customer, facility))
        print("\nCustomer {}: ".format(customerList.index(customer)))
        for line in rangeList:
            print("In range of facility {}: {}".format(rangeList.index(line), line))
        if rangeList.count(True) == 0: # if this is true, then the customer is not in range of any facility and a small cell needs to be placed somewhere
            needsNewCell.append(customer)
            #print("No current facilities in range")

    if len(needsNewCell) == 1:
        newLocX, newLocY = needsNewCell[0][0], needsNewCell[0][1]
        print("\nPlace your small cell at coordinates ({}, {}).".format(newLocX, newLocY))
    elif len(needsNewCell) == 2:
        if fitInCell(needsNewCell, smallMax):
            # place a new small cell facility in between the two
            newLocX, newLocY = customerMidpoint(needsNewCell[0], needsNewCell[1])
            print("\nPlace your small cell at coordinates ({}, {}).".format(newLocX, newLocY))
        else:
            newLoc1X, newLoc1Y = needsNewCell[0][0], needsNewCell[0][1]
            newLoc2X, newLoc2Y = needsNewCell[1][0], needsNewCell[1][1]
            print("\nPlace your small cells at coordinates ({}, {}) and ({}, {}).".format(newLoc1X, newLoc1Y, newLoc2X, newLoc2Y))
    else:
        print("\nSorry, a small cell covering more than two customers is currently not supported.")
