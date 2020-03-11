for inputfile in *.jpg; do
    outputfile="images_red/${inputfile%.*}.jpg"
    convert "$inputfile" -resize 64x64 "$outputfile"
done