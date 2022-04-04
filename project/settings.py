from envparse import env

env.read_envfile()

DATABASE_URL = env("DATABASE_URL")
