def prob_110(VehicleCapacity, DepotLocations, CustomerDemands, CustomerLocations, TimeWindows, ServiceDurations):
    """
    Args:
        VehicleCapacity: an integer, indicates maximum cargo capacity per vehicle
        DepotLocations: a list of lists, each sublist contains two floats denoting coordinates of a distribution center
        CustomerDemands: a list of integers, each denotes fixed delivery quantity for a customer
        CustomerLocations: a list of lists, each sublist contains two floats for customer's geographical coordinates
        TimeWindows: a list of lists, each sublist contains two integers specifying customer's availability window [start, end]
        ServiceDurations: a list of integers, each denotes required service duration at customer location

    Returns:
        TotalDistance: a float, denotes minimized total transportation distance across all vehicles
    """
    # To be implemented
    TotalDistance = 1e9
    return TotalDistance