import json

class Medico:
  def __init__(self, id, nome, fone, email):
    self.__id = id
    self.__nome = nome
    self.__fone = fone
    self.__email = email

  def get_id(self): return self.__id
  def get_nome(self): return self.__nome
  def get_fone(self): return self.__fone
  def get_email(self): return self.__email

  def set_id(self, id): self.__id = id
  def set_nome(self, nome): self.__nome = nome
  def set_fone(self, fone): self.__fone = fone
  def set_email(self, email): self.__email = email

  def __eq__(self, x):
    if self.__id == x.__id and self.__nome == x.__nome and self.__fone == x.__fone and self.__email == x.__email:
      return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__nome} - {self.__fone} - {self.__email}"


class NMedico:
  __medicos = []

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    id = 0
    for aux in cls.__medicos:
      if aux.get_id() - id == 1:
        id = aux.get_id()
      else:
        break
    obj.set_id(id + 1)
    cls.__medicos.append(obj)
    cls.salvar()

  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.__medicos

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for obj in cls.__medicos:
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
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      cls.__medicos.remove(aux)
      cls.salvar()

  @classmethod
  def abrir(cls):
    cls.__medicos = []
    try:
      with open("medicos.json", mode="r") as arquivo:
        medicos_json = json.load(arquivo)
        for obj in medicos_json:
          aux = Medico(obj["_Medico__id"], 
                        obj["_Medico__nome"], 
                        obj["_Medico__fone"],
                        obj["_Medico__email"])
          cls.__medicos.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("medicos.json", mode="w") as arquivo:
      json.dump(cls.__medicos, arquivo, default=vars)