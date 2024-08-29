# legalgenius-backend-model

Responsible for backend LLM-related capabilities.

- This is a python flask based web application, providing APIs for upstream services.

## API Authentication.

- User must apply for `api_key_name` and `api_key` before each API call.
- the `api_key` must be added to each request header such as `Authorization: Bearer API_KEY`

## API Documentations

### Get Chat Response

endpoint: '/v1/chat/completions'
request_body:

```json
{
  "messages": [
    {
      "role": "user",
      "content": "you are helpful assistant..."
    },
    {
      "role": "assistant",
      "content": "my answer is... "
    }
  ]
}
```

response_body:

```json
{
  "message": "您好！我是一点星辰公司的法律机器人，专门为您提供法律咨询和帮助。如果您有任何法律问题或需要法律建议，随时可以向我提问。我会尽我所能为您提供准确、专业的解答。",
  "reservation_intent": "false",
  "result_message": "OK"
}
```

### Get Chat Summary

endpoint: '/v1/chat/summary'
request_body:

```json
{
  "messages": [
    {
      "role": "user",
      "content": "you are helpful assistant..."
    },
    {
      "role": "assistant",
      "content": "my answer is... "
    }
  ]
}
```

response_body:

```json
{
  "summary": "this is a sample summary.",
  "title": "this is a sample chat title."
}
```

### Get Chat Priority

endpoint: '/v1/chat/priority'
request_body:

```json
{
  "messages": [
    {
      "role": "user",
      "content": "you are helpful assistant..."
    },
    {
      "role": "assistant",
      "content": "my answer is... "
    }
  ]
}
```

response_body:

```json
{
  "priority": "this is a sample priority"
}
```
