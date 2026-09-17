def calculate_transpiration(humidity, temperature):
    rate = 1
    rate *= (1 - humidity / 100)
    rate *= (1 + (temperature - 20) * 0.05)
    return max(rate, 0)


def test_transpiration():
    humidity = 60
    temperature = 24
    rate = calculate_transpiration(humidity, temperature)
    #print("Transpiration rate: ", rate)
   


def menu():
    humidity = 50
    temperature = 20
    light = 80
    soil = 40
    sucrose = 20
    sink_demand = 50

    while True:
        print("\n--- Menu ---")
        print("1. Change humidity")
        print("2. Change temperature")
        print("3. Show transpiration rate")
        print("4. Change light level")
        print("5. Change soil moisture")
        print("6. Show stomata state")
        print("7. Change sucrose concentration")
        print("8. Change sink input")
        print("9. Show phloem transport")
        print("10. Leave")
           


        choice = input("Choose an option: ")

        if choice == "1":
            humidity = float(input("Enter humidity (0-100): "))
        elif choice == "2":
            temperature = float(input("Enter temperature (degrees C): "))
        elif choice == "3":
            rate = calculate_transpiration(humidity, temperature)
            print("Transpiration rate:", rate)
        elif choice == "4":
             light = float(input("Enter light level (0-100): "))
        elif choice == "5":
             soil = float(input("Enter soil moisture (0-100): "))
        elif choice == "6":
            print("Stomata state:", stomata_opening(light))
        elif choice == "7":
            sucrose = float(input("Enter sucrose concentration (0-100): "))
        elif choice == "8":
            sink_demand = float(input("Enter sink demand (0-100): "))
        elif choice == "9":
            loading = phloem_loading(sucrose, light)
            pressure = mass_flow(loading, water_uptake(soil))
            unloading = phloem_unloading(pressure, sink_demand)
        elif choice == "10":
            break
        else:
             print("Invalid input")

        print("\n--- Phloem Transport ---")
        print("Loading rate:", loading)
        print("Pressure (mass flow):", pressure)
        print("Unloading rate:", unloading)



def main(): 
    print("Plant Transport System")


if __name__ == "__main__":
    menu()

def stomata_opening(light_level):
    if light_level > 70:
        return "Open" 
    elif light_level > 30:
        return "Half open"
    else:
        return "Closed"

def water_uptake(soil_moisture):
    return soil_moisture * 0.2

def phloem_loading(sucrose_concentration, light_level):
    concentration = sucrose_concentration + (light_level * 0.1)
    return concentration

def mass_flow(loading_rate, water_uptake):
    pressure = loading_rate * 0.05 + water_uptake * 0.1
    return pressure

def phloem_unloading(pressure, sink_demand):
    unloading = pressure * (sink_demand / 100)
    return unloading


light = 80
soil = 40

sucrose = 20
sink_demand = 50
