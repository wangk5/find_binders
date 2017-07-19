FROM python:2.7.13
MAINTAINER kjwang <wangk5@email.chop.edu>

ADD findBider.py /

CMD [ "python", ""./findBinder.py" ]
