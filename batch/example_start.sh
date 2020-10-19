#!/bin/sh

#usage()
#{
#        echo "usage) $0 <collection> <config> <mode>"
#        echo
#        echo "collection:"
#        echo "    Collection name"
#        echo
#        echo "config:"
#        echo "    Config file path"
#        echo
#        echo "mode:"
#        echo "    tokenize, word2vec, doc2vec, elastic"
#        echo "    - tokenize : jbt      -> tokenize"
#        echo "    - word2vec : tokenize -> word2vec"
#        echo "    - doc2vec  : word2vec -> doc2vec"
#        echo "    - elasticsearch  : word2vec -> elasticsearch"
#        echo
#        exit $1
#}

# -------------------------------------------
# SOURCE_HOME
# -------------------------------------------
SOURCE_HOME=`dirname "$0"`
# echo SOURCE_HOME that print "NOW PATH"
export SOURCE_HOME=`cd "$SOURCE_HOME/.."; pwd`

# -------------------------------------------
# Scala/Python HOME
# -------------------------------------------
export PATH=$PATH:/usr/local/scala/bin

# Pyspark conf
export SPARK_HOME=/Users/jinokku/DEV/spark-2.4.6-bin-hadoop2.6
export SPARK_MASTER_IP='127.0.0.1'
export SPARK_LOCAL_IP='127.0.0.1'
export PYSPARK_PYTHON=/usr/local/bin/python3.7

##Python Execution Source
BINARY=$SOURCE_HOME/structapi.py
echo $BINARY
spark-submit --packages="org.elasticsearch:elasticsearch-spark-20_2.11:7.8.0","mysql:mysql-connector-java:5.1.48" $BINARY /config/prototype.yml
# -------------------------------------------
# ENVIRONEMNT
# -------------------------------------------
#PROFILE=$KTTA_HOME/batch/environment
#if [ -f $PROFILE ]; then
#        . $PROFILE
#        echo "set global environment: $PROFILE"
#        echo
#else
#        echo "no such global environment: $PROFILE"
#        exit 1
#fi
#
## -------------------------------------------
## ARGUMENT
## -------------------------------------------
#COLLECTION=$1
#if [ "$#" != "0" ]; then shift; fi
#if [ "x$COLLECTION" = "x" ]; then usage 1; fi
#
#CONFIG=$1
#if [ "$#" != "0" ]; then shift; fi
#if [ "x$CONFIG" = "x" ]; then usage 1; fi
#
#MODE=$1
#if [ "$#" != "0" ]; then shift; fi
#if [ "x$MODE" = "x" ]; then usage 1; fi
#
## -------------------------------------------
## CLASSPATH
## -------------------------------------------
#CLASSPATH=$KTTA_HOME/lib
#for f in `find $KTTA_HOME/lib -name "*.jar"`
#do
#	CLASSPATH=$CLASSPATH:$f
#done
#
## -------------------------------------------
## RUN
## -------------------------------------------
#

##JNI Lib path
##JAVA_LIB_PATH=$KTTA_HOME/module/kobrick
#
##RUNAS="$JAVA_HOME/bin/java -Xms32G -Xmx32G -XX:NewRatio=3 -XX:+UseParallelOldGC -Djava.library.path=$JAVA_LIB_PATH -classpath $CLASSPATH $BINARY -c $CONFIG -m $MODE -t $COLLECTION"
##RUNAS="$JAVA_HOME/bin/java -Xms64G -Xmx64G -XX:NewRatio=3 -XX:+UseParallelOldGC -Djava.library.path=$JAVA_LIB_PATH -classpath $CLASSPATH $BINARY -c $CONFIG -m $MODE -t $COLLECTION"
#
#echo run as: $RUNAS
#$RUNAS
