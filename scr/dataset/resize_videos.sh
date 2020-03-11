for i in *.mp4;
 do name=`echo $i | cut -d'.' -f1`;
 echo $name;
 ffmpeg -i $i -s 64x64 -c:a copy videos_red/$name.mp4;
done