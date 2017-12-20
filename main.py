import math

DEBUGVALS = True

def customerInRange(customer, facility):
    distance = math.sqrt(math.pow(customer[0]-facility[0],2)+math.pow(customer[1]-facility[1],2))
    return distance <= facility[2]

if __name__ == "__main__":
    if DEBUGVALS:
        facilityList = []
        customerList = []
        smallMin = 5
        smallMax = 25
        f1 = [50, 0, 30, 1000]
        f2 = [-50, 0, 30, 1500]
        c1 = [40, 10]
        c2 = [-40, 10]
        c3 = [10, 0]
        c4 = [-10, 0]
        facilityList.append(f1)
        facilityList.append(f2)
        customerList.append(c1)
        customerList.append(c2)
        customerList.append(c3)
        customerList.append(c4)
        for customer in customerList:
            for facility in facilityList:
                print(customerInRange(customer, facility))
    else:
        facilityList = []
        customerList = []
        smallMin = input("Enter minimum range of small cells: ")
        smallMax = input("Enter maximum range of small cells: ")

        addFacility = True
        addCustomers = True
        while(addFacility):
            newFacility = input("Please enter an existing base station's information, separated by commas: x location, y location, range, operating cost\n")
            newFacility = newFacility.split(",")
            newFacility = [int(i.strip()) for i in newFacility]
            print(newFacility)
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
            print(newCustomer)
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
            for facility in facilityList:
                print(customerInRange(customer, facility))
