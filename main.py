# =================================  TESTY  ===================================
# Testy do tego pliku zostały podzielone na dwie kategorie:
#
#  1. `..._invalid_input`:
#     - Sprawdzające poprawną obsługę nieprawidłowych danych wejściowych.
#
#  2. `..._correct_solution`:
#     - Weryfikujące poprawność wyników dla prawidłowych danych wejściowych.
# =============================================================================
import numpy as np
import numpy.polynomial.polynomial as nppoly


def roots_20(coef: np.ndarray) -> tuple[np.ndarray, np.ndarray] | None:
    """Funkcja wyznaczająca miejsca zerowe wielomianu funkcją
    `nppoly.polyroots()`, najpierw lekko zaburzając wejściowe współczynniki 
    wielomianu (N(0,1) * 1e-10).

    Args:
        coef (np.ndarray): Wektor współczynników wielomianu (n,).

    Returns:
        (tuple[np.ndarray, np. ndarray]):
            - Zaburzony wektor współczynników (n,),
            - Wektor miejsc zerowych (m,).
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    if not isinstance(coef, np.ndarray) or coef.ndim != 1:
        return None

    coef_zaburzony = coef + np.random.random_sample(coef.shape)*1e-10
    

    pierwiastki = nppoly.polyroots(coef_zaburzony)
  
    return coef_zaburzony, pierwiastki
    


def frob_a(coef: np.ndarray) -> np.ndarray | None:
    if not isinstance(coef, np.ndarray):
        return None
    
    if not coef.ndim == 1:
        return None
    
    if len(coef) < 2:
        return None
    
    A = np.eye(len(coef)-1, k=1)
    A[-1, :] = -coef[:-1] / coef[-1]
    return A

    pass

  


def is_nonsingular(A: np.ndarray) -> bool | None:
    """Funkcja sprawdzająca czy podana macierz NIE JEST singularna. Przy
    implementacji należy pamiętać o definicji zera maszynowego.

    Args:
        A (np.ndarray): Macierz (n,n) do przetestowania.

    Returns:
        (bool): `True`, jeżeli macierz A nie jest singularna, w przeciwnym 
            wypadku `False`.
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    import numpy as np
    # --- Walidacja wejścia ---
    if not isinstance(A, np.ndarray):
        return None
    if A.ndim != 2:
        return None
    if A.shape[0] != A.shape[1]:
        return None  # musi być kwadratowa

    # Używamy det(A), ale pamiętamy o zerze maszynowym
    detA = np.linalg.det(A)

    # epsilon maszynowy typu float
    eps = np.finfo(float).eps

    # Jeżeli wartość bezwzględna det(A) jest mniejsza niż eps → traktujemy jako zero
    if abs(detA) < eps:
        return False  # macierz osobliwa
    return True        # macierz nieosobliwa

    pass
