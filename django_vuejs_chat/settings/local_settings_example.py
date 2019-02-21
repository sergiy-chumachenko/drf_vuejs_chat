import environ
import os

ROOT_DIR = environ.Path(__file__) - 3
env = environ.Env(
    DJANGO_DATABASE_URL=(str, 'postgres://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'),
)
environ.Env.read_env(env_file=os.path.join(str(ROOT_DIR), '.env'))

DATABASES = {
    'default': env.db('DJANGO_DATABASE_URL')
}
