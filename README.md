Parameters and usage.
Parameters:
    -d, --data, default="./data/ Absolute path to directory with log files(default: ./data/
    -e, --ext, default="png" Saved plot extension(default=png). Available: png, svg, pdf
    -s, --show, default=False Show plot in runtime(default=False)
    -t, --type, default='./data/transformConfig.xml' Absolute path to transformConfig.xml
  

General usage:
    python ./parser.py -d "c:/path/to/log/data/" -t './data/transformConfig.xml' 
To see plot in console:
    python ./parser.py -d "./data/" -s True
To save to svg:
    python ./parser.py -d "./data/" -e "svg"