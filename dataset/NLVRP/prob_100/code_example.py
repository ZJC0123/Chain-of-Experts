def prob_100(VehicleCapacity, DepotLocations, CustomerDemands, CustomerLocations, CustomerTimeWindows):
    """
    Args:
        VehicleCapacity: an integer, indicates maximum cargo weight per vehicle
        DepotLocations: a list of lists, each sublist contains two floats for coordinates of regional distribution centers
        CustomerDemands: a list of integers, each denotes required cargo weight for a store
        CustomerLocations: a list of lists, each sublist contains two floats for store coordinates
        CustomerTimeWindows: a list of lists, each sublist contains two integers for acceptable delivery time range [start, end]

    Returns:
        TotalDistance: an integer, denotes minimized total travel distance across all vehicles
    """
    # To be implemented
    TotalDistance = 1e9
    return TotalDistance