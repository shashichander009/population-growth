import requests
import csv
from os import path
from matplotlib import pyplot as plt
from matplotlib import patches as mpatches

UN_DATA_URL = 'https://datahub.io/core/population-\
growth-estimates-and-projections/r/population-estimates.csv'


ASEAN_COUNTRIES = [
    'Brunei Darussalam',
    'Cambodia',
    'Indonesia',
    "Lao People's Democratic Republic",
    'Malaysia',
    'Myanmar',
    'Philippines',
    'Singapore',
    'Thailand',
    'Viet Nam',
]

SAARC_COUNTRIES = [
    'Afghanistan',
    'Bangladesh',
    'Bhutan',
    'India',
    'Maldives',
    'Nepal',
    'Pakistan',
    'Sri Lanka',
]


# This function downloads UN population data from given URL

def download_data():
    response = requests.get(UN_DATA_URL)
    with open('data.csv', 'wb') as fs:
        fs.write(response.content)


# PROBLEM NO 1
# This function prepares a Bar Plot of India's population vs. years.

def india_data_process():
    india_data = {}
    # This dictionary will store India's data with year as Key
    # and Population as Values. We will keep only last two digits of year and
    # store population in crores
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            region, _, year, population = line
            if region == 'India':
                population_in_crores = round(float(population) / 10000, 2)
                india_data[year[2:]] = population_in_crores

    # Changing India Data dictionary into two different
    # lists of years and population

    lists = india_data.items()
    x, y = zip(*lists)
    plt.rcParams.update({'font.size': 8})
    plt.grid(axis='y')
    plt.bar(x, y, width=0.8, color='lime', zorder=2)
    plt.title("India's Population Over the Years",
              fontsize=20, color='Red')
    plt.xlabel('Year (1950-2015)', fontsize=14, color='Red')
    plt.ylabel('Population (Cr)', fontsize=14, color='indigo')
    plt.show()


# PROBLEM NO 2
# This function prepares the Bar Chart of population of ASEAN countries in 2014
# ASEAN is a collection of South East Asian countries.

def asean_data_process():
    asean_data = {}
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            region, _, year, population = line
            if region in ASEAN_COUNTRIES and year == '2014':
                population_in_crores = round(float(population) / 10000, 2)
                asean_data[region] = population_in_crores

    # Here we update few country names to make it more readable in graph

    asean_data['Brunei'] = asean_data.pop('Brunei Darussalam')
    asean_data['Laos'] = asean_data.pop("Lao People's Democratic Republic")
    asean_data['Vietnam'] = asean_data.pop('Viet Nam')

    lists = sorted(asean_data.items())
    x, y = zip(*lists)
    plt.rcParams.update({'font.size': 10})
    plt.grid(axis='y')
    plt.bar(x, y, width=0.7, color='brown', zorder=2)
    plt.title('ASEAN Countries Population in 2014', fontsize=20,
              color='Red')
    plt.xlabel('Countries', fontsize=14, color='Red')
    plt.ylabel('Population (Cr)', fontsize=14, color='Green')
    plt.show()


# PROBLEM NO 3
# TOTAL population of SAARC countries over the past years
# In this case for each year we have to calculate total
# population of all SAARC countries.
# Then plot a BAR CHART of Total SAARC population vs. year.

def saarc_data_process():
    saarc_data = {}
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            region, _, year, population = line
            if region in SAARC_COUNTRIES:
                population_in_crores = float(population) / 10000
                if saarc_data.get(year[2:]) is None:
                    saarc_data[year[2:]] = population_in_crores
                else:
                    saarc_data[year[2:]] += population_in_crores

    for x, y in saarc_data.items():
        saarc_data[x] = round(float(y), 2)

    lists = saarc_data.items()
    x, y = zip(*lists)
    plt.rcParams.update({'font.size': 6})
    plt.bar(x, y, width=0.8, color='grey', zorder=2)
    plt.title('SAARC Population Over the Years', fontsize=17,
              color='blue')
    plt.xlabel('Year (1950-2015)', fontsize=14, color='Red')
    plt.ylabel('Population (Cr)', fontsize=14, color='Green')
    plt.grid(axis='y')
    plt.show()


# PROBLEM NO 4
# Grouped Bar Chart - ASEAN population vs. years
# We will plot population of ASEAN countries as
# groups over the years 2011 - 2015.

def asean_group_data_process():
    asean_grp_data = {}
    # In this dictionary we will store data of asean countries population
    # The key will be concat of Year + Country to make it unique
    # The value will be population
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            (region, _, year, population) = line
            if region in ASEAN_COUNTRIES and int(year) >= 2011 and \
                    int(year) <= 2015:
                population_in_crores = round(float(population) / 10000, 2)
                asean_grp_data[str(region) + '-' + str(year)
                               ] = population_in_crores

    lists = sorted(asean_grp_data.items())
    _, y = zip(*lists)

    # We will create a list of lists from the asean_grp_data
    # It will be a 10 * 5 matrix with each row
    # representing population of one country
    # Columns will represent each year

    i = 0
    pop_list_of_list = []
    while i < len(y):
        pop_list_of_list.append(y[i:i + 5])
        i += 5

    # This is equivalent to np.arange function.
    # We will use this to plot x axis
    x = [0, 1.0, 2.0, 3.0, 4.0]

    bar_width = 0.08

    colors_list = [
        'gray',
        'darkred',
        'gold',
        'greenyellow',
        'teal',
        'cyan',
        'navy',
        'purple',
        'red',
        'lime',
    ]

    for k in range(10):
        x_cord_list = [round(i + bar_width * k, 2) for i in x]
        plt.bar(x_cord_list, pop_list_of_list[k], width=bar_width,
                color=colors_list[k], zorder=2)

    x_lables_cord = [round(i + bar_width * 5, 2) for i in x]
    plt.xticks(x_lables_cord, ['2011', '2012', '2013', '2014', '2015'])
    plt.title('ASEAN Countries Population (2011-2015)', fontsize=20,
              color='Red')
    plt.xlabel('Years', fontsize=14, color='Red')
    plt.ylabel('Population (Cr)', fontsize=14, color='Green')

    # Here we are adding lables to the graph
    gray_patches = mpatches.Patch(color='gray', label='Brunei')
    darkred_patches = mpatches.Patch(color='darkred', label='Cambodia')
    gold_patches = mpatches.Patch(color='gold', label='Indonesia')
    greenyellow_patches = mpatches.Patch(color='greenyellow',
                                         label='Laos')
    teal_patches = mpatches.Patch(color='teal', label='Malaysia')
    cyan_patches = mpatches.Patch(color='cyan', label='Myanmar')
    navy_patches = mpatches.Patch(color='navy', label='Philippines')
    purple_patches = mpatches.Patch(color='purple', label='Singapore')
    red_patches = mpatches.Patch(color='red', label='Thailand')
    lime_patches = mpatches.Patch(color='lime', label='Vietnam')

    plt.legend(handles=[
        gray_patches,
        darkred_patches,
        gold_patches,
        greenyellow_patches,
        teal_patches,
        cyan_patches,
        navy_patches,
        purple_patches,
        red_patches,
        lime_patches,
    ])
    plt.rcParams.update({'font.size': 10})
    plt.grid(axis='y')
    plt.show()

# This is our main function which will allow users
# to Download Data as well as view those charts


def main():
    if path.exists('data.csv') is not True:
        data_file_status = 'No'
    else:
        data_file_status = 'Yes'

    while True:
        if data_file_status == 'No':
            print('0: Download Data')
            print('5: Quit')
        else:
            print('....Data Downloaded....')
            print('Which Chart do you want to see?')
            print('1: India population over years - Bar Plot')
            print('2: Bar Chart of the population of ASEAN countries in 2014')
            print('3: Total population of SAARC countries over the years')
            print('4: ASEAN countries population vs years - Grouped Bar Chart')
            print('5: Quit')
        choice = int(input('Choose an option: '))
        try:
            if choice == 0 and data_file_status == 'No':
                download_data()
                data_file_status = 'Yes'
            elif choice == 1 and data_file_status == 'Yes':
                india_data_process()
            elif choice == 2 and data_file_status == 'Yes':
                asean_data_process()
            elif choice == 3 and data_file_status == 'Yes':
                saarc_data_process()
            elif choice == 4 and data_file_status == 'Yes':
                asean_group_data_process()
            elif choice == 5:
                break
            else:
                print('Invalid input!')
        except ValueError:

            print('Input not an Integer')


if __name__ == '__main__':
    main()
