from os.path import split, splitext


def pegar_nome_arquivo(path: str, flag:str="_sem_fundo") -> str:
    r, file = split(path)
    n, e = splitext(file)
    return f"{n}{flag}{e}"



if __name__ == "__main__":
    # Testando esse modulo
    print(pegar_nome_arquivo("README.md"))