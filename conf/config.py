import yaml
import os
from enum import Enum
class Config():
    CONF_PATH = os.path.join(os.getcwd(),'conf/config.yaml')

    config_dump = {}

    NAVER_CLIENT_ID:str = ''
    NAVER_CLIENT_SECRET_ID:str = ''
    GOOGLE_CLIENT_ID:str = ''
    GOOGLE_CLIENT_SECRET_ID:str = ''

    DB_HOST:str = ''
    DB_USER:str = '' 
    DB_PASSWORD:str = ''

    class Key(Enum):
        NAVER = 0x11
        GOOGLE = 0x12
        CLIENT_ID = 0x21
        CLIENT_SECRET_ID = 0x22

        DB = 0x13
        TYPE = 0x23
        HOST = 0x24
        USER = 0x25
        PASSWORD = 0x26

    def load(self):
        print("Config load")
        with open(self.CONF_PATH) as f:
            self.config_dump = yaml.load(f, Loader=yaml.FullLoader)
            f.close()

        self.NAVER_CLIENT_ID = self.config_dump[self.Key.NAVER.name][self.Key.CLIENT_ID.name]
        self.NAVER_CLIENT_SECRET_ID = self.config_dump[self.Key.NAVER.name][self.Key.CLIENT_SECRET_ID.name]
        self.GOOGLE_CLIENT_ID = self.config_dump[self.Key.GOOGLE.name][self.Key.CLIENT_ID.name]
        self.GOOGLE_CLIENT_SECRET_ID = self.config_dump[self.Key.GOOGLE.name][self.Key.CLIENT_SECRET_ID.name]
        self.DB_HOST = self.config_dump[self.Key.DB.name][self.Key.HOST.name]
    
    def save(self):
        print("Config save")
        with open(self.CONF_PATH, 'w', encoding='utf8') as f:
            self.config_dump = {(
                {
                    'NAVER':
                    {
                        self.Key.CLIENT_ID.name : self.config_dump[self.Key.NAVER.name][self.Key.CLIENT_ID.name],
                        self.Key.CLIENT_SECRET_ID.name : self.config_dump[self.Key.NAVER.name][self.Key.CLIENT_SECRET_ID.name]
                    },
                    'GOOGLE':
                    {
                        self.Key.CLIENT_ID.name : self.config_dump[self.Key.GOOGLE.name][self.Key.CLIENT_ID.name],
                        self.Key.CLIENT_SECRET_ID.name : self.config_dump[self.Key.GOOGLE.name][self.Key.CLIENT_SECRET_ID.name]
                    }
                })}
            print('new config : ', self.config_dump)
            yaml.dump(self.config_dump, f)

            f.close()

    def init_conf(self):
        print("Config initalize")
        self.save()

if __name__ == '__main__':
    conf = Config()
    # conf.init_conf()
    conf.load()
    print(conf.config_dump[conf.Key.NAVER.name][conf.Key.CLIENT_ID.name])
    print(conf.NAVER_CLIENT_ID)
    print(conf.config_dump[conf.Key.NAVER.name][conf.Key.CLIENT_SECRET_ID.name])
    print(conf.NAVER_CLIENT_SECRET_ID)
    print(conf.Key.CLIENT_SECRET_ID.name)

