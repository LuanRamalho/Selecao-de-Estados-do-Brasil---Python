import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import urllib.request
import io

# Dados das bandeiras
# Dicionário de estados com URLs das bandeiras
states = {
    "norte": [
        {"name": "Acre", "flag": "https://s1.static.brasilescola.uol.com.br/be/2021/05/bandeira-acre.jpg"},
        {"name": "Amapá", "flag": "https://static.mundoeducacao.uol.com.br/mundoeducacao/2021/02/bandeira-amapa.jpg"},
        {"name": "Amazonas", "flag": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Bandeira_do_Amazonas.svg/700px-Bandeira_do_Amazonas.svg.png"},
        {"name": "Pará", "flag": "https://s4.static.brasilescola.uol.com.br/be/2021/05/bandeira-para.jpg"},
        {"name": "Rondônia", "flag": "https://s1.static.brasilescola.uol.com.br/be/2021/02/bandeira-rondonia.jpg"},
        {"name": "Roraima", "flag": "https://s4.static.brasilescola.uol.com.br/be/2021/02/2-bandeira-roraima.jpg"},
        {"name": "Tocantins", "flag": "https://s2.static.brasilescola.uol.com.br/be/2021/04/bandeira-do-tocantins.jpg"}
    ],
    "nordeste": [
        {"name": "Alagoas", "flag": "https://s5.static.brasilescola.uol.com.br/be/2021/05/bandeira-de-alagoas.jpg"},
        {"name": "Bahia", "flag": "https://s2.static.brasilescola.uol.com.br/be/2021/05/bandeira-da-bahia.jpg"},
        {"name": "Ceará", "flag": "https://s3.static.brasilescola.uol.com.br/be/2021/02/bandeira-do-ceara.jpg"},
        {"name": "Maranhão", "flag": "https://s2.static.brasilescola.uol.com.br/be/2021/05/bandeira-maranhao.jpg"},
        {"name": "Paraíba", "flag": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Bandeira_da_Para%C3%ADba.svg/2000px-Bandeira_da_Para%C3%ADba.svg.png"},
        {"name": "Pernambuco", "flag": "https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/acoes-e-programas/cidadania-fiscal/naf/nucleos/arquivos-e-imagens/pernambuco.png/@@images/image.png"},
        {"name": "Piauí", "flag": "https://s1.static.brasilescola.uol.com.br/be/2021/04/bandeira-piaui.jpg"},
        {"name": "Rio Grande do Norte", "flag": "https://s5.static.brasilescola.uol.com.br/be/2021/05/bandeira-rn.jpg"},
        {"name": "Sergipe", "flag": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Bandeira_de_Sergipe.svg/1200px-Bandeira_de_Sergipe.svg.png"}
    ],
    "centro-oeste": [
        {"name": "Distrito Federal", "flag": "https://www.eccobandeiras.com.br/image/cache/catalog/antigas/Distrito_Federal-1111x740.jpg"},
        {"name": "Goiás", "flag": "https://s4.static.brasilescola.uol.com.br/be/2021/04/bandeira-de-goias.jpg"},
        {"name": "Mato Grosso", "flag": "https://s5.static.brasilescola.uol.com.br/be/2021/04/bandeira-mato-grosso.jpg"},
        {"name": "Mato Grosso do Sul", "flag": "https://s5.static.brasilescola.uol.com.br/be/2021/04/bandeira-mato-grosso-do-sul.jpg"}
    ],
    "sudeste": [
        {"name": "Espírito Santo", "flag": "https://img.freepik.com/fotos-premium/bandeira-do-estado-de-espirito-santo-no-brasil_2227-544.jpg"},
        {"name": "Minas Gerais", "flag": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Bandeira_de_Minas_Gerais.svg/2560px-Bandeira_de_Minas_Gerais.svg.png"},
        {"name": "Rio de Janeiro", "flag": "https://i.pinimg.com/736x/47/46/cd/4746cdea93327b831570933d31b59332.jpg"},
        {"name": "São Paulo", "flag": "https://s4.static.brasilescola.uol.com.br/be/2021/05/bandeira-sp.jpg"}
    ],
    "sul": [
        {"name": "Paraná", "flag": "https://s2.static.brasilescola.uol.com.br/be/2021/04/bandeira-parana.jpg"},
        {"name": "Rio Grande do Sul", "flag": "https://media.istockphoto.com/id/1436424171/pt/vetorial/flag-of-rio-grande-do-sul-state-freedom-equality-and-humanity-liberdade-igualdade-e.jpg?s=612x612&w=0&k=20&c=Rf-EGnBX_hJ837HRMkgNUKsvEHDGhhCKTrBFkvN0ntw="},
        {"name": "Santa Catarina", "flag": "https://s4.static.brasilescola.uol.com.br/be/2021/04/1-bandeira-de-santa-catarina.jpg"}
    ]
}


# Configuração da janela
root = tk.Tk()
root.title("Bandeiras dos Estados do Brasil")
root.geometry("600x500")
root.configure(bg='cyan')

# Título
title_label = tk.Label(root, text="Bandeiras dos Estados do Brasil", font=("Arial", 24, "bold"), bg="#007BFF", fg="white")
title_label.pack(pady=20)

# Função para atualizar os estados conforme a região selecionada
def update_states(event):
    region = region_var.get()
    state_var.set('')
    state_select['values'] = [state['name'] for state in states.get(region, [])]

# Função para exibir a bandeira do estado selecionado
def display_flag(event):
    region = region_var.get()
    state_name = state_var.get()
    flag_container.config(image='')  # Limpa a imagem anterior
    
    if region and state_name:
        flag_url = next(state['flag'] for state in states[region] if state['name'] == state_name)
        
        # Carrega a imagem da URL
        with urllib.request.urlopen(flag_url) as url:
            image_data = url.read()
            img = Image.open(io.BytesIO(image_data))
            img.thumbnail((400, 400))
            flag_image = ImageTk.PhotoImage(img)
            flag_container.config(image=flag_image)
            flag_container.image = flag_image

# Dropdown para seleção da região
region_var = tk.StringVar()
region_label = tk.Label(root, text="Selecione a Região:", font=("Arial", 14), bg="cyan")
region_label.pack(pady=10)
region_select = ttk.Combobox(root, textvariable=region_var, state="readonly", font=("Arial", 12))
region_select['values'] = list(states.keys())
region_select.pack()
region_select.bind("<<ComboboxSelected>>", update_states)

# Dropdown para seleção do estado
state_var = tk.StringVar()
state_label = tk.Label(root, text="Selecione o Estado:", font=("Arial", 14), bg="cyan")
state_label.pack(pady=10)
state_select = ttk.Combobox(root, textvariable=state_var, state="readonly", font=("Arial", 12))
state_select.pack()
state_select.bind("<<ComboboxSelected>>", display_flag)

# Container para a bandeira
flag_container = tk.Label(root, bg="cyan")
flag_container.pack(pady=20)

root.mainloop()
