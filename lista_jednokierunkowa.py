from element_plik import Element


class ListaJednokierunkowa:

    def __init__(self):
        self.pierwszy_element = None

    def _is_empty(self) -> bool:  # 2 kroki
        if self.pierwszy_element is None:
            return True
        else:
            return False

    def _dodaj_element_na_poczatek(self, dane) -> None:  # O(1)
        nowy_element = Element(dane)  # 1
        nowy_element.nastepny = self.pierwszy_element  # 1
        self.pierwszy_element = nowy_element  # 1

    def _dodaj_element_na_koniec(self, dane) -> None:  # O(n)
        if self._is_empty():
            self.pierwszy_element = Element(dane)
            print(f"Dodany element został na koniec {self.pierwszy_element.dane}")
        else:

            ostatni_element = self.pierwszy_element
            while ostatni_element.nastepny:
                ostatni_element = ostatni_element.nastepny
            ostatni_element.nastepny = Element(dane)
            print(f"Dodano element {ostatni_element.nastepny.dane} na koniec\n")

    def _dodaj_element_po_wartosci(self, dane, wartosc) -> None:
        aktualny_element = self.pierwszy_element
        while aktualny_element.nastepny:
            if aktualny_element.dane == wartosc:
                nowy_element = Element(dane)
                nowy_element.nastepny = aktualny_element.nastepny
                aktualny_element.nastepny = nowy_element
                print(f"Dodano nowy element {nowy_element.dane} po {aktualny_element.dane}")
                # Mógłbym wypisać, który jest z kolei
            else:
                aktualny_element = aktualny_element.nastepny

    def _usun_pierwszy_element(self):  # O(1)
        if self._is_empty():
            raise Exception('Nie można zwrócić elementu, ponieważ nie istnieje\n')
        else:
            temp = self.pierwszy_element
            self.pierwszy_element = self.pierwszy_element.nastepny
            temp.next = None
            return temp.dane

    # Przechować ostatnią wartość i dodawać po niej, do stworzenia kolejki, lub lista dwukierunkowa
    def _usun_ostatni_element(self):  # O(n)
        if self._is_empty():
            return None

        if self.pierwszy_element.nastepny is None:
            temp = self.pierwszy_element.dane
            self.pierwszy_element = None
            return temp

        przedostatni_element = self.pierwszy_element

        while przedostatni_element.nastepny.nastepny:
            przedostatni_element = przedostatni_element.nastepny
        temp = przedostatni_element.nastepny
        przedostatni_element.nastepny = None
        return temp.dane

    def _wypisz_liste(self):  # O(n)
        if self._is_empty():  # 1
            return None
        i: int = 1  # 1
        aktualny_element = self.pierwszy_element  # 1 (3)
        while aktualny_element is not None:  # N + 1
            print(f"Element nr. {i}. Dane: {aktualny_element.dane}")  # 1
            aktualny_element = aktualny_element.nastepny  # 1
            i += 1  # 1
        print("-" * 100)

    def _wyszukaj_element_po_wartosci(self, wartosc):
        aktualny_element = self.pierwszy_element
        while aktualny_element.nastepny:
            if aktualny_element.dane == wartosc:
                print(f"Wartość {aktualny_element.dane} znaleziona w liście/stosie/ osobne printy")
                return aktualny_element
                # Mógłbym wypisać, który jest z kolei
            else:
                aktualny_element = aktualny_element.nastepny
        print(f"Wartości {aktualny_element} nie ma w liście - osobne printy")
        return None

    def size(self):
        size: int = 0
        if self._is_empty():
            return 0
        aktualny_element = self.pierwszy_element
        while aktualny_element is not None:
            size += 1
            aktualny_element = aktualny_element.nastepny
        return size
