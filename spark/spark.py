from pyspark.sql import SparkSession
from pyspark.sql import DataFrame
from dto.models import *


class Spark:
    """
        Spark 클래스 정의
    """

    # Constructor
    def __init__(self, configDto=None, sparkConf=None):
        try:
            if configDto is None and sparkConf is None:
                self.spark = SparkSession \
                    .builder \
                    .getOrCreate()
            else:
                self.spark = SparkSession \
                    .builder \
                    .config(conf=sparkConf.getSparkProps()) \
                    .getOrCreate()

                self.configDto = configDto
                print('CONFIGDTO ::: {}'.format(self.configDto))
        except Exception as e:
            print(e)

    # Getter SparkSession
    def getSparkSession(self):
        return self.session

    # Extract DataSource
    def extract_jdbc(self) -> None:
        if self.configDto is not None:
            formatter = 'jdbc'
            jdbcOption: JdbcInfo = self.configDto.jdbcOption
            self.spark.read \
                .format(formatter) \
                .options(**jdbcOption.__dict__) \
                .load() \
                .createOrReplaceTempView(jdbcOption.getAttrValue('dbtable'))

    # Translate DataSource
    def transform_data(self) -> dict:
        result = {}
        print('Transform_DATA ::: {}'.format(self.configDto.queryOption))
        queryOptions = self.configDto.queryOption
        query = queryOptions.getAttrValue('query')
        idx = queryOptions.getAttrValue('index.name')
        pk = queryOptions.getAttrValue('primary.key')
        df = self.spark.sql(query)
        df.show(3)
        result['df'] = df
        result['idx'] = idx
        result['pk'] = pk
        return result

    # Save To Elasticsearch
    @staticmethod
    def save_to_es(dataframeDict):
        dfDict = dataframeDict
        if dfDict is not None:
            df = dfDict['df']
            df \
                .write \
                .format("org.elasticsearch.spark.sql") \
                .option("es.nodes", "http://127.0.0.1:9200") \
                .option("es.mapping.id", dfDict['pk']) \
                .option("es.resource", "%s/%s" % (dfDict['idx'], "_doc")) \
                .mode("append") \
                .save()
