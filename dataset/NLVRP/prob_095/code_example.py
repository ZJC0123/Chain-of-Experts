def prob_095(VehicleCapacity, CustomerDemands, DepotLocations, CustomerLocations, TimeWindows):
    """
    Args:
        VehicleCapacity: an integer, indicates the maximum volume capacity of each vehicle
        CustomerDemands: a list of integers, each denotes the volume demand of a customer's order
        DepotLocations: a list of lists, each sublist contains two floats for coordinates of a warehouse location (shape [2])
        CustomerLocations: a list of lists, each sublist contains two floats for coordinates of a customer's location (shape [2])
        TimeWindows: a list of lists, each sublist contains two integers representing [start, end] of acceptable delivery time window (shape [2])

    Returns:
        TotalCost: an integer, denotes the minimized total transportation cost for all coordinated delivery routes
    """
    # To be implemented
    TotalCost = 1e9
    return TotalCost