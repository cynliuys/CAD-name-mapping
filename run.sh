make
echo "running case1..."
./cada039 cases8/case1.json script/case1.py
python3 script/case1.py cases8/case1.map_in.json output/case1.out.json
python3 script/verify.py cases8/case1.json output/case1.out.json 
wc -m script/case1.py
echo "running case2..."
./cada039 cases8/case2.json script/case2.py
python3 script/case2.py cases8/case2.map_in.json output/case2.out.json
python3 script/verify.py cases8/case2.json output/case2.out.json 
wc -m script/case2.py
echo "running case3..."
./cada039 cases8/case3.json script/case3.py
python3 script/case3.py cases8/case3.map_in.json output/case3.out.json
python3 script/verify.py cases8/case3.json output/case3.out.json 
wc -m script/case3.py
echo "running case4..."
./cada039 cases8/case4.json script/case4.py
python3 script/case4.py cases8/case4.map_in.json output/case4.out.json
python3 script/verify.py cases8/case4.json output/case4.out.json 
wc -m script/case4.py
echo "running case5..."
./cada039 cases8/case5.json script/case5.py
python3 script/case5.py cases8/case5.map_in.json output/case5.out.json
python3 script/verify.py cases8/case5.json output/case5.out.json 
wc -m script/case5.py
echo "running case6..."
./cada039 cases8/case6.json script/case6.py
python3 script/case6.py cases8/case6.map_in.json output/case6.out.json
python3 script/verify.py cases8/case6.json output/case6.out.json 
wc -m script/case6.py
echo "running case7..."
./cada039 cases8/case7.json script/case7.py
python3 script/case7.py cases8/case7.map_in.json output/case7.out.json
python3 script/verify.py cases8/case7.json output/case7.out.json 
wc -m script/case7.py
echo "running case8..."
./cada039 cases8/case8.json script/case8.py
python3 script/case8.py cases8/case8.map_in.json output/case8.out.json
python3 script/verify.py cases8/case8.json output/case8.out.json 
wc -m script/case8.py
echo "running case0..."
./cada039 cases8/case0.json script/case0.py
python3 script/case0.py cases8/case0.map_in.json output/case0.out.json
python3 script/verify.py cases8/case0.json output/case0.out.json 
wc -m script/case0.py
