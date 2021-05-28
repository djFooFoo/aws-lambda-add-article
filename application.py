def handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello darkness my old friend'
    }


if __name__ == '__main__':
    print(handler(None, None))