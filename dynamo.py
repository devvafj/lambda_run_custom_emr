from boto3.dynamodb.types import TypeDeserializer


def ddb_deserialize(item, type_deserializer = TypeDeserializer()):
    return type_deserializer.deserialize({"M": item})