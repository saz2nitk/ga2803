FROM ubuntu

RUN apt-get update
RUN apt-get -y install python3
RUN apt-get install -y git
RUN apt-get -y install python3-pip
RUN mkdir project
RUN cd project
RUN git clone https://github.com/saz2nitk/ga2803.git
RUN cd ga2803
RUN pip3 install -r ga2803/requirements.txt

CMD ["python3","ga2803/bin/summarize.py"]
