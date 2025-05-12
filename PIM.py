#Importando o json, para ser exibido no fim do codigo
import json
#Criar um hash para criptografar a senha para ser exibida no json
import bcrypt 
#Não exibir a senha digitada no terminal
from getpass import getpass 

print("Bem-vindo(a) ao nosso site! Para iniciar sua jornada ao conhecimento sobre Cibersegurança, " \
"nos informe as seguintes informações: ")

respostas = {}

respostas["email"] = input("Digite o seu e-mail: ")
respostas["nome"] = input("Digite o seu nome: ")
respostas["sobrenome"] = input("Digite o seu sobrenome: ")
respostas["idade"] = input("Digite a sua idade: ")

senha = getpass("Crie a sua senha de acesso: ")
senha_codificada = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
respostas["Senha Codificada"] = senha_codificada.decode('utf-8')

print(f"\n Obrigado, {respostas['nome']}! Seus dados foram coletados e salvos com sucesso. Abaixo estará disponivel o JSON com suas informações")

json_resultado = json.dumps(respostas, indent=5)

print("\n Dados em JSON")
print(json_resultado)