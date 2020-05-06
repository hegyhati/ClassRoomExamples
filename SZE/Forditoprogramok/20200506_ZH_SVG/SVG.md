# Grammar

```
svgfile : SVGOPEN svgbody SVGCLOSE;

svgbody : svgentry svgbody
        | /* empty */
        ;

svgentry : svggroup
         | svgfile
         | text
         | switch
         | CIRCLE
         | RECTANGLE
         | POLYGON
         ;

text: TEXTOPEN TEXT TEXTCLOSE;

switch: SWITCHOPEN svgbody SWITCHCLOSE;

svggroup : GROUPOPEN svgbody GROUPCLOSE;

```

# Input

```
<svg width="200" height="200">
  <circle cx="20" cy="20" r="20" fill="green" />
  <rect x="110" y="110" height="30" width="30" fill="blue" />
  <g>
    <circle cx="70" cy="70" r="20" fill="purple" />
    <rect x="160" y="160" height="30" width="30" fill="red" />
  </g>
</svg>
```

```
SVGOPEN CIRCLE RECTANGLE GROUPOPEN CIRCLE RECTANGLE GROUPCLOSE SVGCLOSE

```
