def handler(event, context):
  return {
      "statusCode":
      200,
      "body":
      f"Hello, World! Your request was received at {event['requestContext']['time']}.",
  }
