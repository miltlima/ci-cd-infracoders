# Use a base image do Python
FROM python:3.9-slim-buster

# Defina um diretório de trabalho para a aplicação
WORKDIR /app

# Copie o arquivo de requisitos (requirements.txt) para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copie todos os arquivos do aplicativo para o diretório de trabalho
COPY . .
# Configure as variáveis de ambiente para o usuário não-root (opcional)
ENV USER=appuser
ENV UID=1000
ENV GID=1000

# Crie um usuário não-root (opcional)
RUN addgroup --gid $GID $USER && \
    adduser --uid $UID --gid $GID --disabled-password --gecos "" $USER

# Alterne para o usuário não-root (opcional)
USER $USER
# Exponha a porta em que o aplicativo está ouvindo
EXPOSE 8000

# Inicie o aplicativo FastAPI usando o Uvicorn como servidor ASGI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
