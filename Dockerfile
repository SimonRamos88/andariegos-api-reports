# Usa una imagen oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos del proyecto
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto que usa Flask (opcional, informativo)
EXPOSE 5000

# Ejecuta la aplicación
CMD ["flask", "run", "--host=0.0.0.0"]
