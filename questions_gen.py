import json

questions = []


q = "Jak definiuje się klasę w Pythonie?"
a = [
    "Używając słowa kluczowego class",
    "Używając słowa kluczowego def",
    "Używając słowa kluczowego object",
    "Używając słowa kluczowego type",
]
questions.append({"question": q, "answers": a})

q = "Co to jest klasa w Pythonie?"
a = [
    "Szablon dla tworzenia obiektów",
    "Funkcja wywoływana przy tworzeniu obiektu",
    "Zmienna przechowująca wartość",
    "Blok kodu, który może być wielokrotnie używany",
]
questions.append({"question": q, "answers": a})

# Jak nazywamy "szablon" używany do tworzenia obiektów w programowaniu obiektowym?
#
# A) Klasa
# B) Instancja
# C) Interfejs
# D) Pakiet

q = 'Jak nazywamy "szablon" używany do tworzenia obiektów w programowaniu obiektowym?'
a = ["Klasa", "Instancja", "Interfejs", "Pakiet"]
questions.append({"question": q, "answers": a})

# Co różni obiekt od klasy w programowaniu obiektowym?
#
# A) Obiekt jest instancją klasy.
# B) Obiekt jest szablonem dla klasy.
# C) Obiekt definiuje metody i atrybuty klasy.
# D) Obiekt nie może być stworzony na podstawie klasy.

q = "Co różni obiekt od klasy w programowaniu obiektowym?"
a = [
    "Obiekt jest instancją klasy.",
    "Obiekt jest szablonem dla klasy.",
    "Obiekt definiuje metody i atrybuty klasy.",
    "Obiekt nie może być stworzony na podstawie klasy.",
]
questions.append({"question": q, "answers": a})

# Co to są atrybuty klasy w kontekście programowania obiektowego?
#
# A) Są to zmienne zdefiniowane wewnątrz klasy.
# B) Są to funkcje, które operują na danych klasy.
# C) Są to klasy pochodne.
# D) Są to metody do tworzenia nowych instancji klasy.

q = "Co to są atrybuty klasy w kontekście programowania obiektowego?"
a = [
    "Są to zmienne zdefiniowane wewnątrz klasy.",
    "Są to funkcje, które operują na danych klasy.",
    "Są to klasy pochodne.",
    "Są to metody do tworzenia nowych instancji klasy.",
]
questions.append({"question": q, "answers": a})

# Jak nazywamy atrybut, który jest wspólny dla wszystkich instancji klasy?
#
# A) Atrybut klasowy
# B) Atrybut instancji
# C) Atrybut lokalny
# D) Atrybut globalny

q = "Jak nazywamy atrybut, który jest wspólny dla wszystkich instancji klasy?"
a = ["Atrybut klasowy", "Atrybut instancji", "Atrybut lokalny", "Atrybut globalny"]
questions.append({"question": q, "answers": a})

# Co to są atrybuty obiektu w kontekście programowania obiektowego?
#
# A) Są to zmienne związane z konkretną instancją klasy.
# B) Są to metody zdefiniowane wewnątrz klasy.
# C) Są to klasy pochodne.
# D) Są to metody do tworzenia nowych instancji klasy.

q = "Co to są atrybuty obiektu w kontekście programowania obiektowego?"
a = [
    "Są to zmienne związane z konkretną instancją klasy.",
    "Są to metody zdefiniowane wewnątrz klasy.",
    "Są to klasy pochodne.",
    "Są to metody do tworzenia nowych instancji klasy.",
]
questions.append({"question": q, "answers": a})

# Jakiego rodzaju atrybuty są zwykle unikalne dla każdej instancji obiektu?
#
# A) Atrybuty instancji
# B) Atrybuty klasowe
# C) Atrybuty statyczne
# D) Atrybuty globalne

q = "Jakiego rodzaju atrybuty są zwykle unikalne dla każdej instancji obiektu?"
a = [
    "Atrybuty instancji",
    "Atrybuty klasowe",
    "Atrybuty statyczne",
    "Atrybuty globalne",
]
questions.append({"question": q, "answers": a})

q = "Co to jest atrybut klasy w Pythonie?"
a = [
    "Właściwość przypisana do klasy, dostępna dla wszystkich jej instancji",
    "Wartość zwracana przez funkcję",
    "Nazwa klasy",
    "Blok kodu wewnątrz klasy",
]
questions.append({"question": q, "answers": a})

q = "Jak nazywa się funkcję, która jest definiowana wewnątrz klasy w Pythonie?"
a = ["Metodą", "Klasą", "Modułem", "Pakietem"]
questions.append({"question": q, "answers": a})

# Co to są metody obiektu w kontekście programowania obiektowego?
#
# A) Są to funkcje zdefiniowane w klasie, które operują na danych obiektu.
# B) Są to zmienne związane z konkretną instancją klasy.
# C) Są to klasy pochodne.
# D) Są to atrybuty klasy.

q = "Co to są metody obiektu w kontekście programowania obiektowego?"
a = [
    "Są to funkcje zdefiniowane w klasie, które operują na danych obiektu.",
    "Są to zmienne związane z konkretną instancją klasy.",
    "Są to klasy pochodne.",
    "Są to atrybuty klasy.",
]
questions.append({"question": q, "answers": a})

# Co robi metoda obiektu w programowaniu obiektowym?
#
# A) Operuje na danych obiektu i/lub wykonuje akcje związane z tym obiektem.
# B) Definiuje strukturę klasy.
# C) Tworzy nową instancję klasy.
# D) Wszystkie instancje klasy dzielą te same metody.

q = "Co robi metoda obiektu w programowaniu obiektowym?"
a = [
    "Operuje na danych obiektu i/lub wykonuje akcje związane z tym obiektem.",
    "Definiuje strukturę klasy.",
    "Tworzy nową instancję klasy.",
    "Wszystkie instancje klasy dzielą te same metody.",
]
questions.append({"question": q, "answers": a})

# Co to są metody klasy w kontekście programowania obiektowego?
#
# A) Są to funkcje zdefiniowane w klasie, które operują na danych klasy.
# B) Są to zmienne związane z konkretną instancją klasy.
# C) Są to klasy pochodne.
# D) Są to atrybuty obiektu.

q = "Co to są metody klasy w kontekście programowania obiektowego?"
a = [
    "Są to funkcje zdefiniowane w klasie, które operują na danych klasy.",
    "Są to zmienne związane z konkretną instancją klasy.",
    "Są to klasy pochodne.",
    "Są to atrybuty obiektu.",
]

q = "Czym różni się metoda klasy od metody obiektu w Pythonie?"
a = [
    "Metoda klasy jest powiązana z klasą, a nie z konkretną instancją klasy",
    "Metoda klasy jest szybsza",
    "Metoda klasy nie może być przeciążona",
    "Metoda klasy nie może być przekazywana jako argument",
]
questions.append({"question": q, "answers": a})

q = "Co zwraca metoda __init__ w Pythonie?"
a = [
    "Nic (metoda __init__ nie ma instrukcji return)",
    "Nowy obiekt klasy",
    "Wartość True albo False",
    "Bieżący obiekt (self)",
]
questions.append({"question": q, "answers": a})


# Co to jest konstruktor w kontekście programowania obiektowego?
#
# A) Jest to specjalna metoda klasy, która jest wywoływana automatycznie podczas tworzenia obiektu.
# B) Jest to metoda używana do tworzenia nowych klas.
# C) Jest to atrybut obiektu.
# D) Jest to funkcja, która niszczy obiekt.

q = "Co to jest konstruktor w kontekście programowania obiektowego?"
a = [
    "Jest to specjalna metoda klasy, która jest wywoływana automatycznie podczas tworzenia obiektu.",
    "Jest to metoda używana do tworzenia nowych klas.",
    "Jest to atrybut obiektu.",
    "Jest to funkcja, która niszczy obiekt.",
]
questions.append({"question": q, "answers": a})

# Jaką rolę pełni konstruktor w klasie?
#
# A) Inicjalizuje nowo tworzone obiekty i przypisuje im początkowe wartości.
# B) Definiuje metody klasy.
# C) Niszczy obiekty klasy.
# D) Tworzy kopie obiektów klasy.

q = "Jaką rolę pełni konstruktor w klasie?"
a = [
    "Inicjalizuje nowo tworzone obiekty i przypisuje im początkowe wartości.",
    "Definiuje metody klasy.",
    "Niszczy obiekty klasy.",
    "Tworzy kopie obiektów klasy.",
]
questions.append({"question": q, "answers": a})

q = "Co to jest konstruktor klasy w Pythonie?"
a = [
    "Metoda __init__, która jest wywoływana, kiedy tworzony jest nowy obiekt klasy",
    "Funkcja, która tworzy nowe zmienne",
    "Klasa, która tworzy nowe obiekty",
    "Funkcja, która niszczy obiekty",
]
questions.append({"question": q, "answers": a})

# Co to jest metoda statyczna w kontekście programowania obiektowego?
#
# A) Jest to metoda, która jest powiązana z klasą, a nie z instancją klasy.
# B) Jest to metoda, która jest powiązana tylko z konkretnym obiektem.
# C) Jest to metoda, która nie może być dziedziczona.
# D) Jest to metoda, która jest automatycznie wywoływana przy tworzeniu obiektu.

q = "Co to jest metoda statyczna w kontekście programowania obiektowego?"
a = [
    "Jest to metoda, która jest powiązana z klasą, a nie z instancją klasy.",
    "Jest to metoda, która jest powiązana tylko z konkretnym obiektem.",
    "Jest to metoda, która nie może być dziedziczona.",
    "Jest to metoda, która jest automatycznie wywoływana przy tworzeniu obiektu.",
]
questions.append({"question": q, "answers": a})

# Kiedy metody statyczne są zwykle używane w programowaniu obiektowym?
#
# A) Kiedy metoda nie wymaga dostępu do konkretnych danych obiektu i może być wywołana na poziomie klasy.
# B) Kiedy metoda powinna być wywoływana tylko dla konkretnej instancji.
# C) Kiedy metoda powinna być dziedziczona przez wszystkie podklasy.
# D) Kiedy metoda powinna być automatycznie wywoływana przy tworzeniu obiektu.

q = "Kiedy metody statyczne są zwykle używane w programowaniu obiektowym?"
a = [
    "Kiedy metoda nie wymaga dostępu do konkretnych danych obiektu i może być wywołana na poziomie klasy.",
    "Kiedy metoda powinna być wywoływana tylko dla konkretnej instancji.",
    "Kiedy metoda powinna być dziedziczona przez wszystkie podklasy.",
    "Kiedy metoda powinna być automatycznie wywoływana przy tworzeniu obiektu.",
]
questions.append({"question": q, "answers": a})

q = "Co to jest metoda statyczna w Pythonie?"
a = [
    "Metoda powiązana z klasą, a nie z konkretną instancją klasy, nie ma dostępu do żadnego stanu obiektu",
    "Metoda, która nie może być dziedziczona",
    "Metoda, która nie może być przeciążona",
    "Metoda, która jest zawsze wywoływana na początku programu",
]
questions.append({"question": q, "answers": a})

q = "Czym jest abstrakcja w kontekście programowania obiektowego w Pythonie?"
a = [
    "Procesem ukrywania szczegółów implementacji i pokazywania tylko funkcjonalności użytkownikowi",
    "Techniką optymalizacji kodu",
    "Procesem tworzenia nowych modułów",
    "Sposobem zarządzania pamięcią",
]
questions.append({"question": q, "answers": a})

# Jaką rolę pełni abstrakcja w programowaniu obiektowym?
#
# A) Ułatwia zarządzanie złożonymi systemami, ukrywając nieistotne szczegóły i pokazując tylko istotne informacje.
# B) Umożliwia tworzenie wielu kopii tego samego obiektu.
# C) Zapewnia, że wszystkie obiekty muszą mieć ten sam zestaw atrybutów.
# D) Wymusza, aby wszystkie klasy dziedziczyły wszystkie metody i atrybuty klasy bazowej.

q = "Jaką rolę pełni abstrakcja w programowaniu obiektowym?"
a = [
    "Ułatwia zarządzanie złożonymi systemami, ukrywając nieistotne szczegóły i pokazując tylko istotne informacje.",
    "Umożliwia tworzenie wielu kopii tego samego obiektu.",
    "Zapewnia, że wszystkie obiekty muszą mieć ten sam zestaw atrybutów.",
    "Wymusza, aby wszystkie klasy dziedziczyły wszystkie metody i atrybuty klasy bazowej.",
]
questions.append({"question": q, "answers": a})

# Co to jest hermetyzacja (enkapsulacja) w kontekście programowania obiektowego?
#
# A) Jest to proces ukrywania wewnętrznych szczegółów obiektów i zapewniania publicznych metod do manipulowania tymi obiektami.
# B) Jest to proces tworzenia konkretnych instancji obiektów.
# C) Jest to proces tworzenia metody statycznej.
# D) Jest to proces, w którym klasa pochodna dziedziczy pola i metody klasy bazowej.

q = "Co to jest hermetyzacja (enkapsulacja) w kontekście programowania obiektowego?"
a = [
    "Jest to proces ukrywania wewnętrznych szczegółów obiektów i zapewniania publicznych metod do manipulowania tymi obiektami.",
    "Jest to proces tworzenia konkretnych instancji obiektów.",
    "Jest to proces tworzenia metody statycznej.",
    "Jest to proces, w którym klasa pochodna dziedziczy pola i metody klasy bazowej.",
]
questions.append({"question": q, "answers": a})

q = "Co to jest dziedziczenie w Pythonie?"
a = [
    "Mechanizm pozwalający jednej klasie przejąć atrybuty i metody innej klasy",
    "Mechanizm zamiany jednego typu obiektu na inny",
    "Technika tworzenia nowych modułów",
    "Sposób przypisywania wartości do zmiennych",
]
questions.append({"question": q, "answers": a})


# Jaką rolę pełni dziedziczenie w programowaniu obiektowym?
#
# A) Umożliwia ponowne użycie kodu, ułatwiając tworzenie i zarządzanie złożonymi programami.
# B) Kontroluje, jakie dane mogą być dostępne i modyfikowane przez kod poza klasą.
# C) Zapewnia, że wszystkie obiekty muszą mieć ten sam zestaw atrybutów.
# D) Wymusza, aby wszystkie klasy dziedziczyły wszystkie metody i atrybuty klasy bazowej.

q = "Jaką rolę pełni dziedziczenie w programowaniu obiektowym?"
a = [
    "Umożliwia ponowne użycie kodu, ułatwiając tworzenie i zarządzanie złożonymi programami.",
    "Kontroluje, jakie dane mogą być dostępne i modyfikowane przez kod poza klasą.",
    "Zapewnia, że wszystkie obiekty muszą mieć ten sam zestaw atrybutów.",
    "Wymusza, aby wszystkie klasy dziedziczyły wszystkie metody i atrybuty klasy bazowej.",
]
questions.append({"question": q, "answers": a})

# Co to jest modularyzacja w kontekście programowania?
#
# A) Jest to proces podziału programu na mniejsze, niezależne części (moduły), które mogą być oddzielnie opracowane i testowane.
# B) Jest to proces tworzenia konkretnych instancji obiektów.
# C) Jest to proces ukrywania wewnętrznych szczegółów obiektów.
# D) Jest to proces, w którym klasa pochodna dziedziczy pola i metody klasy bazowej.

q = "Co to jest modularyzacja w kontekście programowania?"
a = [
    "Jest to proces podziału programu na mniejsze, niezależne części (moduły), które mogą być oddzielnie opracowane i testowane.",
    "Jest to proces tworzenia konkretnych instancji obiektów.",
    "Jest to proces ukrywania wewnętrznych szczegółów obiektów.",
    "Jest to proces, w którym klasa pochodna dziedziczy pola i metody klasy bazowej.",
]
questions.append({"question": q, "answers": a})

# Jaką rolę pełni modularyzacja w programowaniu?
#
# A) Ułatwia zarządzanie i rozwój kodu, poprawiając jego czytelność, ponowne użycie i łatwość utrzymania.
# B) Kontroluje, jakie dane mogą być dostępne i modyfikowane przez kod poza modułem.
# C) Zapewnia, że wszystkie moduły muszą mieć ten sam zestaw funkcji.
# D) Wymusza, aby wszystkie moduły dziedziczyły wszystkie funkcje i atrybuty modułu bazowego.

q = "Jaką rolę pełni modularyzacja w programowaniu?"
a = [
    "Ułatwia zarządzanie i rozwój kodu, poprawiając jego czytelność, ponowne użycie i łatwość utrzymania.",
    "Kontroluje, jakie dane mogą być dostępne i modyfikowane przez kod poza modułem.",
    "Zapewnia, że wszystkie moduły muszą mieć ten sam zestaw funkcji.",
    "Wymusza, aby wszystkie moduły dziedziczyły wszystkie funkcje i atrybuty modułu bazowego.",
]

# Co to jest dekorator w Pythonie?
#
# A) Jest to specjalny typ funkcji, który pozwala na modyfikowanie zachowania innej funkcji lub klasy.
# B) Jest to proces tworzenia konkretnych instancji obiektów.
# C) Jest to funkcja, która jest automatycznie wywoływana podczas tworzenia obiektu.
# D) Jest to metoda, która pozwala na tworzenie statycznych metod.

q = "Co to jest dekorator w Pythonie?"
a = [
    "Jest to specjalny typ funkcji, który pozwala na modyfikowanie zachowania innej funkcji lub klasy.",
    "Jest to proces tworzenia konkretnych instancji obiektów.",
    "Jest to funkcja, która jest automatycznie wywoływana podczas tworzenia obiektu.",
    "Jest to metoda, która pozwala na tworzenie statycznych metod.",
]
questions.append({"question": q, "answers": a})

# Jaką rolę pełnią dekoratory w Pythonie?
#
# A) Pozwalają na dodanie nowej funkcjonalności do istniejących obiektów (funkcji, klas) bez modyfikowania ich kodu.
# B) Kontrolują, jakie dane mogą być dostępne i modyfikowane przez kod poza funkcją lub klasą.
# C) Zapewniają, że wszystkie funkcje lub klasy muszą mieć ten sam zestaw atrybutów.
# D) Wymuszają, aby wszystkie funkcje lub klasy dziedziczyły wszystkie atrybuty i metody klasy bazowej.

q = "Jaką rolę pełnią dekoratory w Pythonie?"
a = [
    "Pozwalają na dodanie nowej funkcjonalności do istniejących obiektów (funkcji, klas) bez modyfikowania ich kodu.",
    "Kontrolują, jakie dane mogą być dostępne i modyfikowane przez kod poza funkcją lub klasą.",
    "Zapewniają, że wszystkie funkcje lub klasy muszą mieć ten sam zestaw atrybutów.",
    "Wymuszają, aby wszystkie funkcje lub klasy dziedziczyły wszystkie atrybuty i metody klasy bazowej.",
]
questions.append({"question": q, "answers": a})

# Co to jest setter w kontekście programowania obiektowego?
#
# A) Jest to metoda używana do ustawiania wartości atrybutu obiektu.
# B) Jest to metoda, która jest automatycznie wywoływana podczas tworzenia obiektu.
# C) Jest to proces tworzenia konkretnych instancji obiektów.
# D) Jest to metoda, która pozwala na tworzenie statycznych metod.

q = "Co to jest setter w kontekście programowania obiektowego?"
a = [
    "Jest to metoda używana do ustawiania wartości atrybutu obiektu.",
    "Jest to metoda, która jest automatycznie wywoływana podczas tworzenia obiektu.",
    "Jest to proces tworzenia konkretnych instancji obiektów.",
    "Jest to metoda, która pozwala na tworzenie statycznych metod.",
]
questions.append({"question": q, "answers": a})

# Jaką rolę pełni setter w programowaniu obiektowym?
#
# A) Pozwala na kontrolę sposobu, w jaki wartości są przypisywane do atrybutów obiektu, na przykład poprzez walidację danych wejściowych lub wykonanie dodatkowych działań podczas ustawiania wartości.
# B) Kontroluje, jakie dane mogą być dostępne i modyfikowane przez kod poza obiektem.
# C) Zapewnia, że wszystkie obiekty muszą mieć ten sam zestaw atrybutów.
# D) Wymusza, aby wszystkie obiekty dziedziczyły wszystkie metody i atrybuty klasy bazowej.

q = "Jaką rolę pełni setter w programowaniu obiektowym?"
a = [
    "Pozwala na kontrolę sposobu, w jaki wartości są przypisywane do atrybutów obiektu, na przykład poprzez walidację danych wejściowych lub wykonanie dodatkowych działań podczas ustawiania wartości.",
    "Kontroluje, jakie dane mogą być dostępne i modyfikowane przez kod poza obiektem.",
    "Zapewnia, że wszystkie obiekty muszą mieć ten sam zestaw atrybutów.",
    "Wymusza, aby wszystkie obiekty dziedziczyły wszystkie metody i atrybuty klasy bazowej.",
]
questions.append({"question": q, "answers": a})

q = "Jak nazywamy funkcję, która jest wywoływana, gdy próbujemy odczytać wartość atrybutu obiektu w Pythonie?"
a = ["Getter", "Setter", "Property", "Dekorator"]
questions.append({"question": q, "answers": a})

# Co to jest getter w kontekście programowania obiektowego?
#
# A) Jest to metoda używana do uzyskiwania wartości atrybutu obiektu.
# B) Jest to specjalny rodzaj konstruktora używanego do tworzenia obiektów.
# C) Jest to metoda, która zawsze zwraca wartość stałą.
# D) Jest to metoda służąca do porównywania dwóch obiektów.

q = "Co to jest getter w kontekście programowania obiektowego?"
a = [
    "Jest to metoda używana do uzyskiwania wartości atrybutu obiektu.",
    "Jest to specjalny rodzaj konstruktora używanego do tworzenia obiektów.",
    "Jest to metoda, która zawsze zwraca wartość stałą.",
    "Jest to metoda służąca do porównywania dwóch obiektów.",
]
questions.append({"question": q, "answers": a})

# Jaką rolę pełni getter w programowaniu obiektowym?
#
# A) Umożliwia kontrolę nad tym, jak atrybuty obiektu są dostępne dla kodu poza obiektem.
# B) Pozwala na modyfikowanie atrybutów obiektu bez konieczności wywoływania metody.
# C) Umożliwia tworzenie obiektów o identycznych atrybutach.
# D) Umożliwia tworzenie metod, które zawsze zwracają wartość stałą.

q = "Jaką rolę pełni getter w programowaniu obiektowym?"
a = [
    "Umożliwia kontrolę nad tym, jak atrybuty obiektu są dostępne dla kodu poza obiektem.",
    "Pozwala na modyfikowanie atrybutów obiektu bez konieczności wywoływania metody.",
    "Umożliwia tworzenie obiektów o identycznych atrybutach.",
    "Umożliwia tworzenie metod, które zawsze zwracają wartość stałą.",
]
questions.append({"question": q, "answers": a})

# Co to jest dekorator property w Pythonie?
#
# A) Jest to wbudowany dekorator, który pozwala na definiowanie getterów i setterów w obrębie klasy.
# B) Jest to narzędzie do tworzenia funkcji anonimowych.
# C) Jest to mechanizm, który pozwala na modyfikację składni wywołania funkcji.
# D) Jest to dekorator, który zmienia zasięg zmiennej.

q = "Co to jest property w Pythonie?"
a = [
    "Dekorator umożliwiający definiowanie metod dostępu do atrybutu klasy",
    "Wartość przechowywana w obiekcie",
    "Typ danych",
    "Nazwa metody",
]
questions.append({"question": q, "answers": a})

q = "Co to jest dekorator property w Pythonie?"
a = [
    "Jest to wbudowany dekorator, który pozwala na definiowanie getterów i setterów w obrębie klasy.",
    "Jest to narzędzie do tworzenia funkcji anonimowych.",
    "Jest to mechanizm, który pozwala na modyfikację składni wywołania funkcji.",
    "Jest to dekorator, który zmienia zasięg zmiennej.",
]
questions.append({"question": q, "answers": a})

# Jaką rolę pełni dekorator property w Pythonie?
#
# A) Pozwala na tworzenie metod klasy, które można wywoływać jak atrybuty, umożliwiając kontrolę nad ich odczytem i zapisem.
# B) Pozwala na tworzenie funkcji, które są automatycznie wywoływane przy starcie programu.
# C) Zmienia sposób, w jaki Python interpretuje wywołania funkcji.
# D) Umożliwia tworzenie funkcji, które są automatycznie wywoływane przy zakończeniu programu.

q = "Jaką rolę pełni dekorator property w Pythonie?"
a = [
    "Pozwala na tworzenie metod klasy, które można wywoływać jak atrybuty, umożliwiając kontrolę nad ich odczytem i zapisem.",
    "Pozwala na tworzenie funkcji, które są automatycznie wywoływane przy starcie programu.",
    "Zmienia sposób, w jaki Python interpretuje wywołania funkcji.",
    "Umożliwia tworzenie funkcji, które są automatycznie wywoływane przy zakończeniu programu.",
]
questions.append({"question": q, "answers": a})

# Jak w Pythonie zdefiniować coś podobnego do interfejsu znanych z innych języków?
#
# A) Używając klas abstrakcyjnych z modułu abc i definiując metody abstrakcyjne.
# B) Definiując klasę z samymi metodami statycznymi.
# C) Tworząc klasę bez żadnych metod i atrybutów.
# D) Używając dekoratora @interface na klasie.

q = "Jak w Pythonie zdefiniować coś podobnego do interfejsu znanych z innych języków?"
a = [
    "Używając klas abstrakcyjnych z modułu abc i definiując metody abstrakcyjne.",
    "Definiując klasę z samymi metodami statycznymi.",
    "Tworząc klasę bez żadnych metod i atrybutów.",
    "Używając dekoratora @interface na klasie.",
]
questions.append({"question": q, "answers": a})

# Jaka jest rola "interfejsów" (klas abstrakcyjnych) w Pythonie?
#
# A) Definiują one szablon dla klas, wymuszając implementację określonych metod.
# B) Pozwalają na tworzenie obiektów bez konieczności implementowania jakichkolwiek metod.
# C) Zmieniają sposób, w jaki Python interpretuje wywołania funkcji.
# D) Pozwalają na tworzenie funkcji, które są automatycznie wywoływane przy zakończeniu programu.

q = 'Jaka jest rola "interfejsów" (klas abstrakcyjnych) w Pythonie?'
a = [
    "Definiują one szablon dla klas, wymuszając implementację określonych metod.",
    "Pozwalają na tworzenie obiektów bez konieczności implementowania jakichkolwiek metod.",
    "Zmieniają sposób, w jaki Python interpretuje wywołania funkcji.",
    "Pozwalają na tworzenie funkcji, które są automatycznie wywoływane przy zakończeniu programu.",
]
questions.append({"question": q, "answers": a})

# Co to jest metoda abstrakcyjna w Pythonie?
#
# A) Jest to metoda zadeklarowana w klasie abstrakcyjnej, która nie ma implementacji i musi zostać zaimplementowana przez każdą klasę dziedziczącą.
# B) Jest to metoda, która zawsze zwraca wartość None.
# C) Jest to metoda, która nie może zostać zaimplementowana przez klasę dziedziczącą.
# D) Jest to metoda, która automatycznie tworzy obiekty klasy.

q = "Co to jest metoda abstrakcyjna w Pythonie?"
a = [
    "Jest to metoda zadeklarowana w klasie abstrakcyjnej, która nie ma implementacji i musi zostać zaimplementowana przez każdą klasę dziedziczącą.",
    "Jest to metoda, która zawsze zwraca wartość None.",
    "Jest to metoda, która nie może zostać zaimplementowana przez klasę dziedziczącą.",
    "Jest to metoda, która automatycznie tworzy obiekty klasy.",
]
questions.append({"question": q, "answers": a})

# Jaką rolę pełnią metody abstrakcyjne w Pythonie?
#
# A) Definiują one interfejs dla klas dziedziczących, wymuszając implementację tych metod.
# B) Pozwalają na tworzenie metod, które nie mają żadnej funkcjonalności.
# C) Umożliwiają automatyczne tworzenie obiektów klasy.
# D) Pozwalają na tworzenie metod, które są automatycznie wywoływane przy zakończeniu programu.

q = "Jaką rolę pełnią metody abstrakcyjne w Pythonie?"
a = [
    "Definiują one interfejs dla klas dziedziczących, wymuszając implementację tych metod.",
    "Pozwalają na tworzenie metod, które nie mają żadnej funkcjonalności.",
    "Umożliwiają automatyczne tworzenie obiektów klasy.",
    "Pozwalają na tworzenie metod, które są automatycznie wywoływane przy zakończeniu programu.",
]
questions.append({"question": q, "answers": a})

q = "Jakie kolory są obsługiwane w standardzie RGB używanym w OpenGL?"
a = [
    "Czerwony, zielony, niebieski",
    "Cyan, magenta, żółty",
    "Czerwony, pomarańczowy, żółty",
    "Biały, czarny, szary",
]
questions.append({"question": q, "answers": a})

# Czym jest modelowanie w kontekście grafiki komputerowej?
#
# A) Jest to proces tworzenia obiektów 3D, które są potem używane w scenach graficznych.
# B) Jest to proces przekształcania modeli 3D w obrazy 2D.
# C) Jest to proces dodawania ruchu do modeli 3D.
# D) Jest to proces optymalizacji grafiki komputerowej.

q = "Czym jest modelowanie w kontekście grafiki komputerowej?"
a = [
    "Jest to proces tworzenia obiektów 3D, które są potem używane w scenach graficznych.",
    "Jest to proces przekształcania modeli 3D w obrazy 2D.",
    "Jest to proces dodawania ruchu do modeli 3D.",
    "Jest to proces optymalizacji grafiki komputerowej.",
]
questions.append({"question": q, "answers": a})

# Czym jest renderowanie i animacja w kontekście grafiki komputerowej?
#
# A) Renderowanie to proces przekształcania modeli 3D w obrazy 2D, a animacja to proces dodawania ruchu do modeli 3D.
# B) Renderowanie to proces tworzenia obiektów 3D, a animacja to proces przekształcania modeli 3D w obrazy 2D.
# C) Renderowanie to proces dodawania ruchu do modeli 3D, a animacja to proces tworzenia obiektów 3D.
# D) Renderowanie to proces optymalizacji grafiki komputerowej, a animacja to proces tworzenia efektów dźwiękowych.

q = "Czym jest renderowanie i animacja w kontekście grafiki komputerowej?"
a = [
    "Renderowanie to proces przekształcania modeli 3D w obrazy 2D, a animacja to proces dodawania ruchu do modeli 3D.",
    "Renderowanie to proces tworzenia obiektów 3D, a animacja to proces przekształcania modeli 3D w obrazy 2D.",
    "Renderowanie to proces dodawania ruchu do modeli 3D, a animacja to proces tworzenia obiektów 3D.",
    "Renderowanie to proces optymalizacji grafiki komputerowej, a animacja to proces tworzenia efektów dźwiękowych.",
]
questions.append({"question": q, "answers": a})

# Jak nazywamy proces tworzenia obiektów 3D w grafice komputerowej?
#
# A) Modelowanie
# B) Renderowanie
# C) Animacja
# D) Optymalizacja

q = "Jak nazywamy proces tworzenia obiektów 3D w grafice komputerowej?"
a = ["Modelowanie", "Renderowanie", "Animacja", "Optymalizacja"]
questions.append({"question": q, "answers": a})

# Który z procesów grafiki komputerowej przekształca modele 3D w obrazy 2D?
#
# A) Renderowanie
# B) Modelowanie
# C) Animacja
# D) Teksturowanie

q = "Który z procesów grafiki komputerowej przekształca modele 3D w obrazy 2D?"
a = ["Renderowanie", "Modelowanie", "Animacja", "Teksturowanie"]
questions.append({"question": q, "answers": a})

# Który z filarów grafiki komputerowej odpowiada za dodawanie ruchu do modeli 3D?
#
# A) Animacja
# B) Renderowanie
# C) Modelowanie
# D) Skalowanie

q = "Który z filarów grafiki komputerowej odpowiada za dodawanie ruchu do modeli 3D?"
a = ["Animacja", "Renderowanie", "Modelowanie", "Skalowanie"]
questions.append({"question": q, "answers": a})

q = "Co to jest OpenGL?"
a = [
    "API do renderowania grafiki 2D i 3D",
    "Język programowania",
    "Środowisko uruchomieniowe",
    "Narzędzie do tworzenia stron internetowych",
]
questions.append({"question": q, "answers": a})

# Czym jest OpenGL?
#
# A) Jest to wieloplatformowa biblioteka do tworzenia grafiki 2D i 3D.
# B) Jest to język programowania do tworzenia aplikacji webowych.
# C) Jest to środowisko do tworzenia gier komputerowych.
# D) Jest to system zarządzania bazami danych.

q = "Czym jest OpenGL?"
a = [
    "Jest to wieloplatformowa biblioteka do tworzenia grafiki 2D i 3D.",
    "Jest to język programowania do tworzenia aplikacji webowych.",
    "Jest to środowisko do tworzenia gier komputerowych.",
    "Jest to system zarządzania bazami danych.",
]
questions.append({"question": q, "answers": a})

# Jaką rolę pełni OpenGL w tworzeniu grafiki komputerowej?
#
# A) Umożliwia tworzenie i manipulowanie grafiką 2D i 3D.
# B) Umożliwia tworzenie stron internetowych z grafiką interaktywną.
# C) Umożliwia tworzenie animacji 2D dla filmów i seriali animowanych.
# D) Umożliwia tworzenie baz danych graficznych.

q = "Jaką rolę pełni OpenGL w tworzeniu grafiki komputerowej?"
a = [
    "Umożliwia tworzenie i manipulowanie grafiką 2D i 3D.",
    "Umożliwia tworzenie stron internetowych z grafiką interaktywną.",
    "Umożliwia tworzenie animacji 2D dla filmów i seriali animowanych.",
    "Umożliwia tworzenie baz danych graficznych.",
]
questions.append({"question": q, "answers": a})

# Czy OpenGL jest ograniczony do jednej platformy systemowej?
#
# A) Nie, OpenGL jest biblioteką wieloplatformową i może być używany na różnych systemach operacyjnych.
# B) Tak, OpenGL może być używany tylko na systemach operacyjnych Windows.
# C) Tak, OpenGL może być używany tylko na systemach operacyjnych Linux.
# D) Tak, OpenGL może być używany tylko na systemach operacyjnych Mac OS.

q = "Czy OpenGL jest ograniczony do jednej platformy systemowej?"
a = [
    "Nie, OpenGL jest biblioteką wieloplatformową i może być używany na różnych systemach operacyjnych.",
    "Tak, OpenGL może być używany tylko na systemach operacyjnych Windows.",
    "Tak, OpenGL może być używany tylko na systemach operacyjnych Linux.",
    "Tak, OpenGL może być używany tylko na systemach operacyjnych Mac OS.",
]
questions.append({"question": q, "answers": a})

# Czym jest dynamiczny potok (dynamic pipeline) w kontekście nowoczesnego OpenGL?
#
# A) Jest to elastyczny i konfigurowalny potok renderowania, który umożliwia dynamiczną zmianę stanu renderowania w czasie rzeczywistym.
# B) Jest to rodzaj animacji używanej w grafice komputerowej do tworzenia płynnych ruchów.
# C) Jest to złożony proces przetwarzania obrazu, który stosuje efekty specjalne na teksturach.
# D) Jest to moduł do ładowania i renderowania modeli 3D w nowoczesnym OpenGL.

q = "Czym jest dynamiczny potok (dynamic pipeline) w kontekście nowoczesnego OpenGL?"
a = [
    "Jest to elastyczny i konfigurowalny potok renderowania, który umożliwia dynamiczną zmianę stanu renderowania w czasie rzeczywistym.",
    "Jest to rodzaj animacji używanej w grafice komputerowej do tworzenia płynnych ruchów.",
    "Jest to złożony proces przetwarzania obrazu, który stosuje efekty specjalne na teksturach.",
    "Jest to moduł do ładowania i renderowania modeli 3D w nowoczesnym OpenGL.",
]
questions.append({"question": q, "answers": a})

# Jaką rolę pełni dynamiczny potok w nowoczesnym OpenGL?
#
# A) Umożliwia programistom dostosowywanie i modyfikowanie różnych etapów procesu renderowania, takich jak załadowanie shaderów, przekształcenia geometryczne i rasteryzacja.
# B) Kontroluje, jakie tekstury i materiały są używane w procesie renderowania.
# C) Ogranicza ilość przetwarzania, aby zoptymalizować wydajność renderowania.
# D) Zapewnia, że modele 3D są renderowane w czasie rzeczywistym.

q = "Jaką rolę pełni dynamiczny potok w nowoczesnym OpenGL?"
a = [
    "Umożliwia programistom dostosowywanie i modyfikowanie różnych etapów procesu renderowania, takich jak załadowanie shaderów, przekształcenia geometryczne i rasteryzacja.",
    "Kontroluje, jakie tekstury i materiały są używane w procesie renderowania.",
    "Ogranicza ilość przetwarzania, aby zoptymalizować wydajność renderowania.",
    "Zapewnia, że modele 3D są renderowane w czasie rzeczywistym.",
]
questions.append({"question": q, "answers": a})

# Czym jest moduł wierzchołków (vertex shader) w OpenGL?
#
# A) Jest to program, który przetwarza pojedyncze wierzchołki geometrii w przestrzeni 3D.
# B) Jest to specjalny rodzaj tekstury używanej do renderowania obiektów.
# C) Jest to technika renderowania, która zapewnia oświetlenie obiektów.
# D) Jest to algorytm odpowiedzialny za utworzenie drzewa sceny.

q = "Czym jest moduł wierzchołków (vertex shader) w OpenGL?"
a = [
    "Jest to program, który przetwarza pojedyncze wierzchołki geometrii w przestrzeni 3D.",
    "Jest to specjalny rodzaj tekstury używanej do renderowania obiektów.",
    "Jest to technika renderowania, która zapewnia oświetlenie obiektów.",
    "Jest to algorytm odpowiedzialny za utworzenie drzewa sceny.",
]
questions.append({"question": q, "answers": a})

# Czym jest moduł fragmentów (fragment shader) w OpenGL?
#
# A) Jest to program, który przetwarza piksele, które zostaną wyrenderowane na ekranie.
# B) Jest to specjalny rodzaj tekstury używanej do renderowania obiektów.
# C) Jest to technika renderowania, która odpowiada za rasteryzację obiektów.
# D) Jest to algorytm odpowiedzialny za optymalizację przetwarzania grafiki.

q = "Czym jest moduł fragmentów (fragment shader) w OpenGL?"
a = [
    "Jest to program, który przetwarza piksele, które zostaną wyrenderowane na ekranie.",
    "Jest to specjalny rodzaj tekstury używanej do renderowania obiektów.",
    "Jest to technika renderowania, która odpowiada za rasteryzację obiektów.",
    "Jest to algorytm odpowiedzialny za optymalizację przetwarzania grafiki.",
]
questions.append({"question": q, "answers": a})

# Jaki jest główny cel modułu wierzchołków w OpenGL?
#
# A) Przekształcanie wierzchołków 3D z przestrzeni modelu na przestrzeń ekranu.
# B) Generowanie oświetlenia dla obiektów 3D.
# C) Wykonywanie operacji logicznych na pikselach.
# D) Renderowanie tekstur na obiekty.

q = "Jaki jest główny cel modułu wierzchołków w OpenGL?"
a = [
    "Przekształcanie wierzchołków 3D z przestrzeni modelu na przestrzeń ekranu.",
    "Generowanie oświetlenia dla obiektów 3D.",
    "Wykonywanie operacji logicznych na pikselach.",
    "Renderowanie tekstur na obiekty.",
]
questions.append({"question": q, "answers": a})

# Czym jest GLSL?
#
# A) Jest to język programowania używany w OpenGL do definiowania modułów cieniujących.
# B) Jest to język programowania do tworzenia interfejsów graficznych.
# C) Jest to specjalny efekt wizualny używany w grafice komputerowej.
# D) Jest to skrót od "Global Shader Library" - globalnej biblioteki cieniowania.

q = "Czym jest GLSL?"
a = [
    "Jest to język programowania używany w OpenGL do definiowania modułów cieniujących.",
    "Jest to język programowania do tworzenia interfejsów graficznych.",
    "Jest to specjalny efekt wizualny używany w grafice komputerowej.",
    'Jest to skrót od "Global Shader Library" - globalnej biblioteki cieniowania.',
]
questions.append({"question": q, "answers": a})

# Jakie są główne zadania GLSL?
#
# A) Definiuje i kontroluje moduły cieniujące używane w procesie renderowania.
# B) Odpowiada za ładowanie tekstur i materiałów do obiektów graficznych.
# C) Steruje animacją obiektów 3D.
# D) Odpowiada za generowanie grafiki wektorowej w czasie rzeczywistym.

q = "Jakie są główne zadania GLSL?"
a = [
    "Definiuje i kontroluje moduły cieniujące używane w procesie renderowania.",
    "Odpowiada za ładowanie tekstur i materiałów do obiektów graficznych.",
    "Steruje animacją obiektów 3D.",
    "Odpowiada za generowanie grafiki wektorowej w czasie rzeczywistym.",
]
questions.append({"question": q, "answers": a})

# Co to jest biblioteka Vispy?
#
# A) Jest to biblioteka do tworzenia interaktywnej grafiki 2D i 3D w Pythonie.
# B) Jest to biblioteka do tworzenia baz danych w Pythonie.
# C) Jest to biblioteka do manipulacji danymi tabelarycznymi w Pythonie.
# D) Jest to biblioteka do tworzenia gier komputerowych w Pythonie.

q = "Co to jest biblioteka Vispy?"
a = [
    "Jest to biblioteka do tworzenia interaktywnej grafiki 2D i 3D w Pythonie.",
    "Jest to biblioteka do tworzenia baz danych w Pythonie.",
    "Jest to biblioteka do manipulacji danymi tabelarycznymi w Pythonie.",
    "Jest to biblioteka do tworzenia gier komputerowych w Pythonie.",
]
questions.append({"question": q, "answers": a})

# Jakie są główne cechy biblioteki Vispy?
#
# A) Obsługa grafiki 2D i 3D, interaktywność, wydajność, wieloplatformowość.
# B) Tworzenie aplikacji webowych, komunikacja sieciowa, testowanie jednostkowe.
# C) Obsługa baz danych, zarządzanie plikami, generowanie raportów.
# D) Tworzenie sztucznej inteligencji, analiza danych, statystyka.

q = "Jakie są główne cechy biblioteki Vispy?"
a = [
    "Obsługa grafiki 2D i 3D, interaktywność, wydajność, wieloplatformowość.",
    "Tworzenie aplikacji webowych, komunikacja sieciowa, testowanie jednostkowe.",
    "Obsługa baz danych, zarządzanie plikami, generowanie raportów.",
    "Tworzenie sztucznej inteligencji, analiza danych, statystyka.",
]
questions.append({"question": q, "answers": a})

# Jakie są główne zastosowania biblioteki Vispy?
#
# A) Wizualizacja danych naukowych, grafika komputerowa, renderowanie interaktywnych wizualizacji.
# B) Tworzenie stron internetowych, programowanie aplikacji mobilnych, tworzenie gier.
# C) Analiza finansowa, zarządzanie projektami, obliczenia naukowe.
# D) Tworzenie sztucznej inteligencji, robotyka, analiza big data.

q = "Jakie są główne zastosowania biblioteki Vispy?"
a = [
    "Wizualizacja danych naukowych, grafika komputerowa, renderowanie interaktywnych wizualizacji.",
    "Tworzenie stron internetowych, programowanie aplikacji mobilnych, tworzenie gier.",
    "Analiza finansowa, zarządzanie projektami, obliczenia naukowe.",
    "Tworzenie sztucznej inteligencji, robotyka, analiza big data.",
]
questions.append({"question": q, "answers": a})

# Czy biblioteka Vispy jest darmowa i otwartoźródłowa?
#
# A) Tak, biblioteka Vispy jest darmowa i udostępniana na licencji otwartoźródłowej (open source).
# B) Nie, biblioteka Vispy jest płatna i wymaga licencji komercyjnej.
# C) Biblioteka Vispy jest częściowo darmowa, ale nie jest otwartoźródłowa.
# D) Biblioteka Vispy jest dostępna tylko w wersji próbnej, po której należy uiścić opłatę.

q = "Czy biblioteka Vispy jest darmowa i otwartoźródłowa?"
a = [
    "Tak, biblioteka Vispy jest darmowa i udostępniana na licencji otwartoźródłowej (open source).",
    "Nie, biblioteka Vispy jest płatna i wymaga licencji komercyjnej.",
    "Biblioteka Vispy jest częściowo darmowa, ale nie jest otwartoźródłowa.",
    "Biblioteka Vispy jest dostępna tylko w wersji próbnej, po której należy uiścić opłatę.",
]
questions.append({"question": q, "answers": a})

# Jakie są wymagania dotyczące instalacji biblioteki Vispy?
#
# A) Wymaga instalacji Pythona oraz zależności takich jak NumPy i PyOpenGL.
# B) Wymaga posiadania specjalnego sprzętu komputerowego, takiego jak karta graficzna.
# C) Wymaga zakupu licencji przed instalacją.
# D) Wymaga jedynie instalacji odpowiedniego menedżera pakietów w Pythonie.

q = "Jakie są wymagania dotyczące instalacji biblioteki Vispy?"
a = [
    "Wymaga instalacji Pythona oraz zależności takich jak NumPy i PyOpenGL.",
    "Wymaga posiadania specjalnego sprzętu komputerowego, takiego jak karta graficzna.",
    "Wymaga zakupu licencji przed instalacją.",
    "Wymaga jedynie instalacji odpowiedniego menedżera pakietów w Pythonie.",
]
questions.append({"question": q, "answers": a})

# Jak tworzyć aplikacje okienkowe w bibliotece Vispy?
#
# A) Korzystając z klasy Canvas lub SceneCanvas.
# B) Używając modułu vispy.app.
# C) Poprzez utworzenie obiektu vispy.window.Window.
# D) Aplikacje okienkowe nie są obsługiwane w bibliotece Vispy.

q = "Jak tworzyć aplikacje okienkowe w bibliotece Vispy?"
a = [
    "Korzystając z klasy Canvas lub SceneCanvas.",
    "Używając modułu vispy.app.",
    "Poprzez utworzenie obiektu vispy.window.Window.",
    "Aplikacje okienkowe nie są obsługiwane w bibliotece Vispy.",
]
questions.append({"question": q, "answers": a})

# Jak obsługiwać zdarzenia w bibliotece Vispy?
#
# A) Poprzez przypisanie funkcji obsługującej zdarzenie do odpowiedniego atrybutu obiektu wizualizacji.
# B) Korzystając z modułu vispy.event.
# C) Używając funkcji vispy.event.connect.
# D) Obsługa zdarzeń nie jest obsługiwana w bibliotece Vispy.

q = "Jak obsługiwać zdarzenia w bibliotece Vispy?"
a = [
    "Poprzez przypisanie funkcji obsługującej zdarzenie do odpowiedniego atrybutu obiektu wizualizacji.",
    "Korzystając z modułu vispy.event.",
    "Używając funkcji vispy.event.connect.",
    "Obsługa zdarzeń nie jest obsługiwana w bibliotece Vispy.",
]
questions.append({"question": q, "answers": a})

# Jak renderować grafikę z wykorzystaniem modułów cieniujących w bibliotece Vispy?
#
# A) Korzystając z obiektów vispy.gloo.Program i vispy.gloo.Shader.
# B) Używając funkcji vispy.gloo.compile_program.
# C) Poprzez korzystanie z funkcji vispy.gloo.set_shaders.
# D) Renderowanie z użyciem modułów cieniujących nie jest obsługiwane w bibliotece Vispy.

q = "Jak renderować grafikę z wykorzystaniem modułów cieniujących w bibliotece Vispy?"
a = [
    "Korzystając z obiektów vispy.gloo.Program",
    "Używając funkcji vispy.gloo.compile_program.",
    "Poprzez korzystanie z funkcji vispy.gloo.set_shaders.",
    "Renderowanie z użyciem modułów cieniujących nie jest obsługiwane w bibliotece Vispy.",
]
questions.append({"question": q, "answers": a})

# Co to jest bufor danych (data buffer) w bibliotece Vispy?
#
# A) Jest to obszar pamięci, w którym przechowywane są dane, takie jak pozycje wierzchołków lub kolory.
# B) Bufor danych w Vispy jest odpowiedzialny za przechowywanie kodu źródłowego shaderów.
# C) Bufor danych odnosi się do tymczasowego bufora, w którym przechowywane są dane, zanim zostaną wyrenderowane.
# D) Bufor danych w bibliotece Vispy odnosi się do przechowywania danych wejściowych dla analizy statystycznej.

q = "Co to jest bufor danych (data buffer) w bibliotece Vispy?"
a = [
    "Jest to obszar pamięci, w którym przechowywane są dane, takie jak pozycje wierzchołków lub kolory.",
    "Bufor danych w Vispy jest odpowiedzialny za przechowywanie kodu źródłowego shaderów.",
    "Bufor danych odnosi się do tymczasowego bufora, w którym przechowywane są dane, zanim zostaną wyrenderowane.",
    "Bufor danych w bibliotece Vispy odnosi się do przechowywania danych wejściowych dla analizy statystycznej.",
]
questions.append({"question": q, "answers": a})

# Co to jest bufor indeksów (index buffer) w bibliotece Vispy?
#
# A) Jest to bufor przechowujący indeksy wierzchołków, które tworzą trójkąty lub inne prymitywy graficzne.
# B) Bufor indeksów w Vispy odnosi się do przechowywania informacji o kolejności renderowania obiektów.
# C) Bufor indeksów służy do przechowywania kodu źródłowego shaderów.
# D) Bufor indeksów jest odpowiedzialny za przechowywanie danych wejściowych dla analizy statystycznej.

q = "Co to jest bufor indeksów (index buffer) w bibliotece Vispy?"
a = [
    "Jest to bufor przechowujący indeksy wierzchołków, które tworzą trójkąty lub inne prymitywy graficzne.",
    "Bufor indeksów w Vispy odnosi się do przechowywania informacji o kolejności renderowania obiektów.",
    "Bufor indeksów służy do przechowywania kodu źródłowego shaderów.",
    "Bufor indeksów jest odpowiedzialny za przechowywanie danych wejściowych dla analizy statystycznej.",
]
questions.append({"question": q, "answers": a})

# Jakie jest główne zadanie modułu vispy.gloo w bibliotece Vispy?
#
# A) Jest to moduł odpowiedzialny za niskopoziomowe operacje graficzne i interakcję z modułami cieniującymi.
# B) Moduł vispy.gloo służy do obsługi zdarzeń w bibliotece Vispy.
# C) Jest to moduł do manipulacji danymi tabelarycznymi wizualizacji.
# D) vispy.gloo jest odpowiedzialne za tworzenie interfejsów graficznych wizualizacji.

q = "Jakie jest główne zadanie modułu vispy.gloo w bibliotece Vispy?"
a = [
    "Jest to moduł odpowiedzialny za niskopoziomowe operacje graficzne i interakcję z modułami cieniującymi.",
    "Moduł vispy.gloo służy do obsługi zdarzeń w bibliotece Vispy.",
    "Jest to moduł do manipulacji danymi tabelarycznymi wizualizacji.",
    "vispy.gloo jest odpowiedzialne za tworzenie interfejsów graficznych wizualizacji.",
]
questions.append({"question": q, "answers": a})

# Jaki jest główny cel modułu vispy.scene.transforms w bibliotece Vispy?
#
# A) Moduł vispy.scene.transforms służy do przekształceń geometrycznych obiektów w przestrzeni sceny.
# B) Jest to moduł do manipulacji danymi tabelarycznymi wizualizacji.
# C) vispy.scene.transforms jest odpowiedzialne za tworzenie interfejsów graficznych wizualizacji.
# D) Jest to moduł do obsługi zdarzeń w bibliotece Vispy.

q = "Jaki jest główny cel modułu vispy.scene.transforms w bibliotece Vispy?"
a = [
    "Moduł vispy.scene.transforms służy do przekształceń geometrycznych obiektów w przestrzeni sceny.",
    "Jest to moduł do manipulacji danymi tabelarycznymi wizualizacji.",
    "vispy.scene.transforms jest odpowiedzialne za tworzenie interfejsów graficznych wizualizacji.",
    "Jest to moduł do obsługi zdarzeń w bibliotece Vispy.",
]
questions.append({"question": q, "answers": a})

# Jakie są zadania modułu vispy.geometry.generation w bibliotece Vispy?
#
# A) Generowanie geometrii, takiej jak sześciany, sfera czy walec.
# B) Obsługa zdarzeń w bibliotece Vispy.
# C) Manipulacja danymi tabelarycznymi wizualizacji.
# D) Tworzenie interfejsów graficznych wizualizacji.

q = "Jakie są zadania modułu vispy.geometry.generation w bibliotece Vispy?"
a = [
    "Generowanie geometrii, takiej jak sześciany, sfera czy walec.",
    "Obsługa zdarzeń w bibliotece Vispy.",
    "Manipulacja danymi tabelarycznymi wizualizacji.",
    "Tworzenie interfejsów graficznych wizualizacji.",
]
questions.append({"question": q, "answers": a})

# Czy biblioteka Vispy obsługuje tworzenie aplikacji okienkowych, obsługę zdarzeń, renderowanie grafiki z wykorzystaniem modułów cieniujących, bufory danych, bufory indeksów, timer, moduł gloo, moduł transforms i moduł geometry.generation?
#
# A) Tak, biblioteka Vispy obsługuje wszystkie wymienione funkcje.
# B) Nie, biblioteka Vispy nie obsługuje renderowania grafiki z wykorzystaniem modułów cieniujących.
# C) Nie, biblioteka Vispy nie obsługuje obsługi zdarzeń.
# D) Nie, biblioteka Vispy nie obsługuje tworzenia aplikacji okienkowych.

q = "Czy biblioteka Vispy obsługuje tworzenie aplikacji okienkowych, obsługę zdarzeń, renderowanie grafiki z wykorzystaniem modułów cieniujących, bufory danych, bufory indeksów, timer, moduł gloo, moduł transforms i moduł geometry.generation?"
a = [
    "Tak, biblioteka Vispy obsługuje wszystkie wymienione funkcje.",
    "Nie, biblioteka Vispy nie obsługuje renderowania grafiki z wykorzystaniem modułów cieniujących.",
    "Nie, biblioteka Vispy nie obsługuje obsługi zdarzeń.",
    "Nie, biblioteka Vispy nie obsługuje tworzenia aplikacji okienkowych.",
]
questions.append({"question": q, "answers": a})

# Jakie są zastosowania zmiennych typu "attribute" w GLSL?
#
# A) Służą do przekazywania danych wierzchołków do modułów cieniujących.
# B) Przechowują stałe wartości używane w shaderach.
# C) Pozwalają na przesyłanie danych między różnymi shaderami.
# D) Umożliwiają manipulację teksturowaniem obiektów.

q = 'Jakie są zastosowania zmiennych typu "attribute" w GLSL?'
a = [
    "Służą do przekazywania danych wierzchołków do modułów cieniujących.",
    "Przechowują stałe wartości używane w shaderach.",
    "Pozwalają na przesyłanie danych między różnymi shaderami.",
    "Umożliwiają manipulację teksturowaniem obiektów.",
]
questions.append({"question": q, "answers": a})

# Do czego służą zmienne typu "varying" w GLSL?
#
# A) Pozwalają na przekazywanie danych między modułem wierzchołków a modułem fragmentów.
# B) Przechowują stałe wartości używane w shaderach.
# C) Służą do definiowania stałych dla całego programu.
# D) Umożliwiają manipulację oświetleniem w trakcie renderowania.

q = 'Do czego służą zmienne typu "varying" w GLSL?'
a = [
    "Pozwalają na przekazywanie danych między modułem wierzchołków a modułem fragmentów.",
    "Przechowują stałe wartości używane w shaderach.",
    "Służą do definiowania stałych dla całego programu.",
    "Umożliwiają manipulację oświetleniem w trakcie renderowania.",
]
questions.append({"question": q, "answers": a})

# Jakie jest główne zastosowanie zmiennych typu "uniform" w GLSL?
#
# A) Służą do przekazywania danych niezmieniających się przez cały cykl renderowania.
# B) Pozwalają na manipulację zmiennymi w trakcie renderowania.
# C) Przechowują dane oświetlenia dla obiektów w scenie.
# D) Służą do definiowania atrybutów wierzchołków.

q = 'Jakie jest główne zastosowanie zmiennych typu "uniform" w GLSL?'
a = [
    "Służą do przekazywania danych niezmieniających się przez cały cykl renderowania.",
    "Pozwalają na manipulację zmiennymi w trakcie renderowania.",
    "Przechowują dane oświetlenia dla obiektów w scenie.",
    "Służą do definiowania atrybutów wierzchołków.",
]
questions.append({"question": q, "answers": a})

# Czym są Normalized Device Coordinates (NDC) w OpenGL?
#
# A) Są to znormalizowane współrzędne obiektów 3D w przestrzeni sceny.
# B) Są to współrzędne obiektów po transformacji projekcyjnej, skalowane do zakresu [-1, 1].
# C) Są to współrzędne tekstur używane w procesie renderowania w OpenGL.
# D) Są to współrzędne pikseli na ekranie monitora.

q = "Czym są Normalized Device Coordinates (NDC) w OpenGL?"
a = [
    "Są to znormalizowane współrzędne obiektów 3D w przestrzeni sceny.",
    "Są to współrzędne obiektów po transformacji projekcyjnej, skalowane do zakresu [-1, 1].",
    "Są to współrzędne tekstur używane w procesie renderowania w OpenGL.",
    "Są to współrzędne pikseli na ekranie monitora.",
]
questions.append({"question": q, "answers": a})

# Jakie jest znaczenie Normalized Device Coordinates (NDC) w OpenGL?
#
# A) NDC są używane do mapowania obiektów 3D na przestrzeń ekranu w procesie renderowania.
# B) NDC są używane do określania kolizji między obiektami w scenie 3D.
# C) NDC są wykorzystywane do generowania losowych liczb w procesie programowania grafiki komputerowej.
# D) NDC nie mają specjalnego znaczenia w OpenGL.

q = "Jakie jest znaczenie Normalized Device Coordinates (NDC) w OpenGL?"
a = [
    "NDC są używane do mapowania obiektów 3D na przestrzeń ekranu w procesie renderowania.",
    "NDC są używane do określania kolizji między obiektami w scenie 3D.",
    "NDC są wykorzystywane do generowania losowych liczb w procesie programowania grafiki komputerowej.",
    "NDC nie mają specjalnego znaczenia w OpenGL.",
]
questions.append({"question": q, "answers": a})

# Jaki jest zakres wartości w Normalized Device Coordinates (NDC) w OpenGL?
#
# A) Zakres wartości w NDC wynosi [-1, 1], gdzie -1 oznacza dolną granicę, a 1 - górną granicę.
# B) Zakres wartości w NDC wynosi [0, 1], gdzie 0 oznacza dolną granicę, a 1 - górną granicę.
# C) Zakres wartości w NDC zależy od rozdzielczości ekranu, na którym odbywa się renderowanie.
# D) Zakres wartości w NDC jest dynamicznie dostosowywany w zależności od rozmiarów obiektów w scenie.

q = "Jaki jest zakres wartości w Normalized Device Coordinates (NDC) w OpenGL?"
a = [
    "Zakres wartości w NDC wynosi [-1, 1], gdzie -1 oznacza dolną granicę, a 1 - górną granicę.",
    "Zakres wartości w NDC wynosi [0, 1], gdzie 0 oznacza dolną granicę, a 1 - górną granicę.",
    "Zakres wartości w NDC zależy od rozdzielczości ekranu, na którym odbywa się renderowanie.",
    "Zakres wartości w NDC jest dynamicznie dostosowywany w zależności od rozmiarów obiektów w scenie.",
]
questions.append({"question": q, "answers": a})

# Czym jest triangulacja w grafice komputerowej?
#
# A) Jest to proces podziału kompleksu lub poligonu na trójkąty.
# B) Triangulacja odnosi się do techniki generowania tekstur na obiektach 3D.
# C) Triangulacja to proces generowania krawędzi i wierzchołków w grafach komputerowych.
# D) Triangulacja jest stosowana tylko w renderowaniu obiektów o określonym kształcie, takich jak kule lub sześciany.

q = "Czym jest triangulacja w grafice komputerowej?"
a = [
    "Jest to proces podziału kompleksu lub poligonu na trójkąty.",
    "Triangulacja odnosi się do techniki generowania tekstur na obiektach 3D.",
    "Triangulacja to proces generowania krawędzi i wierzchołków w grafach komputerowych.",
    "Triangulacja jest stosowana tylko w renderowaniu obiektów o określonym kształcie, takich jak kule lub sześciany.",
]
questions.append({"question": q, "answers": a})

# Jakie są główne zastosowania triangulacji w grafice komputerowej?
#
# A) Triangulacja jest powszechnie używana do renderowania obiektów 3D, ponieważ trójkąty są prostymi elementami geometrycznymi.
# B) Triangulacja jest stosowana wyłącznie w procesie tworzenia animacji.
# C) Triangulacja jest techniką używaną do tworzenia efektów specjalnych, takich jak rozbłyski świetlne.
# D) Triangulacja jest przydatna tylko w celu wykonywania operacji matematycznych na grafach komputerowych.

q = "Jakie są główne zastosowania triangulacji w grafice komputerowej?"
a = [
    "Triangulacja jest powszechnie używana do renderowania obiektów 3D, ponieważ trójkąty są prostymi elementami geometrycznymi.",
    "Triangulacja jest stosowana wyłącznie w procesie tworzenia animacji.",
    "Triangulacja jest techniką używaną do tworzenia efektów specjalnych, takich jak rozbłyski świetlne.",
    "Triangulacja jest przydatna tylko w celu wykonywania operacji matematycznych na grafach komputerowych.",
]
questions.append({"question": q, "answers": a})

# Czym jest interpolacja barycentryczna w grafice komputerowej?
#
# A) Jest to technika interpolacji wartości na podstawie ich wag wewnątrz trójkąta.
# B) Interpolacja barycentryczna to proces konwersji obiektów 2D na obiekty 3D w grafice komputerowej.
# C) Interpolacja barycentryczna to technika generowania tekstur na obiektach 3D.
# D) Interpolacja barycentryczna to technika oświetlenia obiektów w grafice komputerowej.

q = "Czym jest interpolacja barycentryczna w grafice komputerowej?"
a = [
    "Jest to technika interpolacji wartości na podstawie ich wag wewnątrz trójkąta.",
    "Interpolacja barycentryczna to proces konwersji obiektów 2D na obiekty 3D w grafice komputerowej.",
    "Interpolacja barycentryczna to technika generowania tekstur na obiektach 3D.",
    "Interpolacja barycentryczna to technika oświetlenia obiektów w grafice komputerowej.",
]
questions.append({"question": q, "answers": a})

# Jak działa interpolacja barycentryczna w grafice komputerowej?
#
# A) Interpolacja barycentryczna oblicza wartość piksela na podstawie wagi poszczególnych wierzchołków trójkąta.
# B) Interpolacja barycentryczna odnosi się tylko do interpolacji kolorów na teksturach.
# C) Interpolacja barycentryczna wykorzystuje tylko dwa wierzchołki trójkąta do obliczania wartości piksela.
# D) Interpolacja barycentryczna jest stosowana wyłącznie do interpolacji normalnych na obiektach 3D.

q = "Jak działa interpolacja barycentryczna w grafice komputerowej?"
a = [
    "Interpolacja barycentryczna oblicza wartość piksela na podstawie wagi poszczególnych wierzchołków trójkąta.",
    "Interpolacja barycentryczna odnosi się tylko do interpolacji kolorów na teksturach.",
    "Interpolacja barycentryczna wykorzystuje tylko dwa wierzchołki trójkąta do obliczania wartości piksela.",
    "Interpolacja barycentryczna jest stosowana wyłącznie do interpolacji normalnych na obiektach 3D.",
]
questions.append({"question": q, "answers": a})

# Czym są współrzędne homogeniczne w grafice komputerowej?
#
# A) Są to rozszerzone współrzędne, które zawierają dodatkowy składnik, nazywany składnikiem homogeniczności.
# B) Współrzędne homogeniczne to alternatywny system współrzędnych używany w grafice komputerowej do reprezentacji transformacji geometrycznych.
# C) Są to współrzędne używane tylko w 3D, które reprezentują głębokość obiektów w scenie.
# D) Współrzędne homogeniczne to system współrzędnych, który jest stosowany tylko w przypadku obiektów płaskich, takich jak tekstury.

q = "Czym są współrzędne homogeniczne w grafice komputerowej?"
a = [
    "Są to rozszerzone współrzędne, które zawierają dodatkowy składnik, nazywany składnikiem homogeniczności.",
    "Współrzędne homogeniczne to alternatywny system współrzędnych używany w grafice komputerowej do reprezentacji transformacji geometrycznych.",
    "Są to współrzędne używane tylko w 3D, które reprezentują głębokość obiektów w scenie.",
    "Współrzędne homogeniczne to system współrzędnych, który jest stosowany tylko w przypadku obiektów płaskich, takich jak tekstury.",
]
questions.append({"question": q, "answers": a})

# Jakie są główne zalety stosowania współrzędnych homogenicznych w grafice komputerowej?
#
# A) Współrzędne homogeniczne ułatwiają wykonywanie operacji transformacji, takich jak skalowanie, przesunięcie i obrót.
# B) Stosowanie współrzędnych homogenicznych eliminuje potrzebę przeliczania współrzędnych między różnymi układami odniesienia.
# C) Współrzędne homogeniczne pozwalają na łatwiejsze generowanie tekstur i efektów specjalnych.
# D) Stosowanie współrzędnych homogenicznych gwarantuje większą dokładność w wyliczaniu oświetlenia obiektów 3D.

q = "Jakie są główne zalety stosowania współrzędnych homogenicznych w grafice komputerowej?"
a = [
    "Współrzędne homogeniczne ułatwiają wykonywanie operacji transformacji, takich jak skalowanie, przesunięcie i obrót.",
    "Stosowanie współrzędnych homogenicznych eliminuje potrzebę przeliczania współrzędnych między różnymi układami odniesienia.",
    "Współrzędne homogeniczne pozwalają na łatwiejsze generowanie tekstur i efektów specjalnych.",
    "Stosowanie współrzędnych homogenicznych gwarantuje większą dokładność w wyliczaniu oświetlenia obiektów 3D.",
]
questions.append({"question": q, "answers": a})

# Jakie są główne zastosowania macierzy transformacji w grafice komputerowej?
#
# A) Macierze transformacji są używane do wykonywania przekształceń geometrycznych, takich jak przesunięcie, skalowanie i obrót obiektów.
# B) Macierze transformacji służą wyłącznie do generowania animacji w grafice komputerowej.
# C) Macierze transformacji są stosowane tylko w przypadku obiektów 2D, nie mają zastosowania w grafice 3D.
# D) Macierze transformacji są używane do tworzenia tekstur i efektów specjalnych na obiektach wizualizacji.

q = "Jakie są główne zastosowania macierzy transformacji w grafice komputerowej?"
a = [
    "Macierze transformacji są używane do wykonywania przekształceń geometrycznych, takich jak przesunięcie, skalowanie i obrót obiektów.",
    "Macierze transformacji służą wyłącznie do generowania animacji w grafice komputerowej.",
    "Macierze transformacji są stosowane tylko w przypadku obiektów 2D, nie mają zastosowania w grafice 3D.",
    "Macierze transformacji są używane do tworzenia tekstur i efektów specjalnych na obiektach wizualizacji.",
]
questions.append({"question": q, "answers": a})

# Jak działają macierze transformacji w grafice komputerowej?
#
# A) Macierze transformacji pozwalają na przekształcenie współrzędnych obiektów z jednego układu odniesienia do drugiego poprzez mnożenie punktów przez odpowiednią macierz.
# B) Macierze transformacji służą tylko do skalowania obiektów wzdłuż osi x, y i z.
# C) Macierze transformacji są stosowane wyłącznie do manipulacji oświetleniem obiektów w scenie.
# D) Macierze transformacji są używane tylko do generowania tekstur na obiektach 3D.

q = "Jak działają macierze transformacji w grafice komputerowej?"
a = [
    "Macierze transformacji pozwalają na przekształcenie współrzędnych obiektów z jednego układu odniesienia do drugiego poprzez mnożenie punktów przez odpowiednią macierz.",
    "Macierze transformacji służą tylko do skalowania obiektów wzdłuż osi x, y i z.",
    "Macierze transformacji są stosowane wyłącznie do manipulacji oświetleniem obiektów w scenie.",
    "Macierze transformacji są używane tylko do generowania tekstur na obiektach 3D.",
]
questions.append({"question": q, "answers": a})

# Jak działa macierz translacji w grafice komputerowej?
#
# A) Macierz translacji jest macierzą transformacji, która przesuwa obiekt wzdłuż osi x, y i z o określone wartości.
# B) Macierz translacji służy wyłącznie do skalowania obiektów wzdłuż osi x, y i z.
# C) Macierz translacji jest stosowana tylko w przypadku obiektów 2D, nie ma zastosowania w grafice 3D.
# D) Macierz translacji jest używana do generowania tekstur na obiektach wizualizacji.

q = "Jak działa macierz translacji w grafice komputerowej?"
a = [
    "Macierz translacji jest macierzą transformacji, która przesuwa obiekt wzdłuż osi x, y i z o określone wartości.",
    "Macierz translacji służy wyłącznie do skalowania obiektów wzdłuż osi x, y i z.",
    "Macierz translacji jest stosowana tylko w przypadku obiektów 2D, nie ma zastosowania w grafice 3D.",
    "Macierz translacji jest używana do generowania tekstur na obiektach wizualizacji.",
]
questions.append({"question": q, "answers": a})

# Jak działa macierz skalowania w grafice komputerowej?
#
# A) Macierz skalowania jest macierzą transformacji, która zmienia rozmiar obiektu wzdłuż osi x, y i z poprzez mnożenie jego współrzędnych przez określone wartości.
# B) Macierz skalowania służy do obracania obiektów wokół osi x, y i z.
# C) Macierz skalowania jest stosowana wyłącznie w przypadku obiektów 2D, nie ma zastosowania w grafice 3D.
# D) Macierz skalowania jest używana do generowania tekstur na obiektach wizualizacji.

q = "Jak działa macierz skalowania w grafice komputerowej?"
a = [
    "Macierz skalowania jest macierzą transformacji, która zmienia rozmiar obiektu wzdłuż osi x, y i z poprzez mnożenie jego współrzędnych przez określone wartości.",
    "Macierz skalowania służy do obracania obiektów wokół osi x, y i z.",
    "Macierz skalowania jest stosowana wyłącznie w przypadku obiektów 2D, nie ma zastosowania w grafice 3D.",
    "Macierz skalowania jest używana do generowania tekstur na obiektach wizualizacji.",
]
questions.append({"question": q, "answers": a})

# Jak działa macierz rotacji w grafice komputerowej?
#
# A) Macierz rotacji jest macierzą transformacji, która obraca obiekt wokół określonej osi (x, y, lub z) o określony kąt.
# B) Macierz rotacji służy do przesuwania obiektów wzdłuż osi x, y i z.
# C) Macierz rotacji jest stosowana wyłącznie w przypadku obiektów 2D, nie ma zastosowania w grafice 3D.
# D) Macierz rotacji jest używana do generowania tekstur na obiektach wizualizacji.

q = "Jak działa macierz rotacji w grafice komputerowej?"
a = [
    "Macierz rotacji jest macierzą transformacji, która obraca obiekt wokół określonej osi (x, y, lub z) o określony kąt.",
    "Macierz rotacji służy do przesuwania obiektów wzdłuż osi x, y i z.",
    "Macierz rotacji jest stosowana wyłącznie w przypadku obiektów 2D, nie ma zastosowania w grafice 3D.",
    "Macierz rotacji jest używana do generowania tekstur na obiektach wizualizacji.",
]
questions.append({"question": q, "answers": a})

# Jak działa macierz projekcji w grafice komputerowej?
#
# A) Macierz projekcji jest macierzą transformacji, która przekształca obiekty z przestrzeni trójwymiarowej do przestrzeni projekcyjnej.
# B) Macierz projekcji służy tylko do przesuwania obiektów wzdłuż osi x, y i z.
# C) Macierz projekcji jest stosowana tylko w przypadku obiektów 2D, nie ma zastosowania w grafice 3D.
# D) Macierz projekcji jest używana do generowania tekstur na obiektach wizualizacji.

q = "Jak działa macierz projekcji w grafice komputerowej?"
a = [
    "Macierz projekcji jest macierzą transformacji, która przekształca obiekty z przestrzeni trójwymiarowej do przestrzeni projekcyjnej.",
    "Macierz projekcji służy tylko do przesuwania obiektów wzdłuż osi x, y i z.",
    "Macierz projekcji jest stosowana tylko w przypadku obiektów 2D, nie ma zastosowania w grafice 3D.",
    "Macierz projekcji jest używana do generowania tekstur na obiektach wizualizacji.",
]
questions.append({"question": q, "answers": a})

# Jak działa projekcja ortograficzna w grafice komputerowej?
#
# A) Projekcja ortograficzna jest techniką rzutowania obiektów na płaską powierzchnię z zachowaniem proporcji i równoległych linii.
# B) Projekcja ortograficzna służy tylko do przesuwania obiektów wzdłuż osi x, y i z.
# C) Projekcja ortograficzna jest stosowana tylko w przypadku obiektów 2D, nie ma zastosowania w grafice 3D.
# D) Projekcja ortograficzna jest używana do generowania tekstur na obiektach wizualizacji.

q = "Jak działa projekcja ortograficzna w grafice komputerowej?"
a = [
    "Projekcja ortograficzna jest techniką rzutowania obiektów na płaską powierzchnię z zachowaniem proporcji i równoległych linii.",
    "Projekcja ortograficzna służy tylko do przesuwania obiektów wzdłuż osi x, y i z.",
    "Projekcja ortograficzna jest stosowana tylko w przypadku obiektów 2D, nie ma zastosowania w grafice 3D.",
    "Projekcja ortograficzna jest używana do generowania tekstur na obiektach wizualizacji.",
]
questions.append({"question": q, "answers": a})

# Jak działa projekcja perspektywiczna w grafice komputerowej?
#
# A) Projekcja perspektywiczna jest techniką rzutowania obiektów na płaszczyznę z uwzględnieniem perspektywy i odległości.
# B) Projekcja perspektywiczna służy tylko do przesuwania obiektów wzdłuż osi x, y i z.
# C) Projekcja perspektywiczna jest stosowana tylko w przypadku obiektów 2D, nie ma zastosowania w grafice 3D.
# D) Projekcja perspektywiczna jest używana do generowania tekstur na obiektach wizualizacji.

q = "Jak działa projekcja perspektywiczna w grafice komputerowej?"
a = [
    "Projekcja perspektywiczna jest techniką rzutowania obiektów na płaszczyznę z uwzględnieniem perspektywy i odległości.",
    "Projekcja perspektywiczna służy tylko do przesuwania obiektów wzdłuż osi x, y i z.",
    "Projekcja perspektywiczna jest stosowana tylko w przypadku obiektów 2D, nie ma zastosowania w grafice 3D.",
    "Projekcja perspektywiczna jest używana do generowania tekstur na obiektach wizualizacji.",
]
questions.append({"question": q, "answers": a})

# Jakie są główne różnice między projekcją ortograficzną i perspektywiczną w grafice komputerowej?
#
# A) Projekcja ortograficzna jest techniką rzutowania obiektów na płaską powierzchnię, zachowując proporcje i równoległe linie, podczas gdy projekcja perspektywiczna uwzględnia perspektywę i odległość, co prowadzi do efektu oddalenia i zmniejszania obiektów wraz z ich oddalaniem się od kamery.
# B) Projekcja ortograficzna jest stosowana tylko do obiektów 2D, podczas gdy projekcja perspektywiczna ma zastosowanie w grafice 3D.
# C) Projekcja ortograficzna jest używana tylko w przypadku tekstur, podczas gdy projekcja perspektywiczna jest stosowana do generowania oświetlenia obiektów.
# D) Nie ma żadnych istotnych różnic między projekcją ortograficzną a perspektywiczną w grafice komputerowej.

q = "Jakie są główne różnice między projekcją ortograficzną i perspektywiczną w grafice komputerowej?"
a = [
    "Projekcja ortograficzna jest techniką rzutowania obiektów na płaską powierzchnię, zachowując proporcje i równoległe linie, podczas gdy projekcja perspektywiczna uwzględnia perspektywę i odległość, co prowadzi do efektu oddalenia i zmniejszania obiektów wraz z ich oddalaniem się od kamery.",
    "Projekcja ortograficzna jest stosowana tylko do obiektów 2D, podczas gdy projekcja perspektywiczna ma zastosowanie w grafice 3D.",
    "Projekcja ortograficzna jest używana tylko w przypadku tekstur, podczas gdy projekcja perspektywiczna jest stosowana do generowania oświetlenia obiektów.",
    "Nie ma żadnych istotnych różnic między projekcją ortograficzną a perspektywiczną w grafice komputerowej.",
]
questions.append({"question": q, "answers": a})

# Czym jest macierz widoku (view matrix) w grafice komputerowej?
#
# A) Macierz widoku jest macierzą transformacji, która reprezentuje położenie i orientację kamery w przestrzeni sceny.
# B) Macierz widoku służy tylko do przesuwania obiektów wzdłuż osi x, y i z.
# C) Macierz widoku jest stosowana tylko w przypadku obiektów 2D, nie ma zastosowania w grafice 3D.
# D) Macierz widoku jest używana do generowania tekstur na obiektach wizualizacji.

q = "Czym jest macierz widoku (view matrix) w grafice komputerowej?"
a = [
    "Macierz widoku jest macierzą transformacji, która reprezentuje położenie i orientację kamery w przestrzeni sceny.",
    "Macierz widoku służy tylko do przesuwania obiektów wzdłuż osi x, y i z.",
    "Macierz widoku jest stosowana tylko w przypadku obiektów 2D, nie ma zastosowania w grafice 3D.",
    "Macierz widoku jest używana do generowania tekstur na obiektach wizualizacji.",
]
questions.append({"question": q, "answers": a})

# Czym jest macierz modelu (model matrix) w grafice komputerowej?
#
# A) Macierz modelu jest macierzą transformacji, która reprezentuje położenie, skalę i obrót obiektu w przestrzeni sceny.
# B) Macierz modelu służy tylko do przesuwania obiektów wzdłuż osi x, y i z.
# C) Macierz modelu jest stosowana tylko w przypadku obiektów 2D, nie ma zastosowania w grafice 3D.
# D) Macierz modelu jest używana do generowania tekstur na obiektach wizualizacji.

q = "Czym jest macierz modelu (model matrix) w grafice komputerowej?"
a = [
    "Macierz modelu jest macierzą transformacji, która reprezentuje położenie, skalę i obrót obiektu w przestrzeni sceny.",
    "Macierz modelu służy tylko do przesuwania obiektów wzdłuż osi x, y i z.",
    "Macierz modelu jest stosowana tylko w przypadku obiektów 2D, nie ma zastosowania w grafice 3D.",
    "Macierz modelu jest używana do generowania tekstur na obiektach wizualizacji.",
]
questions.append({"question": q, "answers": a})

# Co to jest tekstura w grafice komputerowej?
#
# A) Tekstura to obraz lub wzór, który jest nakładany na powierzchnię obiektu wizualizacji.
# B) Tekstura to efekt wizualny stosowany tylko w animacjach.
# C) Tekstura to metoda kompresji danych graficznych w celu oszczędności pamięci.
# D) Tekstura to specjalny rodzaj obiektu, który emituje światło w trakcie renderowania sceny.

q = "Co to jest tekstura w grafice komputerowej?"
a = [
    "Tekstura to obraz lub wzór, który jest nakładany na powierzchnię obiektu wizualizacji.",
    "Tekstura to efekt wizualny stosowany tylko w animacjach.",
    "Tekstura to metoda kompresji danych graficznych w celu oszczędności pamięci.",
    "Tekstura to specjalny rodzaj obiektu, który emituje światło w trakcie renderowania sceny.",
]
questions.append({"question": q, "answers": a})

# Co to jest aliasing w kontekście grafiki komputerowej?
#
# A) Aliasing to efekt, w którym występujące krawędzie lub linie obiektów są wyświetlane jako pikselowane lub zniekształcone.
# B) Aliasing to technika stosowana tylko w generowaniu animacji.
# C) Aliasing to proces redukcji rozmiaru obrazu w grafice komputerowej.
# D) Aliasing to tylko błąd programistyczny, nie ma wpływu na wygląd renderowanych obiektów.

q = "Co to jest aliasing w kontekście grafiki komputerowej?"
a = [
    "Aliasing to efekt, w którym występujące krawędzie lub linie obiektów są wyświetlane jako pikselowane lub zniekształcone.",
    "Aliasing to technika stosowana tylko w generowaniu animacji.",
    "Aliasing to proces redukcji rozmiaru obrazu w grafice komputerowej.",
    "Aliasing to tylko błąd programistyczny, nie ma wpływu na wygląd renderowanych obiektów.",
]
questions.append({"question": q, "answers": a})

# Co to jest antyaliasing w kontekście grafiki komputerowej?
#
# A) Antyaliasing to technika, która redukuje efekt aliasingu poprzez wygładzanie krawędzi i linii obiektów.
# B) Antyaliasing to metoda kompresji grafiki używana do oszczędzania pamięci.
# C) Antyaliasing to tylko dodatkowy efekt wizualny stosowany w animacjach.
# D) Antyaliasing nie ma żadnego zastosowania w grafice komputerowej.

q = "Co to jest antyaliasing w kontekście grafiki komputerowej?"
a = [
    "Antyaliasing to technika, która redukuje efekt aliasingu poprzez wygładzanie krawędzi i linii obiektów.",
    "Antyaliasing to metoda kompresji grafiki używana do oszczędzania pamięci.",
    "Antyaliasing to tylko dodatkowy efekt wizualny stosowany w animacjach.",
    "Antyaliasing nie ma żadnego zastosowania w grafice komputerowej.",
]
questions.append({"question": q, "answers": a})

json.dump(questions, open("questions.json", "w"))
