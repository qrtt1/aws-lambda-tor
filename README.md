build a `tor` for AWS Lambda

## aws-lambda-tor

The project is a proof-of-concept to launch tor-proxy in the lambda context. It helps to run cralwers behind the tor proxy.


## Files

* tor: a prebuilt static linked tor
* main.py: a lambda function which to get its IP address from the tor proxy
* build.sh: a build script to make a Lambda.zip
  * start a python:3.6 docker and use the pip to install libraries
  * create the Lambda.zip for aws lambda runs in the python 3.6

## Demo


```
aws lambda invoke --invocation-type RequestResponse \
    --function-name aws-lambda-tor \
    --region ap-southeast-1 \
    --profile your-profile-name \
    outputfile.txt
```

```
cat outputfile.txt | jq -r
{"ip": "176.10.99.200", "ip_decimal": 2953470920, "country": "Switzerland", "country_iso": "CH", "port": 9563}
```

## Extras

If you want to use aws lambda layer, there is [another project](https://github.com/qrtt1/lambda-layer-tor) to provide the prebuilt tor layer.
