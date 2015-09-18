<<<<<<< HEAD
all: outfile diff

term: nooutfile diff

outfile: 
	files=`ls *xml`; for the_file in $$files; do \
	     BASE=`basename  $$the_file .xml`;\
	     EXT=`echo "$$the_file"|awk -F . '{print $$NF}'`;\
	     OUT_DIR=final;\
	     OUT_FILE=$$OUT_DIR/$${BASE}_test_;\
	     command="rstxml2xml.py -o $$OUT_FILE $$the_file";\
	     eval $$command;\
	      done

nooutfile: 
	files=`ls *xml`; for the_file in $$files; do \
	     BASE=`basename  $$the_file .xml`;\
	     EXT=`echo "$$the_file"|awk -F . '{print $$NF}'`;\
	     OUT_DIR=final;\
	     OUT_FILE=$$OUT_DIR/$${BASE}_test_;\
	     command="python ../rstxml2xml.py $$the_file" > $$OUT_FILE;\
	     eval $$command;\
	      done
diff:
	cd final; files=`ls *xml`; for the_file in $$files; do \
	     BASE=`basename  $$the_file .xml`;\
	     EXT=`echo "$$the_file"|awk -F . '{print $$NF}'`;\
	     TEST_FILE=$${BASE}_test_;\
	    diff $$the_file $$TEST_FILE;\
	    done

clean:
	rm -f final/*_test_

=======
all: outfile diff

term: nooutfile diff

outfile: 
	files=`ls *xml`; for the_file in $$files; do \
	     BASE=`basename  $$the_file .xml`;\
	     EXT=`echo "$$the_file"|awk -F . '{print $$NF}'`;\
	     OUT_DIR=final;\
	     OUT_FILE=$$OUT_DIR/$${BASE}_test_;\
	     command="rstxml2xml.py -o $$OUT_FILE $$the_file";\
	     eval $$command;\
	      done

nooutfile: 
	files=`ls *xml`; for the_file in $$files; do \
	     BASE=`basename  $$the_file .xml`;\
	     EXT=`echo "$$the_file"|awk -F . '{print $$NF}'`;\
	     OUT_DIR=final;\
	     OUT_FILE=$$OUT_DIR/$${BASE}_test_;\
	     command="python ../rstxml2xml.py $$the_file" > $$OUT_FILE;\
	     eval $$command;\
	      done
diff:
	cd final; files=`ls *xml`; for the_file in $$files; do \
	     BASE=`basename  $$the_file .xml`;\
	     EXT=`echo "$$the_file"|awk -F . '{print $$NF}'`;\
	     TEST_FILE=$${BASE}_test_;\
	    diff $$the_file $$TEST_FILE;\
	    done

clean:
	rm -f final/*_test_

>>>>>>> 30665a03f9af0025ac7f44d3b46a3b6df1db009f
