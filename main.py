
'''
🎯 PROJECT-2: Polution Map of Indian Cities.
Data used: (21-08-2025 09:00:00)

Author: Subhash Kumar Rana
Email: subhash_2312res664@iitp.ac.in

🔍 Description:
This project uses GeoPandas along with shapefiles and pollution data to create a geospatial map
that marks Indian cities and colors them based on their air pollution values. It helps visualize the
severity of pollution in different regions.

🔧 Technologies Used:
- Python
- Pandas
- GeoPandas
- Matplotlib
'''

if __name__ == "__main__":
    print("Welcome to the Indian Cities Visualization Project!....!")

    while True:
        cmd = \
            (
                "\n🎯 Choose an Option from the Menu:\n"
                "--------------------------------------\n"
                "0. ❌ Exit / Close Program\n"
                "1. 📉 Most Polluted Cities       \n"
                "2. 📈 Low Polluted Cities        \n"
                "3. 🥧 Normal Polluted Cities       \n"
                "4. 🌐 WebView / Apply Filter        \n"
                "5. 📊 Polluted Cities India's     \n "
                "6. 🧠 Project Info     \n"
            )
        userinput = input(cmd)

        if userinput.lower() == "q" or userinput == "0":
            break
        elif userinput.lower() == "1":
            from services import mostPollutadeCities
            mostPollutadeCities()
        elif userinput.lower() == "2":
            from services import lowpollutionmap
            lowpollutionmap()
        elif userinput.lower() == "3":
            from services import medpollutionmap
            medpollutionmap()
        elif userinput == "4":
            from services import webviewmap
            webviewmap()
        elif userinput == "5":
            from services import fullviewpollutionmap
            fullviewpollutionmap()
        elif userinput == "6":
            from services import ProjectInfo
            projectinfo = ProjectInfo()
        elif userinput == "664":
            from services import AboutMe
            AboutMe()
        else:
            print("Please enter a valid option.")




