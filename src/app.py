from tkinter import *
from tkinter import ttk
import services


def main():
    def on_enviar():
        nome = nomeEntry.get()
        email = emailEntry.get()
        senha = senhaEntry.get()
        services.enviar_dados(nome, email, senha)


        nomeEntry.delete(0, END)
        emailEntry.delete(0, END)
        senhaEntry.delete(0, END)

    def listar_usuarios():
        usuarios = services.listar_usuario()


        janela_listar = Toplevel(janela)
        janela_listar.title("Lista de Usuários")
        janela_listar.geometry("600x300")


        tree = ttk.Treeview(janela_listar, columns=( 'ID','Nome', 'Email'), show='headings')
        tree.heading('ID', text='ID')
        tree.heading('Nome', text='Nome')
        tree.heading('Email', text='Email')

        voltar = Button(janela_listar, text='voltar', width=10, command=janela_listar.destroy)
        voltar.pack(fill=BOTH, expand=True, side=BOTTOM)


        tree.pack(fill=BOTH, expand=True)

        for usuario in usuarios:
        
            tree.insert('', END, values=usuario)

    janela = Tk()
    janela.title("Formulario")
    janela.geometry("400x300")

    titulo = Label(janela, text='CRUD', font=('Arial', 20))
    titulo.pack(pady=30)

    nome = Label(janela, text="Nome:")
    nome.place(x=50, y=100)

    global nomeEntry
    nomeEntry = Entry(janela, width=30)
    nomeEntry.place(x=100, y=100)

    email = Label(janela, text="Email:")
    email.place(x=50, y=130)

    global emailEntry
    emailEntry = Entry(janela, width=30)
    emailEntry.place(x=100, y=130)

    senha = Label(janela, text="Senha:")
    senha.place(x=50, y=160)

    global senhaEntry
    senhaEntry = Entry(janela, width=30, show='*')
    senhaEntry.place(x=100, y=160)

    enviar = Button(janela, text="Cadastrar", width=10, command=on_enviar)
    enviar.place(x=100, y=200)

    listar = Button(janela, text='Listar Usuários', width=15, command=listar_usuarios )
    listar.place(x=200, y=200)

    janela.mainloop()

if __name__ == '__main__':
    main()