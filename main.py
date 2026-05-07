from controller import FilmeController
from view import CinemaView

def start():
    controller = FilmeController()
    view = CinemaView()

    while True:
        opcao = view.mostrar_menu()

        if opcao == "1":
            t, d = view.ler_dados_filme()
            sucesso, msg = controller.cadastrar(t, d)
            view.mostrar_mensagem(msg)
        
        elif opcao == "2":
            lista = controller.buscar_todos()
            view.listar_filmes(lista)
        
        elif opcao == "0":
            break
        else:
            view.mostrar_mensagem("Opção inválida.")

if __name__ == "__main__":
    start()