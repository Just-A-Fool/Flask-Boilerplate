from dotenv import load_dotenv
import os

load_dotenv()


DB_URL = os.getenv('DATABASE_URL')
ENV = os.getenv('ENV')
PORT = os.getenv('PORT')
JWT_SECRET = os.getenv('JWT_SECRET')


config = {
    'ENV': ENV,
    'PORT': PORT,
    'DB_URL': DB_URL,
    'JWT_SECRET': JWT_SECRET,
}
