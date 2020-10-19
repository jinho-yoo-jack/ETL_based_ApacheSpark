import yaml
from dto.models import *
"""

"""


class ArgsUtil:
    def __init__(self, configFilePath, idx=0):
        try:
            if configFilePath is not None:
                self.yamlObj = self.getYamlToObject(configFilePath)
                self.sparkProps: SparkProperties = SparkProperties(**self.yamlObj['spark.properties'])
                self.jdbcOption: JdbcInfo = JdbcInfo(**self.yamlObj['input'][idx]['config'])
                self.queryOption: QueryInfo = QueryInfo(**self.yamlObj['input'][idx]['data'])
            else:
                raise Exception
        except Exception as e:
            print('Occur Exception ::: {}'.format(e))

    @staticmethod
    def getYamlToObject(configFilePath):
        try:
            with open(file=configFilePath, mode="r") as f:
                config = yaml.load(f, Loader=yaml.FullLoader)
            return config
        except Exception as e:
            raise Exception(e)


if __name__ == '__main__':
    """ TestCode """
    arg = ArgsUtil('/Users/jinokku/PycharmProjects/pythonProject/config/prototype.yml')
    print(type(arg.queryOption))
    print(arg.queryOption.getAttrValueByAll())
