FROM debian
USER root
RUN apt-get update && apt-get install python3-full python3-pip -y
RUN pip3 install requests jsonlines pandas urllib3
RUN mkdir data
ADD . .
CMD ["viper.py"]
ENTRYPOINT ["python3"]