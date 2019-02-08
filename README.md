# python-console
A Click-based console logging utility.

#### Usage

```python
from annasys import console


console.header('hello')
# ------------------------------ HELLO ------------------------------

console.log('log')
#              -> log

console.error('error')
# [     ERROR] ! error

console.warning('warning')
# [      WARN] -> warning

console.info('info')
# [      INFO] -> info

console.success('success')
# [   SUCCESS] -> success
```

#### Customization

```python
console.header('message', width=80, fg='green', bold=True)
```

* `'message'` can be any python object (internally it uses string format to display a string representation of the object)
* `width` is an integer for how wide you want the header to be
* `fg` is the foreground color, via colorama
* `bold` is whether to use bold, via colorama

```python
console.log('status', 'message', fg='white', bold=False, color_status=False, width=12, arrow=None, include_brackets=False)
```

* `status`: This goes in front of the arrow (see below). Like the `header` function, uses `str` internally
* `message`: This goes after the arrow. Uses `str` internally
* `fg`: the foreground color, via colorama
* `bold`: bold flag, via colorama
* `color_status`: If True, colors the `status`, otherwise colors the `message`
* `width`: width of the section in front of the arrow
* `arrow`: the arrow to use between status and message, defaults to `' -> '`
* `include_brackets`: If True, adds `[]` around the status, otherwise does not
