#!/bin/bash

echo  "interaction with HDFS"

hdfs dfs -put 'filename' diretorio_destino_hdfs
hdfs dfs -get /diretorio_hdfs/arquivo
hdfs dfs -put filename diretorio_destino_hdfs
hdfs dfs -help
