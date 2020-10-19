class SparkProperties:
    def __init__(self, **kwargs):
        """
        YAML 파일의 spark.properties 하위에 정의 해놓은 설정 값들이
        Dict 타입의 속성으로 설정됨.
        :param kwargs:
        """
        self.__dict__ = kwargs


class InfoObj:
    def getAttrValue(self, key):
        return self.__dict__.__getitem__(key)

    def getAttrValueByAll(self):
        print(self.__dict__.items())
        print(type(self.__dict__))
        d = self.__dict__
        for key, value in d.items():
            print(key, ":", value)


class JdbcInfo(InfoObj):
    def __init__(self, **kwargs):
        self.__dict__ = kwargs


class QueryInfo(InfoObj):
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

