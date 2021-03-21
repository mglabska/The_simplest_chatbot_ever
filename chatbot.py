#! python3
# Hair salon chatbot: gets a service name, preferred time, user's names, phone number and saves the data to a csv file.

import csv
import datetime
import holidays
import os
import re
from enum import Enum


# Define Service class and choice options.
class Service(Enum):
    HAIR_CUT_WOMEN = 1
    HAIR_CUT_MEN = 2
    DYEING = 3
    BALAYAGE = 4
    STYLING = 5


# Say 'Hello'
def say_hello():
    print('Dzień dobry, miło Cię widzieć!\n')


# Ask for service (1, 2, 3, 4, 5) and get the service number from the user, check correctness, get service code.
def get_service():
    service_number = input('Wybierz numer usługi, z której chcesz skorzystać:\nstrzyżenie damskie - 1,\n'
                           'strzyżenie męskie - 2,\nfarbowanie - 3,\nbalayage - 4,\nczesanie z modelowaniem - 5.\n')
    while True:
        if service_number.isnumeric() and int(service_number) in range(1, 6):
            return Service(int(service_number)).name
        else:
            service_number = input('Wpisz cyfrę od 1 do 5.')


# Get service description (to display to the customer).
def get_description(service):
    if service == 'HAIR_CUT_WOMEN':
        return 'Strzyżenie damskie'
    elif service == 'HAIR_CUT_MEN':
        return 'Strzyżenie męskie'
    elif service == 'DYEING':
        return 'Farbowanie'
    elif service == 'BALAYAGE':
        return 'Balayage'
    elif service == 'STYLING':
        return 'Czesanie z modelowaniem'


# Ask for preferred date and hours (check format, correctness, check holidays and current year, eliminate past dates).
def get_time():
    date_pattern = re.compile(r'\d{4}-[0-1][0-9]-[0-3][0-9]')
    time_pattern = re.compile(r'^([0-9][0-9]):00')
    pl_holidays = holidays.Poland()
    date = input(
        'Podaj dzień wizyty w formacie rrrr-mm-dd (np.: 2021-09-02).\n'
        'Przyjmujemy zapisy tylko na bieżący rok. Nie pracujemy w święta, ale jesteśmy otwarci w weekendy.\n')
    while True:
        try:
            if date_pattern.match(date) is None:
                date = input('Wymagany format daty: rrrr-mm-dd. Wpisz datę jeszcze raz.\n')
            elif datetime.datetime(int(date[0:4]), int(date[5:7]), int(date[8:10])) < datetime.datetime.now():
                date = input('Podaj datę przypadającą w przyszłości (jutro lub później).\n')
            elif date[0:4] != str(datetime.datetime.now().year):
                date = input('Podaj datę w bieżącym roku.\n')
            elif date in pl_holidays:
                date = input('To dzień świąteczny. Podaj inną datę.\n')
            else:
                break
        except ValueError:
            date = input('Ta data nie istnieje. Podaj istniejącą datę.\n')
    time = input(
        'Podaj godzinę wizyty w formacie gg:mm (np. 12:00).\n'
        'Zapisujemy tylko na pełne godziny od 09:00 do 18:00.\n')
    while time_pattern.match(time) is None or int(time[0:2]) not in range(9, 19):
        time = input(
            'Wymagany format godziny: gg:mm. Zapisujemy tylko na pełne godziny (gg:00) między 09:00 a 18:00.\n'
            'Wpisz godzinę jeszcze raz.\n')
    if date_pattern.match(date) is not None and time_pattern.match(time) is not None:
        return datetime.datetime.strptime(date + ' ' + time, '%Y-%m-%d %H:%M')


# Ask for first and last name.
def get_name():
    name = input('Podaj imię i nazwisko.\n')
    return name


# Ask for contact number (in defined format, check format).
def get_number():
    number = input('Podaj kontaktowy numer telefonu w formacie +48123456789.\n')
    pattern = re.compile(r'\+\d{11}')
    while True:
        if pattern.match(number) is not None:
            return number
        else:
            number = input('Numer musi być w formacie +48123456789. Wpisz numer jeszcze raz.\n')


# Create the main function to run the functions defined above and save the results to a csv file.
def main():
    service = get_service()
    time = get_time()
    name = get_name()
    number = get_number()
    filename = 'visits.csv'
    # Check if the datafile already exists.
    if not os.path.exists(filename):
        # Create file
        with open(filename, 'w', newline='') as csvfile:
            # Create first row with column names.
            visit_writer = csv.writer(csvfile, delimiter='\t', quoting=csv.QUOTE_MINIMAL)
            visit_writer.writerow(['Service', 'Date and Time', 'Name', 'Phone Number'])
    # Save data to the existing file.
    with open(filename, 'a', newline='') as csvfile:
        visit_writer = csv.writer(csvfile, delimiter='\t', quoting=csv.QUOTE_MINIMAL)
        visit_writer.writerow([service, time, name, number])
    # Confirm data collection and sum up.
    print(
        f'Zapisano następujące dane:\n'
        f'Usługa: {get_description(service)}\n'
        f'Termin: {time}\n'
        f'Imię i nazwisko: {name}\n'
        f'Numer telefonu: {number}\n'
        f'Dziękuję!'
    )


# Run program.
if __name__ == '__main__':
    say_hello()
    main()
