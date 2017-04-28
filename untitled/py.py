class Generador:
    def generaTituloParrafo(self, titulo, parrafo):
        titulo = "<h1>" + titulo + "</h1>"
        parrafo = "<p>" + parrafo + "</p>"
        return titulo + parrafo

    def generaLista(self, listaItems):
        codigo = ""
        for i in listaItems:
            codigo = codigo + "<li>" + i + "</li>"
        return "<ol>" + codigo + "</ol>"

    def generarTabla(self, itemTabla):
        codigo = ""

        c=""

        for i in itemTabla:
            x="<tr>"
            for j in i.split(","):
                c=c+"<td>"+j+"</td>"
            v="</tr>"
        codigo=codigo + x + c + v
        return "<table>" + codigo + "</table>"


miGenerador = Generador()

print(miGenerador.generaTituloParrafo("hola", "mundo"))
n = open("lista", "r")
print(miGenerador.generarTabla(n))
