# Repositorio do Curso de Especializacao Tecnica
#### Criar ambiente com virtualenv
virtualenv -p /usr/bin/python3.5 env
#### ativar ambiente
source env/bin/activate
#### instalando bibliotecas 
pip install -r requirements.txt
#### executando a aplicacao
python run.py


## Instalando o sqlitebrowser para visualizar banco de dados da aplicação

sudo add-apt-repository -y ppa:linuxgndu/sqlitebrowser
sudo apt-get update
sudo apt-get install sqlitebrowser
