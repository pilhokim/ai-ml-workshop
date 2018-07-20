def lambda_handler(event, context):
    import boto3
    import json
    
    sagemaker = boto3.client('runtime.sagemaker')
    endpoint_name = 'DEMO-Seq2SeqEndpointConfig-2018-03-14-13-26-43'
    
    sentences = event["sentences"]

    payload = {"instances" : []}
    for sent in sentences:
        payload["instances"].append({"data" : sent["query"]})
    
    response = sagemaker.invoke_endpoint(EndpointName=endpoint_name, 
                                       ContentType='application/json', 
                                       Body=json.dumps(payload))
    
    response = response["Body"].read().decode("utf-8")
    response = json.loads(response)
    
    return response
