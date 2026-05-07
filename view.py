class CinemaView:
    def mostrar_menu(self):
        print("\n--- MENU CINEMA ---")
        print("1. Cadastrar Filme")
        print("2. Listar Filmes")
        print("0. Sair")
        return input("Escolha: ")

    def ler_dados_filme(self):
        titulo = input("Título: ")
        duracao = int(input("Duração (min): "))
        return titulo, duracao

    def listar_filmes(self, filmes):
        print("\n--- LISTA DE FILMES ---")
        for f in filmes:
            print(f"ID: {f[0]} | Título: {f[1]} | Duração: {f[2]}min")

    def mostrar_mensagem(self, msg):
        print(f"-> {msg}")