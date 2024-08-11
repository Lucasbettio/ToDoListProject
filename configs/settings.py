from dotenv import load_dotenv
from dynaconf import Dynaconf

load_dotenv()

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=["./settings.toml", "./.env"]
)