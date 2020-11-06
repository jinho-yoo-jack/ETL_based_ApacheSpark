# Set SparkConf
from pyspark import SparkConf


class SparkConfig:
    """ Set SparkConf """
    def __init__(self, configDto, sparkConf):
        """
        SparkConf 객체를 생성하고, Spark의 Properties 설정한다.
            :param configObj: YAML parse to Object
            :param sparkConf: SparkConf Object
        """
        # Create pyspark.SparkConf
        self.sparkConf = sparkConf
        # Load SparkProperties from configFile
        self.sparkProperties = configDto.sparkProps
        self.jdbcOptions = configDto.jdbcOption
        self.queryOptions = configDto.queryOption
        # SparkConf() 객체의 Spark 속성(Properties) 값 설정
        self.setSparkProps()

    def setSparkProps(self):
        """
        Spark Application(Spark Driver)의 Properties 설정
            :return: None
        """
        for key in self.sparkProperties.__dict__.items():
            print("sparkInfo key ::: {}".format(key))
            getattr(self.sparkConf, "set")(key[0], key[1])

        print('SparkConf Properties ::: {}'.format(self.sparkConf.getAll()))

    def getSparkProps(self) -> SparkConf:
        """
        Spark 드라이버의 Properties가 설정된 SparkConf 객체 리턴
            :return: SparkConf
        """
        return self.sparkConf

