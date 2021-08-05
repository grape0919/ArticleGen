import yaml
import os
from enum import Enum
class Config(dict):
    CONF_PATH = os.path.join(os.getcwd(),'conf/config.yaml')

    class Key(Enum):
        NAVER = 0
        GOOGLE = 0
        CLIENT_ID = 1
        CLIENT_SECRET_ID = 1

    NAVER_CLIENT_ID = ''
    NAVER_CLIENT_SECRET_ID = ''

    def load(self):
        print("Config load")
        with open(self.CONF_PATH) as f:
            temp = yaml.load(f, Loader=yaml.FullLoader)
            self.update(temp)
            f.close()

    def save(self):
        print("Config save")
        with open(self.CONF_PATH, 'w', encoding='utf8') as f:
            self.update(
                {
                    'NAVER':
                    {
                        self.CLIENT_ID:self[self.CLIENT_ID_KEY]
                        ,self.CLIENT_SECRET_ID:self[self.CLIENT_SECRET_ID_KEY]
                    }
                })
            print('new config : ' + str(self.copy()))
            yaml.dump(self.copy(), f)
            f.close()

    def init_conf(self):
        print("Config initalize")
        self.save()

if __name__ == '__main__':
    conf = Config()
    # conf.init_conf()
    conf.load()
    print(conf)

    print(conf[conf.Key.NAVER.name][conf.Key.CLIENT_ID.name])
