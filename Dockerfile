# Usar a imagem base do Miniconda
FROM continuumio/miniconda3:latest

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o arquivo de ambiente Conda para o contêiner
COPY conda_environment.yml /app/

# Criar o ambiente Conda
RUN conda env create -f conda_environment.yml

# Ativar o ambiente Conda no Dockerfile
RUN echo "conda activate django_env" >> ~/.bashrc

# Copiar o código da aplicação para o contêiner
COPY . /app/

# Garantir que o ambiente Conda esteja ativado durante a execução
CMD ["bash", "-c", "source ~/.bashrc && tail -f /dev/null"]
