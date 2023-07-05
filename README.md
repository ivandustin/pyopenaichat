# pyopenaichat

A simple wrapper for OpenAI Chat Completion API.

## Install

### Pip

```
pip install git+https://github.com/ivandustin/pyopenaichat.git
```

### Poetry

```
poetry add git+https://github.com/ivandustin/pyopenaichat.git
```

## Example

```python
from pyopenaichat import chat, user, assistant, system, function

messages = [
    system("Your name is Alice."),
    user("Who are you?")
]
message = chat(messages)
print(message)
```

Output

```
{
  "role": "assistant",
  "content": "Hello! My name is Alice. How can I assist you today?"
}
```
