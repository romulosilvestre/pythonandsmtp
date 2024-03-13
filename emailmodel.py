class EmailModel:
    def __init__(self, destinatario, email, assunto, conteudo, anexo):
        self.destinatario = destinatario
        self.email = email
        self.assunto = assunto
        self.conteudo = conteudo
        self.anexo = anexo

    def __str__(self):
        return f"destinatario: {self.destinatario}\nemail:{self.email}\nassunto:{self.assunto}\nconteudo:{self.conteudo}\nanexo:{self.anexo}"


