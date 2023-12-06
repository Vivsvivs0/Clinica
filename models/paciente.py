import json

class Paciente:
  def __init__(self, id, nome, fone, email, senha):
    self.__id = id
    self.__nome = nome
    self.__fone = fone
    self.__email = email
    self.__senha = senha

  def get_id(self): return self.__id
  def get_nome(self): return self.__nome
  def get_fone(self): return self.__fone
  def get_email(self): return self.__email
  def get_senha(self): return self.__senha

  def set_id(self, id): self.__id = id
  def set_nome(self, nome): self.__nome = nome
  def set_fone(self, fone): self.__fone = fone
  def set_email(self, email): self.__email = email
  def set_senha(self, senha): self.__senha = senha

  def __eq__(self, x):
    if self.__id == x.__id and self.__nome == x.__nome and self.__fone == x.__fone and self.__email == x.__email and self.__senha == x.__senha:
      return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__nome} - {self.__fone} - {self.__email}"


class NPaciente:
  __pacientes = []

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    id = 0
    for aux in cls.__pacientes:
      if aux.get_id() - id == 1:
        id = aux.get_id()
      else:
        break
    obj.set_id(id + 1)
    cls.__pacientes.append(obj)
    cls.salvar()

  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.__pacientes

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for obj in cls.__pacientes:
      if obj.get_id() == id: return obj
    return None

  @classmethod
  def atualizar(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      aux.set_nome(obj.get_nome())
      aux.set_fone(obj.get_fone())
      aux.set_email(obj.get_email())
      aux.set_senha(obj.get_senha())
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      cls.__pacientes.remove(aux)
      cls.salvar()

  @classmethod
  def abrir(cls):
    cls.__pacientes = []
    try:
      with open("pacientes.json", mode="r") as arquivo:
        pacientes_json = json.load(arquivo)
        for obj in pacientes_json:
          aux = Paciente(obj["_Paciente__id"], 
                        obj["_Paciente__nome"], 
                        obj["_Paciente__fone"],
                        obj["_Paciente__email"],
                        obj["_Paciente__senha"])
          cls.__pacientes.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("pacientes.json", mode="w") as arquivo:
      json.dump(cls.__pacientes, arquivo, default=vars)