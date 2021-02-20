weight = int(input("Ievadi savu svaru (kg): "))
heightInCentimetters = int(input("Ievadi savu augumu (cm): "))
height = heightInCentimetters / 100
massIndex = weight / (height * height)
print(f"Tavs ķermeņa masas indekss ir: {massIndex}")