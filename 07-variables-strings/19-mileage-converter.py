# Kilometer to Miles Converter
kilometer_cycle = float(input("How many kilometeres did you cycle today? "))
mile_cycle = kilometer_cycle / 1.60934
mile_cycle = round(mile_cycle, 2)

print(f"Your {kilometer_cycle}km ride is equal to {mile_cycle}mi.")
