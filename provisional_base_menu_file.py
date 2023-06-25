import tkinter as tk
from tkinter import ttk
import list_logic as ll
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

LARGEFONT = ("Verdana", 35)

this_array = []
weight, height, tree, edges, leaf_nodos, inorder_array, postorder_array, preorder_array, int_array = (None, None, None, None, None, None, None, None, None)
def convert_to_int(entry_object, window):
    get_information = entry_object.get()
    this_list = get_information.split(',')
    prov_list = []

    try:
        for i in this_list:
            prov_list.append(i)
        global int_array, edges, tree, weight, height, leaf_nodos, inorder_array, postorder_array, preorder_array
        this_array = prov_list
        int_array = [int(x) for x in this_array]
        tree = ll.create_tree(int_array)

        inorder_array = ll.get_inorder(tree)
        postorder_array = ll.get_postorder(tree)
        preorder_array = ll.get_preorder(tree)

        weight = ll.get_weight(int_array)
        height = ll.get_height(tree)
        leaf_nodos = ll.get_hojas(tree)

        edges = ll.create_tuple_list(tree)
    except ValueError:
        print('Error')


    window.destroy()


class IngresarValores:

    def __init__(self):
        self.root = tk.Tk()
        entry_ingress = tk.Entry(self.root)
        button_enviar = tk.Button(self.root, text="Enviar", command=lambda: convert_to_int(entry_ingress, self.root))
        entry_ingress.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        button_enviar.place(relx=0.5,rely=0.8,anchor=tk.CENTER)
        self.root.mainloop()

IngresarValores()

class Application(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)


        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}


        for F in (Menu, EstructuraArbol, IndicarPeso, MostrarOrden, IndicarAltura, IndicarHojas):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Menu)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



class Menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Menu", font=LARGEFONT)
        label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        button1 = ttk.Button(self, text="Estructura Arbol",
                             command=lambda: controller.show_frame(EstructuraArbol))

        button2 = ttk.Button(self, text="Indicar Peso",
                             command= lambda : controller.show_frame(IndicarPeso))

        button3 = ttk.Button(self, text="Mostrar Orden",
                             command= lambda : controller.show_frame(MostrarOrden))
        button4 = ttk.Button(self, text="Indicar Altura",
                             command=lambda: controller.show_frame(IndicarAltura))

        button5 = ttk.Button(self, text="Indicar Hojas",
                             command= lambda : controller.show_frame(IndicarHojas))

        button1.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        button2.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        button3.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        button4.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        button5.place(relx=0.5, rely=0.7, anchor=tk.CENTER)





class EstructuraArbol(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Estructura Arbol", font=LARGEFONT)

        self.draw_graph()
        label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)


        button1 = ttk.Button(self, text="Menu",
                             command=lambda: controller.show_frame(Menu))
        button1.place(rely=0.5, anchor=tk.W)

    def draw_graph(self):

        global int_array, edges, tree
        figure = plt.figure()
        graph = nx.DiGraph()
        graph.add_edges_from(edges)

        pos = ll.hierarchy_pos(graph, int_array[0])
        nx.draw(graph, pos=pos, with_labels=True)

        canvas = FigureCanvasTkAgg(figure=figure, master=self)
        canvas.draw()

        canvas.get_tk_widget().place(relx=0.5, rely=0.5, anchor=tk.CENTER)


class IndicarPeso(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global int_array, edges, tree, weight, height, leaf_nodos, inorder_array, postorder_array, preorder_array
        label = ttk.Label(self, text="PESO DEL ARBOL: ", font=LARGEFONT)
        label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        label_indicate = ttk.Label(self, text=f"{weight}", font=("sans-serif", 50))
        label_indicate.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        button1 = ttk.Button(self, text="Menu",
                             command=lambda: controller.show_frame(Menu))
        button1.place(rely=0.5, anchor=tk.W)

class IndicarAltura(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global int_array, edges, tree, weight, height, leaf_nodos, inorder_array, postorder_array, preorder_array
        label = ttk.Label(self, text="IndicarAltura", font=LARGEFONT)
        label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        label_indicate = ttk.Label(self, text=f"{height}", font=LARGEFONT)
        label_indicate.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        button1 = ttk.Button(self, text="Startpage",
                             command=lambda: controller.show_frame(Menu))
        button1.place(rely=0.5, anchor=tk.W)

class IndicarHojas(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global int_array, edges, tree, weight, height, leaf_nodos, inorder_array, postorder_array, preorder_array
        label = ttk.Label(self, text="Indicar Nodos Hojas", font=LARGEFONT)
        label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        label_indicate = ttk.Label(self, text=f"{leaf_nodos}", font=LARGEFONT)
        label_indicate.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        button1 = ttk.Button(self, text="Startpage",
                             command=lambda: controller.show_frame(Menu))
        button1.place(rely=0.5, anchor=tk.W)

class MostrarOrden(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global int_array, edges, tree, weight, height, leaf_nodos, inorder_array, postorder_array, preorder_array
        label = ttk.Label(self, text="Mostrar Ordenes", font=LARGEFONT)
        label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)


        label_inorder = ttk.Label(self, text=f"Inorden: {inorder_array}", font=LARGEFONT)
        label_postorder = ttk.Label(self, text=f"Postorden: {postorder_array}", font=LARGEFONT)
        label_preorder = ttk.Label(self, text=f"Preorden: {preorder_array}", font=LARGEFONT)

        label_inorder.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        label_postorder.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        label_preorder.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        button1 = ttk.Button(self, text="Startpage",
                             command=lambda: controller.show_frame(Menu))
        button1.place(rely=0.5, anchor=tk.W)



app = Application()
app.mainloop()
