class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
    
    def __str__(self):
        # Representación en cadena del libro
        return f"Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}"