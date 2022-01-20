# Generated by Django 4.0.1 on 2022-01-20 05:04

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('cellphone', models.CharField(blank=True, max_length=11, verbose_name='Celular')),
                ('departamento', models.CharField(blank=True, max_length=100, verbose_name='Departamento')),
                ('ciudad', models.CharField(blank=True, max_length=100, verbose_name='Ciudad')),
                ('pais', models.CharField(blank=True, max_length=100, verbose_name='Pais')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='Direccion')),
                ('is_activate', models.BooleanField(default=False, verbose_name='Registrado')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('is_disabled', models.BooleanField(default=False)),
                ('token', models.TextField(max_length=700, verbose_name='Token')),
            ],
            options={
                'verbose_name': 'Sesión',
                'verbose_name_plural': 'Sesiones',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.CharField(max_length=100)),
                ('nombre_empresa', models.CharField(max_length=200)),
                ('nombre_comercial_empresa', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('sitio_web', models.URLField()),
                ('ciudad', models.CharField(blank=True, max_length=100, verbose_name='Ciudad')),
                ('pais', models.CharField(blank=True, max_length=100, verbose_name='Pais')),
                ('departamento', models.CharField(blank=True, max_length=100, verbose_name='Departamento')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.CharField(max_length=255, verbose_name='Nombres')),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfiles',
            },
        ),
        migrations.CreateModel(
            name='PuntoAccesoEmpresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('geolocalizacion', models.CharField(max_length=100)),
                ('estado', models.BooleanField(default=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.empresa')),
            ],
            options={
                'verbose_name': 'Punto Acceso',
                'verbose_name_plural': 'Puntos Acceso',
            },
        ),
        migrations.CreateModel(
            name='HorarioAcceso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario_inicio', models.DateTimeField()),
                ('horario_fin', models.DateTimeField()),
                ('punto_acceso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.puntoaccesoempresa')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Horario Acceso',
                'verbose_name_plural': 'Horarios Acceso',
            },
        ),
        migrations.CreateModel(
            name='ActivateUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('expiration_date', models.DateTimeField(verbose_name='Fecha de vencimiento')),
                ('is_used', models.BooleanField(default=False, verbose_name='Fue usado')),
                ('token', models.TextField(max_length=700, verbose_name='Token')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Activar de usuario',
                'verbose_name_plural': 'Activar de usuarios',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.empresa'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.ManyToManyField(related_name='user_profile', to='api.Profile'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
