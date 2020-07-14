import requests
import csv
from os import path
from matplotlib import pyplot as plt

plt.rcParams.update({'font.size': 6})

UN_DATA_URL = 'https://datahub.io/core/population-growth-estimates-and-projections/r/population-estimates.csv'

# This function downloads UN population data from given URL


def download_data():
    response = requests.get(UN_DATA_URL)
    with open("data.csv", 'wb') as fs:
        fs.write(response.content)
    return "Success"

# PROBLEM NO 1
# This function prepares a Bar Plot of 'population of India' vs. years.


def india_data_process():
    india_data = {}  # This dictionary will store India's data with year as Key and Population as Values. We will keep only last two digits of year and population in crores
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            region, _, year, population = line
            if region == 'India':
                population_in_crores = round(float(population)/10000, 2)
                india_data[year[2:]] = population_in_crores
    # Changing India Data dictionary into two sepreate lists of years and population
    lists = india_data .items()
    x, y = zip(*lists)
    plt.bar(x, y, width=0.8, color="blue")
    plt.title("India's Population Over the Years", fontsize=20, color='Red')
    plt.xlabel('Year (1950-2015)', fontsize=14, color='Red')
    plt.ylabel('Population (Cr)', fontsize=14, color='Green')
    plt.show()

# PROBLEM NO 2
# This function prepares the Bar Chart of population of ASEAN countries in 2014
# ASEAN is a collection of South East Asian countries. Plot a Bar Chat of the population of these countries. Only use data for the year 2014


def asean_data_process():
    asean_data = {}
    asean_countries = ['Brunei Darussalam', 'Cambodia', 'Indonesia', "Lao People's Democratic Republic", 'Malaysia',
                       'Myanmar', 'Philippines', 'Singapore', 'Thailand', 'Viet Nam']

    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            region, _, year, population = line
            if region in asean_countries and year == '2014':
                population_in_crores = round(float(population)/10000, 2)
                asean_data[region] = population_in_crores

    asean_data['Brunei'] = asean_data.pop('Brunei Darussalam')
    asean_data["Laos"] = asean_data.pop("Lao People's Democratic Republic")
    asean_data['Vietnam'] = asean_data.pop('Viet Nam')

    lists = sorted(asean_data .items())
    x, y = zip(*lists)
    plt.rcParams.update({'font.size': 10})
    plt.bar(x, y, align="center", width=0.7, color="red")
    plt.title("ASEAN Countries Population in 2014", fontsize=20, color='Red')
    plt.xlabel('Countries', fontsize=14, color='Red')
    plt.ylabel('Population (Cr)', fontsize=14, color='Green')
    plt.show()

# PROBLEM NO 3
# This function calculates the TOTAL population of SAARC countries over the past years,
# In this case for each year we have to calculate the sum of the population of all SAARC countries. Then plot a BAR CHART of Total SAARC population vs. year.


def saarc_data_process():
    saarc_data = {}
    saarc_countries = ['Afghanistan', 'Bangladesh', 'Bhutan',
                       'India', 'the Maldives', 'Nepal', 'Pakistan', 'Sri Lanka']

    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            region, _, year, population = line
            if region in saarc_countries:
                population_in_crores = round(float(population)/10000, 2)
                if saarc_data.get(year[2:]) is None:
                    saarc_data[year[2:]] = population_in_crores
                else:
                    saarc_data[year[2:]] += population_in_crores

    for x, y in saarc_data.items():
        saarc_data[x] = round(float(y), 2)

    lists = saarc_data .items()
    x, y = zip(*lists)
    plt.bar(x, y, align="center", width=0.8, color="blue")
    plt.title("SAARC Population Over the Years", fontsize=20, color='Red')
    plt.xlabel('Year (1950-2015)', fontsize=14, color='Red')
    plt.ylabel('Population (Cr)', fontsize=14, color='Green')
    plt.show()


def main():
    if path.exists("data.csv") != True:
        data_file_status = 'No'
    else:
        data_file_status = 'Yes'

    while True:
        if data_file_status == "No":
            print("0: Download Data")
            print("5: Quit")
        else:
            print("....Data Downloaded....")
            print("Which Chart do you want to see?")
            print("1: India population over years - Bar Plot")
            print("2: Bar Chart of the population of ASEAN countries in 2014")
            print("3: Total population of SAARC countries over the years")
            print("4: Grouped Bar Chart - ASEAN population vs. years")
            print("5: Quit")
        choice = int(input("Choose an option: "))
        try:
            if choice == 0 and data_file_status == "No":
                download_data()
                data_file_status = 'Yes'
            elif choice == 1 and data_file_status == "Yes":
                india_data_process()
            elif choice == 2 and data_file_status == "Yes":
                asean_data_process()
            elif choice == 3 and data_file_status == "Yes":
                saarc_data_process()
            elif choice == 4 and data_file_status == "Yes":
                break
            elif choice == 5:
                break
            else:
                print("Invalid input!")

        except ValueError:
            print("Input not an Integer")


if __name__ == "__main__":
    main()
