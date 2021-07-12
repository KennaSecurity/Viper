FROM debian
USER root
RUN apt update && apt install python3 python3-pip -y
RUN pip3 install requests jsonlines pandas urllib3
RUN mkdir data
ADD . .
CMD ["viper.py"]
ENTRYPOINT ["python3"]