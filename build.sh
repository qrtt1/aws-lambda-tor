docker run --rm -v `pwd`/build:/data python:3.6 pip install PySocks -t /data
cp tor build/
cp *.py build/
cd build
zip -r ../Lambda.zip *
