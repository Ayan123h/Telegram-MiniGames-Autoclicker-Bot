from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int 
    API_HASH: str 

    LOGIN_SLEEP: list[int] = [60, 360]
    MINI_SLEEP: list[int] = [5, 15]
    BIG_SLEEP: list[int] = [10800, 18000]

    BOT_MOOD_SEQUENTIAL: bool= False
    ACCOUNTS_MOOD_SEQUENTIAL: bool= True



    ACTIVE_BOTS: dict[str, dict] = {
        "blum": {"Active": True, "REF_ID": ""},
        "catsgang": {"Active": False, "REF_ID": ""},
        "catsvsdogs": {"Active": True, "REF_ID": ""},
        "cexio": {"Active": True, "REF_ID": ""},
        "goats": {"Active": True, "REF_ID": ""},
        "major": {"Active": True, "REF_ID": ""},
        "notpixel": {"Active": True, "REF_ID": ""},
        "tomarket": {"Active": True, "REF_ID": ""}
    }
    


global_settings = Settings()
