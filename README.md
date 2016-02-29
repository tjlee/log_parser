Parameters and usage.
Parameters:
    -d, --data, default="./data/ Absolute path to directory with log files(default: ./data/
    -e, --ext, default="png" Saved plot extension(default=png). Available: png, svg, pdf
    -s, --show, default=False Show plot in runtime(default=False)
    -t, --types, default=["getGoodsCatalogWithTi", "importActionsWithTi", "importCashiersWithTi",
        "getCardsCatalogWithTi","writeObjectsToFile", "insertEvent", "getNewProductsToCash", "processDocument"], Data types to analyze(default:"getGoodsCatalogWithTi" "importActionsWithTi" "importCashiersWithTi" "getCardsCatalogWithTi" "writeObjectsToFile" "insertEvent" "getNewProductsToCash" "processDocument"
                        To pass parameters use: -t "one" "two" "four"

General usage:
    python ./parser.py -d "c:/path/to/log/data/" -t "insertEvent" "processDocument" "importCashiersWithTi" 
To see plot in console:
    python ./parser.py -d "./data/" -t "insertEvent" "processDocument" "importCashiersWithTi" -s True
To save to svg:
    python ./parser.py -d "./data/" -t "insertEvent" "processDocument" "importCashiersWithTi" -e "svg"