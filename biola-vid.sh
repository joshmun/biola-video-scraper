python scrape-biola.py

while read link ; do 
  youtube-dl -o "~/Desktop/Biola/OT_Survey/%(title)s.%(ext)s" $link
done < vidlinks.txt
echo "Finished downloading, enjoy! 🎉"