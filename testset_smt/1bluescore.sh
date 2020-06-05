


~/Desktop/satsahib/mosesdecoder/scripts/generic/multi-bleu.perl -lc 12testRefSmall.eng < 13testpredSmall.eng > 1BLEUSmall.txt
~/Desktop/satsahib/mosesdecoder/scripts/generic/multi-bleu.perl -lc 16testRefMedium.eng < 17testpredMedium.eng > 28BLEUMedium.txt
~/Desktop/satsahib/mosesdecoder/scripts/generic/multi-bleu.perl -lc 20testRefLarge.eng < 21testpredLarge.eng > 3BLEULarge.txt
~/Desktop/satsahib/mosesdecoder/scripts/generic/multi-bleu.perl -lc test.eng < testpredsmt.eng > 4BLEUComplete.txt





perl ~/Desktop/satsahib/apertium-eval-translator-master/apertium-eval-translator-master/WER.pl -t testpred.eng -r test.eng

perl ~/Desktop/satsahib/apertium-eval-translator-master/apertium-eval-translator-master/PER.pl -t testpred.eng -r test.eng



perl ~/Desktop/satsahib/apertium-eval-translator-master/apertium-eval-translator-master/apertium-eval-translator-line.pl -t testpred.eng -r test.eng









