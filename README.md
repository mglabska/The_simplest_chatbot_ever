# chatbot.py - program do umawiania wizyt w salonie fryzjerskim

Program służy do umawiania wizyt w salonie fryzjerskim - pobiera od użytkownika:
1. kod wybranej usługi,
2. preferowany termin (datę i godzinę) w danym roku kalendarzowym, z wyłączeniem oficjalnych świąt (w przedziale od 9:00 do 18:00, zapisy są przyjmowane o pełnych godzinach),
3. imię i nazwisko,
4. numer kontaktowy.

Następnie zapisuje wszystkie dane w pliku csv i wyświetla użytkownikowi potwierdzenie. 
Program sprawdza też poprawność danych: czy format daty i godziny jest poprawny, czy data istnieje (wyklucza daty typu 30 lutego lub 31 września), czy nie przypada w przeszłości albo w święto państwowe. Nie sprawdza, czy dany termin jest już zajęty - przyjęto założenie, że w salonie pracuje wiele osób oraz jest w nim wystarczająco dużo miejsc, aby obsłużyć kilku klientów w jednym terminie.

Program chatbot.py wymaga instalacji środowiska języka Python (w wersji 3.x). Przed uruchomieniem programu należy zainstalować bibliotekę holidays (komendą: pip install holidays lub: pip3 install holidays).
Aby uruchomić program, należy z poziomu folderu, w którym zapisano program, wpisać w wierszu poleceń komendę: python chatbot.py (lub: python3 chatbot.py).
