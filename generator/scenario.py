from library.steps_core import check_get_geo_function, create_and_store_parameters, check_weather_files, check_renewables_files, create_and_store_demand_input, create_and_store_network, create_and_store_optimize, create_and_store_results, clear_working_files
from library.steps_addon import create_and_store_addon_results
def run_scenario(config, tidy):

    # Files: none
    print("Check the get_geo(config) function")
    check_get_geo_function(config)

    # Files: assumptions.csv
    print("Create and store parameters")
    create_and_store_parameters(config)

    # Files: cutout.nc, time_index.csv, selection files (verify only)
    print("Check weather files")
    check_weather_files(config)

    # Files: avail_{solar|onwind|offwind}.nc, avail_capacity_{solar|onwind|offwind}.nc (verify only)
    print("Check renewables data")
    check_renewables_files(config)

    # Files: demand.csv
    print("Create and store demand")
    create_and_store_demand_input(config)

    # Files: network.nc
    print("Create and store network")
    create_and_store_network(config)

    # Files: statistics.pkl
    print("Run optimization")
    create_and_store_optimize(config)

    # Files: multiple
    create_and_store_results(config)

    # Files: multiple
    create_and_store_addon_results(config)

    if tidy:
        clear_working_files(config)
