import yaml

class Config(dict):
    CONF_PATH = './conf/config.yaml'
    CLIENT_ID = 'iLSTcLpJKsaBETLkEHOq'
    CLIENT_ID_KEY = "CLIENT_ID"
    CLIENT_SECRET_ID = '_SBXwc4_ht'
    CLIENT_SECRET_ID_KEY = "CLIENT_SECRET_ID"

    def load(self):
        print("Config load")
        with open(self.CONF_PATH) as f:
            temp = yaml.load(f, Loader=yaml.FullLoader)
            self.update(temp)
            f.close()

    def save(self):
        print("Config save")
        with open(self.CONF_PATH, 'w', encoding='utf8') as f:
            self.update({
                self.CLIENT_ID:self[self.ADMIN_ID_KEY]
                ,self.ADMIN_PASSWD_KEY:self[self.ADMIN_PASSWD_KEY]
                ,self.DOWNLOAD_FILE_FORM_KEY:self[self.DOWNLOAD_FILE_FORM_KEY]
                ,self.TIMER_KEY:self[self.TIMER_KEY]
                ,self.HOMEPATH_KEY:self[self.HOMEPATH_KEY]
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

    print(conf[conf.ADMIN_ID_KEY])
