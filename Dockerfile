# Imagen base
FROM python:3.10-slim

# Crear carpeta de trabajo
WORKDIR /app

# Copiar archivos al contenedor
COPY . .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto
EXPOSE 5000

# Ejecutar la aplicación con gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
