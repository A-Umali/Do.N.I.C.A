class BaseModule:
    POSITIVE = ["YES", "YEAH", 'SURE', "YAH", "YA"]
    NEGATIVE = ["NO", "NEGATIVE", "NAH", "NA", "NOPE"]

    def __init__(self, key_words_assigned, raw_text, sub_words, key_words, assistant, c):
        self.key_words_assigned = key_words_assigned
        self.raw_text = raw_text
        self.sub_words = sub_words
        self.key_words = key_words
        self.config = c.config
        self.parent_configuration = c

    def get_configuration(self, key, section='MODULES'):
        try:
            value = self.config[section][key]
        except KeyError:
            print("API KEYS FOR %s" + " is not provided in the config.ini file."
                                           "Refer back to the docs." % key)
            return False
        if value:
            return value
        print("The correct API KEY wasnt privded or wasnt provided at all for" + key)
        return False

    def write_configuration(self, key, value, section='MODULES'):
        self.config.set(section, key, value)
        with open(self.parent_configuration.abs_filename, 'w') as configfile:
            self.config.write(configfile)
            configfile.close()
        return value

