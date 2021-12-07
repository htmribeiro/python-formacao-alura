class Funcionario:
    def __init__(self, nome):
        self.nome = nome
    
    def registra_horas(self, horas):
        print('Horas registradas...')
        
    def mostrar_tarefas(self):
        print('Fez muita coisa...')
        
class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')
        
    def buscar_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos- {mes}' if mes else 'Mostrar cursos desse mês')

class Alura(Funcionario):
    # def mostrar_tarefas(self):
    #     print('Fez muita coisa, Alurete!')
        
    def buscar_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

class Hipster:
  def __str__(self):
      return f'Hipster, {self.nome}'

class Junior(Alura):
    pass

class Pleno(Alura, Caelum, Hipster):
    pass

class Senior(Alura, Caelum, Hipster):
  pass

jose = Junior('José')
jose.buscar_perguntas_sem_resposta()
jose.mostrar_tarefas()

luana = Pleno('Luana')
luana.buscar_perguntas_sem_resposta()
luana.buscar_cursos_do_mes()
luana.mostrar_tarefas()

luan = Senior('Luan')
print(luan)