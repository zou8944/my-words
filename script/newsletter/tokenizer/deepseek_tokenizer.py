# pip3 install transformers
# python3 deepseek_tokenizer.py
import os

import transformers

chat_tokenizer_dir = os.path.dirname(os.path.abspath(__file__))


def calculate_tokenizer(msg: str) -> int:
    tokenizer = transformers.AutoTokenizer.from_pretrained(chat_tokenizer_dir, trust_remote_code=True)
    result = tokenizer.encode(msg)
    return len(result)


if __name__ == "__main__":
    print(calculate_tokenizer("你好，世界！"))
