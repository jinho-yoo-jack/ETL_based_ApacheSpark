import sys
import os
from pyspark import SparkConf
from pyspark.sql.functions import *
from spark.spark import Spark
from spark.sparkConfig import SparkConfig
from utils.ArgsUtil import ArgsUtil

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def main():
    configFile = sys.argv[1]
    fullPath = ROOT_DIR + configFile
    configDto: ArgsUtil = ArgsUtil(fullPath)

    # 1. Load SparkConfig through UserConfigFile
    sparkCfg: SparkConfig = SparkConfig(configDto, SparkConf())
    # 2. Create Spark Instance with sparkCfg
    spark: Spark = Spark(configDto, sparkCfg)
    # 3. After Read jdbc, Crate SparkSQL Table
    spark.extract_jdbc()
    # 4. Execute SELECT Query
    transformDf: dict = spark.transform_data()
    # 5. Save To Elasticsearch
    spark.save_to_es(transformDf)


if __name__ == '__main__': main()
