# from tkinter import *

while True:

    print("\nDo you want to proceed? Press Y to 'Yes' or N for 'No'")
    choice = input("User preference! Y/N : ")
    print("\n")
    
    if choice == "Y" or choice == "y" or choice == "yes" or choice == "Yes" or choice == "YES":

        aM = len('Mach no. calculation tool')
        print(f"+{59*'-'}+")
        print(f"|{int((59-aM)/2)*' '}Mach no. calculation tool{int((59-aM)/2)*' '}|")
        print(f"+{59*'-'}+")
        print('''
The Mach number is a dimensionless quantity representing the ratio of 
the actual fluid velocity to its speed of sound. 
        ''')
        print("\nUser input data in Numbers or Floating value with decimal point:")
        V = float(input("Fluid velocity (m/s): "))
        k = float(input("k-constant (-): "))
        Z = float(input("Compresibility (-): "))
        T = float(input("Fluid temperature (degC): "))
        mw = float(input("Mole weight (kg/kmol): "))

        # Sonic velocity calculation
        vSonic = (91.1811 * (k*Z*(T+273.15)/mw)**0.5)
        vSonic = round(vSonic, 6)

        # Mach No. calculation
        Mach = V / vSonic
        Mach = round(Mach, 6)

        print(f"Sonic velocity: {vSonic}, m/s")
        print(f"Mach no.: {Mach}, (-)")

        print("\nMach No. is calculated based on following equation:\n------------------------------------------------------------ \nMach no. = V(media speed) / C(sound speed) \nV / [91.1811 * sqrt(kZT/MW)] \n------------------------------------------------------------ \nInput parameters: \n*****************\nVelocity (m/s): " + str(
            V) + "\nk (-): " + str(k) + "\nZ (-): " + str(Z) + "\nTemperature (degC): " + str(T) + "\nMole Weight (kg/kmole):" + str(mw) + "\nSound Speed (m/s):" + str(vSonic) + "\n------------------------------------------------------------ \n\nResult Mach No (-): " + str(Mach) + "\n\n------------------------------------------------------------\nCalculation tool developed in Python coding!\n\n")
        
        aW = len('Warning message')
        bW = len('Information message')
        
        if Mach > 1.0:
            print(f"+{59*'-'}+")
            print(f"|{int((59-aW)/2)*' '}Warning message{int((59-aW)/2)*' '}|")
            print(f"+{59*'-'}+")
            print("-=> Mach no. is greater than 1.0; Sonic velocity \n")
        else:
            print(f"+{59*'-'}+")
            print(f"|{int((59-aW)/2)*' '}Warning message{int((59-aW)/2)*' '}|")
            print(f"+{59*'-'}+")
            print("-=> None \n")

        print(f"+{59*'-'}+")
        print(f"|{int((59-bW)/2)*' '}Information message{int((59-bW)/2)*' '}|")
        print(f"+{59*'-'}+")
        
        for i in range (9, 0, -1):
            i = round(i * 0.1, 1)
            print(f"-=> Mach no. is {i} @ fluid velocity of {round(i*vSonic, 1)}, m/s")

    elif choice == "N" or choice == "n" or choice == "no" or choice == "No" or choice == "NO":
        input('Press ENTER to exit!')
        break
        
    else:
        print("Select valid option! Y/N")