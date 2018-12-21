# translater
A python function to translate into the language of each country

# example

```python
from translater import translate

print(translate('hello')) # -> こんにちは
print(translate('hello', target_lang='de')) # -> Hallo
print(translate('hello', target_lang='ko')) # -> 여보세요
print(translate('hello', target_lang='fr')) # -> Bonjour

print(translate('こんにちは')) # -> Hello
print(translate('Bonjour', source_lang='fr', target_lang='en')) # -> Hello
```