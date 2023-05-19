from lista_jednokierunkowa import ListaJednokierunkowa


class Stos(ListaJednokierunkowa):
    def __init__(self):
        super().__init__()

    def stos_jest_pusty(self) -> bool:
        return self._is_empty()

    def push(self, dane) -> None:
        self._dodaj_element_na_poczatek(dane)
        # print(f"Dodano element {dane} na stos")

    def pop(self):
        usuniety_element = self._usun_pierwszy_element()
        return usuniety_element

    def wypisz_stos(self) -> None:
        self._wypisz_liste()
        return None

    def top(self):
        if self._is_empty():
            print("Stos jest pusty")
        else:
            print(f"Element na górze stosu: {self.pierwszy_element.dane}")
            return self.pierwszy_element.dane
