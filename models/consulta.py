import json
import datetime

class Consulta:
  def _init_(self, id, confirmado, data, id_paciente, id_medico):
    self.__id = id
    self.__confirmado = confirmado
    self.__data = data
    self.__id_paciente = id_paciente
    self.__id_medico = id_medico

  def get_id(self): return self.__id
  def get_confirmado(self): return self.__confirmado
  def get_data(self): return self.__data
  def get_id_paciente(self): return self.__id_paciente
  def get_id_medico(self): return self.__id_medico

  def set_id(self, id): self.__id = id
  def set_confirmado(self, confirmado): self.__confirmado = confirmado
  def set_data(self, data): self.__data = data
  def set_id_paciente(self, id_paciente): self.__id_paciente = id_paciente
  def set_id_medico(self, id_medico): self.__id_medico = id_medico

  def _eq_(self, x):
    if self._id == x.id and self.confirmado == x.confirmado and self.data == x.data and self.id_medico == x.id_medico and self.id_paciente == x._id_paciente:
      return True
    return False

  def _str_(self):
    return f"{self._id} - {self.confirmado} - {self.data.strftime('%d/%m/%Y %H:%M')} - {self._id_paciente} - {self.id_medico}"

  def to_json(self):
    return {
      'id': self.__id,
      'confirmado': self.__confirmado,
      'data': self.__data.strftime('%d/%m/%Y %H:%M'),
      'id_paciente': self.__id_paciente,
      'id_medico': self.__id_medico}


class NConsulta:
  __consultas = []

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    id = 0
    for aux in cls.__consultas:
      if aux.get_id() > id: id = aux.get_id()
    obj.set_id(id + 1)
    cls.__consultas.append(obj)
    cls.salvar()

  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.__consultas

  @classmethod
  def listar_nao_confirmados(cls):
    cls.abrir()
    nao_confirmados = []
    aux = datetime.datetime.now()
    hoje = datetime.datetime(aux.year, aux.month, aux.day)
    for obj in cls.__consultas:
      if not obj.get_confirmado() and obj.get_data() > hoje:
        nao_confirmados.append(obj)
    return nao_confirmados

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for obj in cls.__consultas:
      if obj.get_id() == id: return obj
    return None

  @classmethod
  def atualizar(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      aux.set_confirmado(obj.get_confirmado())
      aux.set_data(obj.get_data())
      aux.set_id_medico(obj.get_id_medico())
      aux.set_id_paciente(obj.get_id_paciente())
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      cls.__consultas.remove(aux)
      cls.salvar()

  @classmethod
  def abrir(cls):
    cls.__consultas = []
    try:
      with open("consultas.json", mode="r") as arquivo:
        consultas_json = json.load(arquivo)
        for obj in consultas_json:
          aux = Consulta(
            obj["id"], obj["confirmado"],
            datetime.datetime.strptime(obj["data"], "%d/%m/%Y %H:%M"),
            obj["id_paciente"], obj["id_medico"])
          cls.__consultas.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("consultas.json", mode="w") as arquivo:
      json.dump(cls.__consultas, arquivo, default=Consulta.to_json)