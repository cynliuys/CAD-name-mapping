# ICCAD Contest cada039 : Name Mapping
2018 ICCAD CONTEST ProblemA  Smart EC : Program-Building for Name Mapping

* Team Number: cada039
* This project was developed by [Cynthia Liu](https://github.com/CynthiaYLiu), and [Chou Yun](https://github.com/TeresaChou).
* You can see our algorithm aproach in ./report


## Content
```
.
├── README.md
├── cada039
├── Makefile
├── run.sh (run case1 to case8)
├── main.cpp
├── nameMap.cpp
├── nameMap.h
├── record.cpp
├── util.cpp
├── util.h
├── write.cpp
├── script
│   ├── case0.py
│   │   ...
│   ├── case8.py
│   └── verify.py
├── output
│   └── (output json files)
├── cases8
│   └── (test cases released by organizer)
├── doc
│   └── 2018ICCADContest_ProblemA.pdf
├── report
│   └── (project final report)
└── V1
    └── (previous version)
```

## How to run the program

(1) Generate a python script for name mapping
```
$ make
$ ./cad039 <map_in.json> <python_script.py> 
```
Or generate python scrips for 8 test cases
```
$ make
$ bash run.sh
```

(2) Use python script to map from <name_in.json> to <map_out.json>
```
$ python3 <python_script.py> <name_in.json> <map_out.json>
```

## Verify

For comparing if two json file contains the same mapping.
Usage:
```
$ python3 script/verify.py <file1.json> <file2.json>
```
You will see Success! or Fail!
