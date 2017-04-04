# unboxer
Software and datasets for the PhD thesis "From Logic to Language: Natural Language Generation from Logical Forms"

## Surface Realization

The code that implements the surface realization algorithm by composition from Chapter 3 is in _src/unboxer/drx2txt.py_

It can be used as a Python module:

```python
parser = DRGParser()
parser.parse_tup_lines(LDRG_FILE)
print (unbox(parser.drg))
```
*LDRG_FILE* is a file containing a Lexicalized Discourse Representation Graph as output by Boxer. An example is in the file _examples/example.ldrg_. There is a helper script in src/gold2surface.py that reads an LDRG from the standard input and prints out the generated surface form:

```
cat examples/example.ldrg | src/gold2surface.py
```

