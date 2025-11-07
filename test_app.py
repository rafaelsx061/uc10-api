def sum_numbers(a, b):
    return a + b

def get_text():
    return "UC10 - Teste Automatizado"

def test_soma_simples():
    assert sum_numbers(2, 3) == 5

def test_verifica_texto():
    assert "UC10" in get_text()
