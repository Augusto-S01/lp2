#!/bin/bash

# Ativar o ambiente Conda
source /opt/conda/etc/profile.d/conda.sh
conda activate django_env

# Rodar as migrações
python manage.py migrate

# Verificar se as variáveis de superusuário foram definidas
if [ -z "$SUPERUSER_USERNAME" ] || [ -z "$SUPERUSER_EMAIL" ] || [ -z "$SUPERUSER_PASSWORD" ]; then
    echo "As variáveis de superusuário não foram definidas. O superusuário não será criado."
else
    # Verificar se o superusuário já existe
    echo "Verificando se o superusuário já existe..."
    if python manage.py shell -c "from users.models import CustomUser; print(CustomUser.objects.filter(username='$SUPERUSER_USERNAME').exists())" | grep -q "True"; then
        echo "O superusuário já existe."
    else
        echo "Criando superusuário..."

        # Criar o superusuário sem a senha
        python manage.py createsuperuser --noinput \
            --username "$SUPERUSER_USERNAME" \
            --email "$SUPERUSER_EMAIL"

        # Definir a senha programaticamente
        echo "Definindo a senha do superusuário..."
        python manage.py shell <<EOF
from users.models import CustomUser  # Importando o modelo personalizado
user = CustomUser.objects.get(username='$SUPERUSER_USERNAME')
user.set_password('$SUPERUSER_PASSWORD')
user.save()
EOF

        echo "Superusuário criado com sucesso."
    fi
fi

# Iniciar o servidor Django
python manage.py runserver 0.0.0.0:8000
