echo "Do that? [gene,mRNA]"
read input
case $input in  
  gene|GENE|Gene) echo "gene|GENE|Gene" ;; 
  mrna|MRNA|mRNA|Mrna) echo "mrna|MRNA|mRNA|Mrna" ;; 
  *) echo "fsalsche eingabe" ;; 
esac
