def estimate_range(battery_capacity_kwh, efficiency_wh_per_km, soc_percent):
    usable_energy_wh = battery_capacity_kwh * 1000 * (soc_percent / 100)
    estimated_range = usable_energy_wh / efficiency_wh_per_km
    return estimated_range


try:
    battery_capacity = float(input("Enter battery capacity (kWh): "))
    efficiency = float(input("Enter vehicle efficiency (Wh/km): "))
    soc = float(input("Enter current State of Charge (%): "))

    if battery_capacity <= 0 or efficiency <= 0:
        print("Battery capacity and efficiency must be positive.")
    elif soc < 0 or soc > 100:
        print("State of Charge must be between 0 and 100.")
    else:
        range_km = estimate_range(battery_capacity, efficiency, soc)
        print(f"\nEstimated Driving Range: {range_km:.2f} km")

except ValueError:
    print("Please enter valid numeric values.")
