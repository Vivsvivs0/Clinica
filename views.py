from models.paciente import Paciente, NPaciente
from models.medico import Medico, NMedico
from models.consulta import Consulta, NConsulta
import datetime

class View:
  def paciente_listar():
    return NPaciente.listar()
  
  def paciente_listar_id(id):
    return NPaciente.listar_id(id)

  def paciente_inserir(nome, fone, email, senha):
    paciente = Paciente(0, nome, fone, email, senha)
    NPaciente.inserir(paciente)

  def paciente_atualizar(id, nome, fone, email, senha):
    paciente = Paciente(id, nome, fone, email, senha)
    NPaciente.atualizar(paciente)
    
  def paciente_excluir(id):
    paciente = Paciente(id, "", "", "", "")
    NPaciente.excluir(paciente)    

  def paciente_admin():
    for paciente in View.paciente_listar():
      if paciente.get_nome() == "admin": return
    View.paciente_inserir("admin", "999999999", "admin", "admin")

  def paciente_login(email, senha):
    for paciente in View.paciente_listar():
      if paciente.get_email() == email and paciente.get_senha() == senha:
        return paciente
    return None

  def consulta_listar():
    return NConsulta.listar()

  def consulta_listar_paciente(paciente):
    r = []
    for horario in View.consulta_listar():
      if horario.get_id_paciente() == paciente.get_id():
        r.append(horario)
    return r
  
  def consulta_listar_mes():
    r = []
    hoje = datetime.datetime.today()
    fds = hoje + datetime.timedelta(days = 30)
    for horario in View.consulta_listar():
      if fds.date() >= horario.get_data().date() >= hoje.date():
        r.append(horario)
    return r 
  
  def consulta_nao_confirmada():
    return NConsulta.listar_nao_confirmados()
  
  def consulta_listar_id(id):
    return NConsulta.listar_id()

  def consulta_inserir(data, confirmado, id_paciente, id_medico):
    NConsulta.inserir(Consulta(0, data, confirmado, id_paciente, id_medico))

  def consulta_atualizar(id, data, confirmado, id_paciente, id_medico):
    NConsulta.atualizar(Consulta(id, data, confirmado, id_paciente, id_medico))

  def consulta_excluir(id):
    NConsulta.excluir(Consulta(id, "", "", 0, 0))

#   def consulta_periodo(obj, inicio, final):
#     data_inicio = datetime.datetime.strptime(f"{inicio} 00:00", "%d/%m/%Y %H:%M")
#     data_fim = datetime.datetime.strptime(f"{final} 23:59", "%d/%m/%Y %H:%M")
#     if data_inicio <= obj.get_data() <= data_fim: return True

  def consulta_solicitados():
    r = []
    for obj in NConsulta.listar_nao_confirmados():
      if obj.get_id_paciente(): r.append(obj)
    return r
  
  def medico_listar():
    return NPaciente.listar()
  
  def medico_listar_id(id):
    return NPaciente.listar_id(id)
  
  def medico_inserir(nome, fone, email, senha):
    medico = Paciente(0, nome, fone, email, senha)
    NPaciente.inserir(medico)

  def medico_atualizar(id, nome, fone, email, senha):
    medico = Paciente(id, nome, fone, email, senha)
    NPaciente.atualizar(medico)
    
  def medico_excluir(id):
    medico = Paciente(id, "", "", "", "")
    NPaciente.excluir(medico)    